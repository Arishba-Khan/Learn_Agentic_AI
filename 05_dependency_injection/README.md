# 🔑 **FastAPI Dependency Injection Demo**  
*Secure your API endpoints with headers and query parameters using FastAPI’s dependency system.*

---

## 🚀 **What This Code Does**  
This API shows how to use **dependency injection** to:  
1. **Authenticate users** with a secret token (sent in headers).  
2. **Validate required inputs** (like an `item_id` query parameter).  
3. Combine both checks cleanly using FastAPI’s `Depends()`.

---

## 🛠️ **Testing with Postman**  
Let’s test the `/favorite` endpoint step-by-step:  

### **Step 1: Set Up the Request**  
1. Open Postman.  
2. Create a new `GET` request.  
3. Set the URL to:  
   ```  
   http://localhost:8000/favorite  
   ```  

---

### **Step 2: Test Valid Requests**  
#### ✅ **Case 1: Valid Token + Valid `item_id`**  
- **Headers**:  
  | Key       | Value           |  
  |-----------|-----------------|  
  | `X-Token` | `mysecrettoken` |  

- **Query Parameters**:  
  | Key       | Value |  
  |-----------|-------|  
  | `item_id` | `42`  |  

**Expected Response (200 OK)**:  
```json  
{  
  "user": "authorized",  
  "favorite_item": "Item 42"  
}  
```  

---

### **Step 3: Test Invalid Requests**  
#### ❌ **Case 1: Missing/Invalid Token**  
- **Headers**: Omit `X-Token` or use a wrong value (e.g., `123`).  
- **Query Parameters**: `item_id=42`.  

**Expected Error (403 Forbidden)**:  
```json  
{  
  "detail": "Invalid or Missing Token"  
}  
```  

#### ❌ **Case 2: Missing `item_id`**  
- **Headers**: `X-Token: mysecrettoken`.  
- **Query Parameters**: None.  

**Expected Error (400 Bad Request)**:  
```json  
{  
  "detail": "Item ID is required"  
}  
```  

---

## 🔧 **Key Components Explained**  
### 1. **Token Authentication (`get_token`)**  
- Checks for the `X-Token` header.  
- Only accepts `mysecrettoken`.  

### 2. **Item ID Validation (`get_item_id`)**  
- Requires an `item_id` as a query parameter.  
- Example URL: `/favorite?item_id=42`.  

### 3. **Dependency Injection**  
- `Depends(get_token)` and `Depends(get_item_id)` run automatically before the endpoint.  
- Reusable across multiple endpoints.  

---

## 📖 **Why This Matters**  
- **Security**: Protect endpoints with tokens/API keys.  
- **Data Quality**: Ensure required parameters are provided.  
- **Clean Code**: Keep validation logic separate from business logic.  

---

## 🧠 **Key Terms**  
| Term                | Explanation                                  | Example                     |  
|---------------------|----------------------------------------------|-----------------------------|  
| **Header**          | Hidden data sent with the request            | `X-Token: mysecrettoken`    |  
| **Query Parameter** | Visible key-value pairs in the URL           | `?item_id=42`               |  
| **Dependency**      | Reusable validation/authentication logic     | `get_token`, `get_item_id`  |  

---

🔧 *For setup instructions, see the main README file.*  

--- 
