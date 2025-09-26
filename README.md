
# ChatMCA 🧠💬  
*A Django-Based AI-Powered Chatbot using Azure OpenAI*  

## 📌 Overview  
**ChatMCA** is a web-based chatbot application built with the **Django framework** and integrated with **Azure OpenAI services** to provide intelligent conversational experiences.  
The project focuses on delivering a **clean, modern, and user-friendly interface** similar to popular chat platforms — but rebranded as **ChatMCA**.  

## ✨ Features  
- 🔹 Django-powered backend for scalability and maintainability  
- 🔹 Real-time AI-driven chat powered by **Azure OpenAI**  
- 🔹 Modern and minimal UI styled to mimic a popular chatbot experience  
- 🔹 Secure API integration with environment variable support  
- 🔹 Responsive design for desktop and mobile users  

## 🛠️ Tech Stack  
- **Backend**: Django (Python 3.x)  
- **Frontend**: HTML, CSS, JavaScript (with Bootstrap/Tailwind)  
- **AI Engine**: Azure OpenAI (ChatGPT or GPT models)  
- **Database**: SQLite (default), can be upgraded to PostgreSQL/MySQL  
- **Deployment Options**: Azure Web App / Docker / Heroku  

## ⚙️ Installation & Setup  

### 1. Clone the Repository  
```bash
git clone https://github.com/your-username/ChatMCA.git
cd ChatMCA
````

### 2. Create Virtual Environment & Install Dependencies

```bash
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows

pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file in the root directory and add:

```
AZURE_OPENAI_API_KEY=your_api_key_here
AZURE_OPENAI_ENDPOINT=https://your-endpoint.openai.azure.com/
DJANGO_SECRET_KEY=your_secret_key_here
DEBUG=True
```

### 4. Apply Migrations

```bash
python manage.py migrate
```

### 5. Run the Development Server

```bash
python manage.py runserver
```

Visit 👉 **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)** to start chatting!

---


## 🚀 Future Enhancements

* Add **user authentication & history tracking**
* Support for **multiple languages**
* Real-time streaming responses
* Integration with **speech-to-text** and **text-to-speech**

---

## 🤝 Contribution

Contributions are welcome! Feel free to **fork** this repo, create a new branch, and submit a PR.

---

## 📜 License

This project is licensed under the **MIT WPU Pune License** – feel free to use and modify.

---

## 👨‍💻 Author

**Chavhan Mauli Shivaji**
📧 [maulichawan928@gmail.com](mailto:maulichawan928@gmail.com)
🔗 [LinkedIn](https://linkedin.com/in/mauli-chavhan) | [GitHub](https://github.com/maulichawan)


