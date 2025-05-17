
---

#  **Data Validation Made Simple with Python**  
*Learn how to validate user input (like names, colors, weights) using Python’s Pydantic library.*

---

## 🚀 **What Does This Code Do?**  
This script ensures that **data entered by users** (e.g., in a form or app) follows specific rules. For example:  
- Names must be text, not numbers.  
- Colors can *only* be "Black" or "red".  
- Weights must be positive numbers (like `1.8`, not `0` or `-5`).  

If the data breaks these rules, the script **catches errors automatically** and tells you what’s wrong!

---

## 🛠️ **How It Works**  
The code uses `Pydantic` (a Python library) to define a **data template** called `UserData`. Here’s what each part means:  

| Field    | Rule                                                                 | Example Valid Input         |  
|----------|----------------------------------------------------------------------|------------------------------|  
| `name`   | Must be text (string)                                               | `"Arishba Khan"`             |  
| `color`  | Can *only* be `'Black'` or `'red'` (case-sensitive!)                | `'Black'`                    |  
| `weight` | Must be a positive number (> 0)                                     | `1.8`                        |  
| `item`   | A dictionary with text keys and lists of tuples (see example below) | `{'Football': [(1, True, 0.1)]}` |  

---

## 📝 **Example**  
### ✅ **Valid Input**  
```python  
UserData(  
  name="Arishba Khan",  
  color='Black',  
  weight=1.8,  
  item={'Football': [(1, True, 0.1)]},  
)  
```  
→ This works because all fields follow the rules.  

### ❌ **Invalid Input**  
```python  
UserData(  
  name=7,  # ❌ Name must be text, not a number!  
  color='red',  
  weight=2.8,  
  item={'basketball': [(1, True, 0.1)]},  
)  
```  
→ **Error message**:  
`name: Input should be a valid string`  

---

## 🤔 **Why Should I Care?**  
- **Avoid crashes**: Stop bugs caused by bad data (e.g., negative weights).  
- **Clean data**: Force users to enter values in the correct format.  
- **Learn Python skills**: This is how real apps validate forms, APIs, and user inputs!  

---

## 🛑 **Common Errors & Fixes**  
| Error                          | Why It Happens                     | How to Fix                          |  
|--------------------------------|------------------------------------|-------------------------------------|  
| `color` is `'black'` (lowercase) | Only `'Black'` or `'red'` allowed  | Use uppercase `'Black'`            |  
| `weight` is `0`                | Weight must be > 0                | Enter a positive number like `0.1` |  
| `name` is a number             | Names must be text                | Wrap in quotes: `"Alex"`           |  

---

## ⚙️ **How to Use This Code**  
1. **Install Pydantic**:  
   ```bash  
   pip install pydantic  
   ```  
2. Copy the code into a Python file (e.g., `validate_data.py`).  
3. Run it! Test with your own values to see errors in action.  

---

## 🧠 **Learn More**  
- **Pydantic**: Used here for real-time data validation.  
- **Type Hints**: Python’s way of declaring data types (e.g., `str`, `float`).  

**Perfect for**: Students, new developers, or anyone who wants to ensure their Python apps handle data safely! 🌟  

--- 

**Feel free to tweak the rules (like adding new colors or stricter limits) and experiment!** 🚀
