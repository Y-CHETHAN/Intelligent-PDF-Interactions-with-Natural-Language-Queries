import os
import json
from langchain.llms import OpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores.cassandra import Cassandra
from langchain.indexes import VectorstoreIndexCreator
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import PyPDFLoader
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from copy import deepcopy
from tempfile import NamedTemporaryFile
import streamlit as st

@st.cache_resource
def create_datastax_connection():

    cloud_config= {'secure_connect_bundle': 'secure-connect-pdf-qa.zip'}

    with open("pdf_qa_bot-token.json") as f:
        secrets = json.load(f)

    CLIENT_ID = secrets["clientId"]
    CLIENT_SECRET = secrets["secret"]

    auth_provider = PlainTextAuthProvider(CLIENT_ID, CLIENT_SECRET)
    cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
    astra_session = cluster.connect()
    return astra_session

def main():

    index_placeholder = None
    st.set_page_config(page_title = "Chat with your PDF", page_icon="📔")
    st.header('📔 Chat with your PDF')
    
    if "conversation" not in st.session_state:
        st.session_state.conversation = None

    if "activate_chat" not in st.session_state:
        st.session_state.activate_chat = False

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"], avatar = message['avatar']):
            st.markdown(message["content"])

    session = create_datastax_connection()

    os.environ['OPENAI_API_KEY'] = "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"
    llm = OpenAI(temperature=0)
    openai_embeddings = OpenAIEmbeddings()
    table_name = 'qa_mini_demo'
    keyspace = 'default_keyspace'

    out_index_creator = VectorstoreIndexCreator(
            vectorstore_cls = Cassandra,
            embedding = openai_embeddings,
            text_splitter = RecursiveCharacterTextSplitter(
            chunk_size = 400,
            chunk_overlap = 30),
            vectorstore_kwargs={
            'session': session,
            'keyspace': keyspace,
            'table_name': table_name}
        )
    
    with st.sidebar:
        st.subheader('Upload Your PDF File')
        docs = st.file_uploader('⬆️ Upload your PDF & Click to process',
                                accept_multiple_files = False, 
                                type=['pdf'])
        if st.button('Process'):
            with NamedTemporaryFile(dir='.', suffix='.pdf', delete=False) as f:
                f.write(docs.getbuffer())
                with st.spinner('Processing'):
                    file_name = f.name
                    loader = PyPDFLoader(file_name)
                    pages = loader.load_and_split()
                    for doc in pages:
                      doc.metadata = {"source": "document123", "title": "Document"}
                    pdf_index = out_index_creator.from_loaders([loader])
                    if "pdf_index" not in st.session_state:
                        st.session_state.pdf_index = pdf_index
                    st.session_state.activate_chat = True

    if st.session_state.activate_chat:
        if prompt := st.chat_input("Ask your question from the PDF?"):
            with st.chat_message("user", avatar = '👨🏻'):
                st.markdown(prompt)
            st.session_state.messages.append({"role": "user", 
                                              "avatar" :'👨🏻',
                                              "content": prompt})

            index_placeholder = st.session_state.pdf_index
            pdf_response = index_placeholder.query_with_sources(prompt, llm = llm)
            cleaned_response = pdf_response["answer"]
            with st.chat_message("assistant", avatar='🤖'):
                st.markdown(cleaned_response)
            st.session_state.messages.append({"role": "assistant", 
                                              "avatar" :'🤖',
                                              "content": cleaned_response})
        else:
            st.markdown(
                'Upload your PDF to chat'
                )

if __name__ == '__main__':
    main()