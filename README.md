---
title: MedChat
emoji: 🌍
colorFrom: purple
colorTo: pink
sdk: streamlit
sdk_version: 1.41.1
app_file: app.py
pinned: false
license: apache-2.0
---
# 
# 🩺 **MedChat** 🌟


Welcome to the **MedChat**! 🌍  
A Medical Knowledge Assistant , cutting-edge tool designed to help you with all your medical queries. Whether you're a student, a healthcare professional, or just someone curious about health topics, this tool will provide you with **detailed, in-depth explanations** on a wide range of medical topics. From symptoms, causes, and treatments to complex medical terms and theories, we've got you covered!

---

## 🚀 **Features**

- **Detailed Answers**: Get comprehensive and accurate responses to your medical queries, including definitions, causes, symptoms, and treatments.
- **Medical Comparison**: Easily compare two conditions or medical terms with structured and detailed differences.
- **Accessible for All**: Powered by Hugging Face Spaces, anyone with the link can use it — no account or installation required!
- **Real-Time Streaming**: Get responses on the fly, as we use Groq's API for real-time model completion.

---

## 💡 **How it Works**

1. **Vectorized Medical Knowledge**: The assistant has been trained on a vast collection of medical books, which have been **vectorized** to provide you with accurate and contextually relevant answers.
2. **Groq's Magic**: When you ask a question, we pull relevant information from the medical dataset and send it to Groq’s AI for an insightful, medically accurate response.
3. **Streamlit UI**: A fun and easy-to-use interface to interact with your medical assistant. Just type your question and get answers!

---

## 🛠 **Setup**

If you’re trying to run this locally or want to get technical with it, follow the steps below. But if you just want to **ask medical questions**, head straight to the deployed link (below) and start typing! 🚀

### **Requirements**

- Python 3.8+
- Streamlit
- Hugging Face API Key (for Groq integration)
- Chroma (for vector store)
- Pre-trained embeddings model: `BAAI/bge-large-en`

### **Installing Dependencies**

1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/med-knowledge-assistant.git
   cd med-knowledge-assistant
Install required dependencies:

bash
Copy code
```
pip install -r requirements.txt
```
Set your environment variables (you’ll need a Groq API Key):

Create a .env file and add:
makefile
Copy code
```python
GROQ_API_KEY=your_api_key_here
```
Run the Streamlit app locally:

bash
Copy code
```python
streamlit run app.py
```

## 🌐 Access the Medical Knowledge Assistant
You can start asking your questions right away! Just visit the link below and have your medical queries answered:

[**Medical Knowledge Assistant on Hugging Face**](https://huggingface.co/spaces/yash001010/MedChat)


##  🎉 Example Use Cases
"What is the difference between Type 1 and Type 2 Diabetes?"
"What are the symptoms of the flu?"
"Explain the treatment process for a heart attack."

## ✨ Contributing
If you’re passionate about medicine and AI and want to help improve this project, feel free to contribute! You can:

Add more medical content to the dataset.
Improve the UI/UX of the Streamlit app.
Suggest new features or report bugs.
Feel free to fork the repository, create an issue, or submit a pull request!

##  📝 Disclaimer
This tool is intended for informational purposes only. While we aim to provide accurate and reliable information, always consult a medical professional for diagnosis or treatment.

## 📱 Contact
For any questions or feedback, reach out to:

Email: yshtrivdi@gmail.com
