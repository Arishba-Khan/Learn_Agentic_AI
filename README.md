# 🌟 **Generative AI Learning Lab**  
*A zero-fuss repository to learn GenAI concepts through practical projects.*  

**Start Here →** Before coding, read the **[01_generative_ai.md](01_generative_ai.md)** to understand core GenAI concepts!  

---

## 🚀 **Why This Repo?**  
- **No Virtual Environments**: Uses UV’s app mode for simple dependency management.  
- **Beginner-Centric**: Minimal setup, maximum learning.  
- **Hands-On Projects**: Start with APIs, then move to advanced GenAI models.  
- **Always Updated**: New projects added weekly!  

---

## 🛠️ **Setup Guide (UV App Mode)**  

### **1. Prerequisites**  
- **Python 3.10+**: [Download Python](https://www.python.org/downloads/)  
- **UV**: A modern Python package manager.  
  ```bash  
  pip install uv  
  ```  

### **2. Create Project in VS Code**  
1. Open VS Code.  
2. Create a folder (e.g., `task-manager-api`).  

### **3. Initialize UV App**  
In your project folder’s terminal:  
```bash  
uv init --app  
```  
*(This creates a `pyproject.toml` file for dependency tracking.)*  

### **4. Add Dependencies**  
```bash  
uv add fastapi[standard] uvicorn  
```  
*(UV automatically resolves and installs packages.)*  

### **5. Run the API**  
```bash  
uv run uvicorn main:app --reload  
```  
- **Interactive Docs**: Visit [http://localhost:8000/docs](http://localhost:8000/docs)  

---

## 📡 **Testing with Postman**  
**What is Postman?**  
A free tool to test APIs by sending requests (GET/POST/PUT) and viewing responses.  

**Quick Test**:  
1. Install [Postman](https://www.postman.com/downloads/).  
2. Send a `GET` request to `http://localhost:8000/users/1`.  

---

## 🗂️ **Project Structure**  
```  
task-manager-api/  
├── .uv/                 # UV-managed dependencies (auto-created)  
├── main.py              # Your FastAPI code  
└── pyproject.toml       # Dependency list (managed by UV)  
```  

---

## 💡 **Tips & Tricks**  

### **For UV App Mode**  
- **Update Dependencies**:  
  ```bash  
  uv add --upgrade fastapi  
  ```  
- **No Activation Needed**: UV handles dependencies per-project automatically!  

### **Learning GenAI**  
1. **Start Small**: Master APIs before diving into LLMs.  
2. **Break Things**: Intentionally cause errors (e.g., send invalid dates) to learn validation.  
3. **Use AI Assistants**: Ask ChatGPT/Bard to explain unfamiliar code blocks.  

### **GitHub Basics**  
1. **Ignore UV Cache**: Add `.uv/` to `.gitignore` to avoid committing dependency files.  
2. **Commit Code**:  
   ```bash  
   git add main.py pyproject.toml  
   git commit -m "Added task manager API"  
   ```  

---

## 🚨 **Troubleshooting**  
| Issue                          | Fix                                                                 |  
|--------------------------------|---------------------------------------------------------------------|  
| `uv: command not found`        | Reinstall UV: `pip install uv`                                     |  
| `ModuleNotFoundError`          | Run `uv add <missing-package>` (e.g., `uv add pydantic`)           |  
| Port 8000 in use               | Stop other servers: `kill -9 $(lsof -ti:8000)` (Mac/Linux)         |  



---

 *Star ⭐ this repo to track updates!*

--- 
