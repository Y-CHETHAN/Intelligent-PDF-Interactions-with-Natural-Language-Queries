# Intelligent PDF Interactions with Natural Language Queries
## About
The goal of this project is to develop a system that can answer natural language queries about the content of a PDF document. The system should be able to understand the content of the PDF and answer questions about it. The project is divided into three main parts:
1. **PDF Preprocessing**: Extracting the text from the PDF and preprocessing it to make it suitable for the next steps.
2. **Question Answering**: Answering the natural language queries about the content of the PDF.
3. **User Interface**: Providing a user interface to interact with the system.

## Features
- Extract text from PDF
- Preprocess the text
- Answer natural language queries
- User interface

## Requirements 
- Python 3.x installed on your system.
- Required Python libraries:
  1. langchain
  2. langchain.vectorstores.cassandra
  3. langchain.indexes.vectorstore
  4. langchain.embeddings
  5. langchain.text_splitter
  6. streamlit
  7. PyPDF2

## Usage
1. Clone the repository:

```
git clone https://github.com/Y-CHETHAN/Intelligent-PDF-Interactions-with-Natural-Language-Queries.git
```
2. Install dependencies
3. Set up necessary environment variables:

- ASTRA_DB_APPLICATION_TOKEN: Your Astra DB application token.
- ASTRA_DB_ID: Your Astra DB ID.
- OPENAI_API_KEY: Your OpenAI API key.
  
4. Navigate to your Jupyter Notebook file (*.ipynb) and open it.

- Run all cells in the notebook to ensure that all necessary variables are defined and data processing steps are completed.

- Check for any errors or warnings during execution and resolve them if necessary.

- Once the notebook has been successfully executed, save any changes and close the notebook.

5.Run the Streamlit app:
streamlit run pdf_chatbot.py

## System Architecture
![Blank diagram](https://github.com/Y-CHETHAN/Intelligent-PDF-Interactions-with-Natural-Language-Queries/assets/75234991/77b2128c-401d-4655-a806-1a62337abbf7)
 

## Output
![Chat with your PDF - Opera 28-02-2024 17_43_29](https://github.com/Y-CHETHAN/Intelligent-PDF-Interactions-with-Natural-Language-Queries/assets/75234991/9270f1a2-9782-4cab-98dd-14259c6e757a)

## User Interface:
![Chat with your PDF - Opera 28-02-2024 17_40_27](https://github.com/Y-CHETHAN/Intelligent-PDF-Interactions-with-Natural-Language-Queries/assets/75234991/80d0fffe-d4bd-47c0-98b8-064dd4453ca1)

## Results and Impacts
1. The system enables users to interact with PDF documents using natural language queries, offering a seamless and intuitive interface.
2. Integration of advanced technologies such as Cassandra and OpenAI's language models enhances the system's capabilities in processing and responding to user queries.
3. Experimental evaluations demonstrate the system's efficacy and accuracy in retrieving precise information from digital documents.
4. The project contributes to advancing the field of intelligent PDF interactions, providing a sophisticated and user-centric solution for efficient document analysis and extraction of meaningful insights.

## Future Directions:
Further enhancements could include support for more document formats, improved handling of complex queries, and integration of additional language models for enhanced response generation.
Continuous evaluation and refinement of the system based on user feedback to ensure optimal performance and usability.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## References
1. Aggarwal, Mukul. "Information retrieval and question answering nlp approach: an artificial intelligence application." International Journal of Soft Computing and Engineering (IJSCE) 1, no. NCAI2011 (2011).
2. Braun, S., & Tsay, J. (2022). A chatbot for PDFs: Using LangChain and Pinecone to build a conversational AI assistant for document management. arXiv preprint arXiv:2201.08244.
3. Cai, H., & Liu, Z. (2022). A survey on large language models. arXiv preprint arXiv:2201.08237.
4. Clementeena, A., and P. Sripriya. "A literature survey on question answering system in natural language processing." International Journal of Engineering and Technology (2018) 7, no. 3.3 (2018): 452-455.
5. Devlin, J., Chang, M.-W., Lee, K., & Toutanova, K. (2018). Bert: Pre-training of deep bidirectional transformers for language understanding. arXiv preprint arXiv:1810.04805.


