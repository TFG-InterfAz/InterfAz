# InterfAz

Welcome to the **InterfAz** project! This web application utilizes AI models, such as Ollama or ChatGPT, to generate React components dynamically based on user input. The backend is powered by Django, ensuring a robust and scalable foundation for the application.

## Features

- **AI-Powered React Component Generation**: Input descriptions or requirements, and the app generates functional React components.
- **User-Friendly Interface**: Intuitive UI for providing prompts and receiving generated code.
- **Seamless Integration**: Download generated React components or copy them directly into your project.
- **Extensibility**: Designed to support various AI models and customizations.

## Tech Stack

### Frontend
- **React**: For building the user interface.
- **JavaScript/TypeScript**: For enhanced functionality and typing support.

### Backend
- **Django**: A robust and flexible Python web framework.
- **Django REST Framework (DRF)**: For building API endpoints.

### AI Integration
- **OpenAI GPT or LLaMA**: To handle the AI generation logic.

## Installation

### Prerequisites
Ensure you have the following installed:
- Python (>= 3.8)
- Node.js (>= 14.x)
- npm
- PostgreSQL (for Django backend)
- Ollama: https://ollama.com/

### Hardware
Ensure your PC can handle llama2:

1.**GPU (Recommended for Faster Inference):**
 - Minimum: NVIDIA GTX 1660 Ti (6GB VRAM) with 4-bit quantization
 - Recommended: RTX 3060 (12GB VRAM) or better
   
2.**CPU (If running without GPU):**
 - Minimum: 6-core CPU (e.g., Intel Core i7-10750H or better)
 - Recommended: 8-core or higher (e.g., AMD Ryzen 7 5800H)
   
3.**RAM:**
 - Minimum: 16GB
 - Recommended: 32GB for better performance
   
4.**Storage:**
 - Minimum: 30GB SSD (for model weights)
 - Recommended: NVMe SSD for faster loading
   
5.**OS:**
 - Linux or Windows 10/11 with WSL (if needed for compatibility)
  
### 1 Configurate the DataBase
Enter in postgresql's bash:

`cd "C:\Program Files\PostgreSQL\17\bin"`
`psql -U postgres`

Create the database and the user. Introduce the following commands:

```
CREATE DATABASE interfaz;
CREATE USER interfaz_user WITH PASSWORD 'interfaz_password';
GRANT ALL PRIVILEGES ON DATABASE interfaz TO interfaz_user;
\c interfaz;
GRANT USAGE ON SCHEMA public TO interfaz_user;
GRANT CREATE ON SCHEMA public TO interfaz_user;
GRANT ALL PRIVILEGES ON SCHEMA public TO interfaz_user;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL PRIVILEGES ON TABLES TO interfaz_user;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL PRIVILEGES ON SEQUENCES TO interfaz_user;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL PRIVILEGES ON FUNCTIONS TO interfaz_user;

\q
```


### 2 Backend Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/ai-react-generator.git](https://github.com/TFG-InterfAz/InterfAz.git
   ```
2. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate
   # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Apply migrations:
   ```bash
   python manage.py migrate
   ```
5. Start the server:
   ```bash
   python manage.py runserver
   ```
#### 2.1 Starcoder Setup
1. Log in using a token:
   ```bash
   huggingface-cli login
   ```
   token = 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

#### 2.2 Ollama Setup
1. Go to Ollama: https://ollama.com/ and download it
2. Install Ollama
3. Open any terminal and run:
```bash
ollama pull llama2
```

#### 2.2 Create virtual environment, install requirements, execute
Using anaconda we isolate the development environment and handle dependencies.

Open anaconda prompt and run:

```bash
conda create -n interfaz python=3.10.16
conda env list
```

In vscode, CTRL+Shift+P and select: “Python: Select Interpreter”
Choose the new interface
Open a new terminal cmd in the workspace and check the use of interfaz. Execute:
```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Navigating in `http://127.0.0.1:8000/`, you could check the web app.


### 3 Frontend Setup
1. Navigate to the `frontend` directory:
   ```bash
   cd frontend
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Start the development server:
   ```bash
   npm start
   ```

## Usage
1. Open your browser and navigate to `http://127.0.0.1:8000` (backend) and `http://localhost:3000` (frontend).
2. Input a description or prompt for the desired React component.
3. Receive the generated code and preview or download it.

## Folder Structure
```plaintext
ai-react-generator/
├── backend/         # Django backend
│   ├── manage.py    # Django project manager
│   ├── app/         # Core app logic
├── frontend/        # React frontend
│   ├── src/         # Source files
│   ├── public/      # Static files
├── requirements.txt # Python dependencies
├── README.md        # Project documentation
```

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and push them to your fork.
4. Submit a pull request.

## License
This project is licensed under the [placeholder](LICENSE).

## Contact
For questions or feedback, please contact **ivan.ramirez.lara18@gmail.com** or create an issue on GitHub.
