# 🌐 **FastAPI Parameters: Path vs Query Demo**  
*Learn the difference between path parameters and query parameters in FastAPI with simple examples.*  

---

## 🛠️ **What This Code Does**  
This FastAPI app demonstrates two ways to pass data in URLs:  
1. **Path Parameters** (Dynamic URL segments).  
2. **Query Parameters** (Optional key-value pairs after `?` in the URL).  

---

### 📍 **Endpoint 1: Path Parameter**  
**URL**: `/items/{item_id}`  
**Example**: `/items/apple`  
**Response**:  
```json  
{"item_id": "apple"}  
```  
- **What’s happening**:  
  - `{item_id}` is a **path parameter** – it’s part of the URL structure.  
  - Used to fetch specific resources (e.g., details for item "apple").  

---

### 🔍 **Endpoint 2: Query Parameter**  
**URL**: `/items?item_id=apple`  
**Response**:  
```json  
{"item_id": "apple"}  
```  
- **What’s happening**:  
  - `item_id=apple` is a **query parameter** – optional and added after `?`.  
  - Used for filtering/searching (e.g., `?category=fruit&price<10`).  

---

## 🚀 **Try It Yourself**  
1. Visit `/items/apple` → Uses a **path parameter**.  
2. Visit `/items?item_id=apple` → Uses a **query parameter**.  

---

## 📖 **Key Differences**  

| Feature          | Path Parameter                    | Query Parameter                  |  
|------------------|-----------------------------------|----------------------------------|  
| **URL Example**  | `/items/apple`                    | `/items?item_id=apple`          |  
| **Use Case**     | Required for unique resources     | Optional filtering/sorting      |  
| **Structure**    | Part of the URL path              | Added after `?` (key=value)     |  
| **Required?**    | Yes (unless optional with `=None`) | No (optional by default)        |  

---

## 💡 **Why This Matters**  
- **Path parameters** define *what* you’re accessing (e.g., user profiles: `/users/arishba`).  
- **Query parameters** define *how* you want data (e.g., sorting: `?sort=price&order=asc`).  

---

🔧 *For setup instructions, see the main README file.*  

--- 
