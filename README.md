# 📚 StudySage - Offline AI Study Assistant

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/DheerajNair123/StudySage.svg)](https://github.com/DheerajNair123/StudySage/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/DheerajNair123/StudySage.svg)](https://github.com/DheerajNair123/StudySage/network)
[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/streamlit-1.28+-red.svg)](https://streamlit.io/)

> An intelligent offline AI study assistant that helps you interact with your study materials using local language models

## 🎯 Overview

StudySage is a powerful offline AI study assistant that allows students to upload PDF documents (notes, chapters, textbooks) and ask questions about the content. Built with privacy in mind, it runs entirely offline using local language models, ensuring your study materials never leave your device.

The application uses advanced natural language processing to understand your documents and provide accurate, contextual answers to help enhance your learning experience.

## ✨ Features

- **📄 PDF Document Processing**: Upload and extract text from PDF files
- **🤖 Offline AI Chat**: Ask questions about your uploaded materials using Llama3 model
- **🔍 Intelligent Search**: Advanced vector-based document retrieval for accurate answers
- **🖥️ User-Friendly Interface**: Clean Streamlit web interface
- **🔒 Privacy-First**: Completely offline - your documents never leave your device
- **⚡ Fast Responses**: Optimized vector search for quick question answering

## 🛠️ Technologies Used

- **Frontend**: Streamlit (Web Interface)
- **Backend**: Python
- **Language Model**: Ollama (Llama3)
- **Document Processing**: PyMuPDF (fitz)
- **Vector Database**: FAISS
- **Embeddings**: HuggingFace Sentence Transformers (all-MiniLM-L6-v2)
- **Framework**: LangChain (RAG Implementation)

## 📋 Prerequisites

Before installing StudySage, ensure you have:

- **Python 3.8+** installed on your system
- **Ollama** installed and running
- **Llama3 model** downloaded via Ollama

### Installing Ollama and Llama3

1. **Install Ollama**:
   - Visit [Ollama's official website](https://ollama.com/) and follow installation instructions for your OS
   - Or use: `curl -fsSL https://ollama.com/install.sh | sh` (Linux/macOS)

2. **Download Llama3 model**:
   ```bash
   ollama pull llama3
   ```

3. **Verify installation**:
   ```bash
   ollama list
   ```

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/DheerajNair123/StudySage.git
   cd StudySage
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv studysage_env
   source studysage_env/bin/activate  # On Windows: studysage_env\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create required directories**
   ```bash
   mkdir -p data/uploaded_docs
   ```

5. **Start Ollama service** (if not already running)
   ```bash
   ollama serve
   ```

## 🎮 Usage

1. **Start the application**
   ```bash
   streamlit run main.py
   ```

2. **Access the web interface**
   - Open your browser and go to `http://localhost:8501`

3. **Upload and Query**
   - Upload a PDF file using the file uploader
   - Type your question in the text input box
   - Get AI-powered answers based on your document content

### Example Workflow

1. Upload a PDF textbook chapter or study notes
2. Ask questions like:
   - "What is the main concept explained in this chapter?"
   - "Summarize the key points about photosynthesis"
   - "What are the different types of algorithms mentioned?"
3. Receive contextual answers extracted from your uploaded material

## 📁 Project Structure

```
StudySage/
├── main.py                 # Main Streamlit application
├── document_parser.py      # PDF text extraction utilities
├── vector_store.py         # FAISS vector store implementation
├── chat_engine.py          # RAG chain setup with Ollama
├── requirements.txt        # Python dependencies
├── data/
│   └── uploaded_docs/      # Directory for uploaded PDF files
├── README.md
└── LICENSE
```

## 🔧 Configuration

The application uses the following default configurations:

- **Language Model**: Llama3 via Ollama
- **Embedding Model**: sentence-transformers/all-MiniLM-L6-v2
- **Vector Store**: FAISS (CPU version)
- **Retrieval Method**: RetrievalQA with similarity search

## 🤝 Contributing

We welcome contributions to StudySage! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. **Make your changes and test them**
4. **Commit your changes**
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```
5. **Push to the branch**
   ```bash
   git push origin feature/AmazingFeature
   ```
6. **Open a Pull Request**

### Development Guidelines

- Follow PEP 8 style guidelines
- Add docstrings to functions
- Test your changes thoroughly
- Update documentation as needed

## 🐛 Troubleshooting

### Common Issues

**Ollama not found error**
- Ensure Ollama is installed and running: `ollama serve`
- Verify Llama3 model is downloaded: `ollama list`

**PDF upload issues**
- Ensure the `data/uploaded_docs/` directory exists
- Check file permissions for the upload directory

**Slow responses**
- Consider using a smaller embedding model
- Ensure sufficient RAM for the language model

## 📊 Performance Notes

- **Memory Usage**: Requires ~4-8GB RAM depending on document size
- **Response Time**: 2-10 seconds per query (varies by hardware)
- **Supported Formats**: Currently PDF only
- **File Size Limit**: Recommended <50MB per PDF

## 🗺️ Roadmap

- [ ] Support for additional file formats (DOCX, TXT, EPUB)
- [ ] Multiple document chat capability
- [ ] Conversation history and context retention
- [ ] Custom model selection interface
- [ ] Document summarization features
- [ ] Export chat conversations
- [ ] Mobile-responsive interface improvements

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Dheeraj Nair**
- GitHub: [@DheerajNair123](https://github.com/DheerajNair123)
- Project Link: [StudySage](https://github.com/DheerajNair123/StudySage)

## 🙏 Acknowledgments

- **Ollama** for providing local language model capabilities
- **LangChain** for the RAG implementation framework
- **Streamlit** for the intuitive web interface
- **HuggingFace** for the embedding models
- **PyMuPDF** for PDF processing capabilities

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/DheerajNair123/StudySage/issues) page for existing solutions
2. Create a new issue with detailed information about your problem
3. Include your Python version, OS, and error messages when reporting bugs

---

**Happy Studying! 📚✨**

*StudySage - Making offline AI-powered learning accessible to everyone*
