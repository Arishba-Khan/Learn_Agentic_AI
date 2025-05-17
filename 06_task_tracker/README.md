# 🚀 **Task Manager API with FastAPI**  
*A simple API to manage users and tasks with validation and in-memory storage.*

---

## 🌟 **Features**  
- **User Management**: Create and retrieve users.  
- **Task Management**: Create, update, and fetch tasks with due dates and statuses.  
- **Validation**:  
  - Due dates cannot be in the past.  
  - Task statuses must be `pending`, `in_progress`, or `completed`.  
- **In-Memory Storage**: No database required (data resets on server restart).  

---

## 🛠️ **Installation**  
1. Install dependencies:  
   ```bash  
   pip install fastapi uvicorn pydantic  
   ```  
2. Copy the code into a file (e.g., `main.py`).  

---

## ⚡ **Run the API**  
```bash  
uvicorn main:app --reload  
```  
*(Access docs at `http://localhost:8000/docs`)*  

---

## 📡 **API Endpoints**  

### **Users**  
| Endpoint          | Method | Description                  | Example Request Body                     |  
|-------------------|--------|------------------------------|------------------------------------------|  
| `/users/`         | POST   | Create a new user            | `{"username": "alice", "email": "alice@example.com"}` |  
| `/users/{user_id}`| GET    | Get user details by ID       | N/A                                      |  

### **Tasks**  
| Endpoint               | Method | Description                  | Example Request Body                     |  
|------------------------|--------|------------------------------|------------------------------------------|  
| `/tasks/`              | POST   | Create a new task            | `{"title": "Homework", "due_date": "2024-12-31", "user_id": 1}` |  
| `/tasks/{task_id}`     | GET    | Get task details by ID       | N/A                                      |  
| `/tasks/{task_id}`     | PUT    | Update task status           | `{"status": "in_progress"}`              |  
| `/users/{user_id}/tasks` | GET  | Get all tasks for a user     | N/A                                      |  

---

## 🛑 **Validation Rules**  
### **Tasks**  
1. **Due Date**:  
   - Must be today or in the future.  
   - Example error: `"Due date cannot be in the past"`.  
2. **Status**:  
   - Allowed values: `pending`, `in_progress`, `completed`.  
   - Example error: `"Invalid status"`.  

### **Users**  
- Email must be valid (e.g., `user@example.com`).  

---

## 💡 **Example Usage**  
### Create a User  
**Request**:  
```bash  
POST http://localhost:8000/users/  
Body (JSON):  
{  
  "username": "alice",  
  "email": "alice@example.com"  
}  
```  

**Response**:  
```json  
{  
  "id": 1,  
  "username": "alice",  
  "email": "alice@example.com"  
}  
```  

### Create a Task  
**Request**:  
```bash  
POST http://localhost:8000/tasks/  
Body (JSON):  
{  
  "title": "Finish project",  
  "due_date": "2024-12-31",  
  "user_id": 1  
}  
```  

**Response**:  
```json  
{  
  "id": 1,  
  "title": "Finish project",  
  "due_date": "2024-12-31",  
  "status": "pending",  
  "user_id": 1  
}  
```  

---

## 🚨 **Error Handling**  
| Error Code | Meaning                          | Example Cause                     |  
|------------|----------------------------------|-----------------------------------|  
| `404`      | User/Task not found              | Invalid `user_id` or `task_id`    |  
| `422`      | Validation failed                | Past due date or invalid status   |  

---

## ⚠️ **Limitations**  
- Data is stored in memory (lost when the server restarts).  
- No authentication (for simplicity).  

--- 

🔧 *For setup instructions, see the main README file.*  

--- 
