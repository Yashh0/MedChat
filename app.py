import os
import streamlit as st
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceBgeEmbeddings
from groq import Groq
from dotenv import load_dotenv

# Initialize Streamlit page configuration
st.set_page_config(page_title="Medical Knowledge Assistant", layout="wide")

# Add API key input in sidebar
with st.sidebar:
    st.header("API Key Configuration")
    api_key = st.text_input("Enter your Groq API Key:", type="password")
    if api_key:
        os.environ['GROQ_API_KEY'] = api_key
    else:
        # Try loading from .env file
        load_dotenv()
        api_key = os.getenv("GROQ_API_KEY")
        if api_key:
            st.success("API Key loaded from .env file")

# Check for API key before proceeding
if not api_key:
    st.warning("Please enter your Groq API key in the sidebar to continue.")
    st.stop()

# Initialize the app
st.title("Medical Knowledge Assistant")

try:
    # Set up the embeddings
    model_name = "BAAI/bge-large-en"
    model_kwargs = {'device': 'cpu'}
    encode_kwargs = {'normalize_embeddings': False}
    embeddings = HuggingFaceBgeEmbeddings(
        model_name=model_name,
        model_kwargs=model_kwargs,
        encode_kwargs=encode_kwargs
    )

    # Load the vector store from the local drive
    script_dir = os.path.dirname(os.path.abspath(__file__))
    persist_directory = os.path.join(script_dir, 'Embedded_Med_books')
    
    # Debug information
    st.sidebar.header("Debug Information")
    st.sidebar.write("Vector store path:", persist_directory)
    
    with st.sidebar:
        st.write("API Key Loaded:", "Yes" if api_key else "No")

    # Check vector store directory
    if not os.path.exists(persist_directory):
        st.error(f"Vector store directory not found at: {persist_directory}")
        if st.button("Create Directory"):
            os.makedirs(persist_directory)
            st.success("Directory created!")
    
    # Load the vector store
    vector_store = Chroma(
        persist_directory=persist_directory,
        embedding_function=embeddings
    )
    retriever = vector_store.as_retriever(search_kwargs={'k': 1})
    
    # Initialize Groq client
    client = Groq(api_key=api_key)

    # Streamlit input
    query = st.text_input("Enter your medical question here:")

    def query_with_groq(query, retriever):
        try:
            # Retrieve relevant documents
            docs = retriever.get_relevant_documents(query)
            context = "\n".join([doc.page_content for doc in docs])

            # Call the Groq API with the query and context
            completion = client.chat.completions.create(
                model="llama3-70b-8192",
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are a knowledgeable medical assistant. For any medical term or disease, include comprehensive information covering: "
                            "definitions, types, historical background, major theories, known causes, and contributing risk factors. "
                            "Explain the genesis or theories on its origin, if applicable. Use a structured, thorough approach and keep language accessible. "
                            "provide symptoms, diagnosis, and treatment and post operative care , address all with indepth explanation , with specific details and step-by-step processes where relevant. "
                            "If the context does not adequately cover the user's question, respond with: 'I cannot provide an answer based on the available medical dataset.'"
                        )
                    },
                    {
                        "role": "system",
                        "content": (
                            "If the user asks for a medical explanation, ensure accuracy, don't include layman's terms if complex terms are used, "
                            "and organize responses in a structured way."
                        )
                    },
                    {
                        "role": "system",
                        "content": (
                            "When comparing two terms or conditions, provide a clear, concise, and structured comparison. Highlight key differences in their "
                            "definitions, symptoms, causes, diagnoses, and treatments with indepth explanation of each. If relevant, include any overlapping characteristics."
                        )
                    },
                    {
                        "role": "user",
                        "content": f"{context}\n\nQ: {query}\nA:"
                    }
                ],
                temperature=0.7,
                max_tokens=3000,
                stream=True
            )

            # Create a placeholder for streaming response
            response_container = st.empty()
            response = ""
            
            # Stream the response
            for chunk in completion:
                if chunk.choices[0].delta.content:
                    response += chunk.choices[0].delta.content
                    response_container.markdown(response)
            
            return response
            
        except Exception as e:
            st.error(f"Error during query processing: {str(e)}")
            return None

    if st.button("Get Answer"):
        if query:
            with st.spinner("Processing your query..."):
                answer = query_with_groq(query, retriever)
                if answer:
                    st.success("Query processed successfully!")
        else:
            st.warning("Please enter a query.")

except Exception as e:
    st.error(f"Initialization error: {str(e)}")