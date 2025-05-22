NAAN MUDHALVAN - IBM  
1 
COLLEGE CODE : 1125 
COLLEGE NAME : Sri Venkateswara Institute of Science 
and Technology, Tiruvallur 
DEPARTMENT :  CSE,AI&DS,AI&DS,ECE. 
STUDENT NM-ID : 
e5060b6759388fd9e8d4d11d31bf6529 
267d5bff03342c9b40c4e520d0034d22 
d432b6d442425ff91184ef687e792ee6 
67d6773e918cf5c9c3047fcd800d8080 
ROLL NO : 
112523104008 
112523243004 
112523243005 
112523106304 
DATE : 15/05/2025 
AI-Powered Supply Chain Management System 
SUBMITTED BY 
MOHAMED SAKEEN.P.K 
NARAYANAN.P 
SANTHOSH KUMAR.V 
VARUN KUMAR.G The AI-Powered Personalized Marketing and Customer Experience system will be 
demonstrated to stakeholders, showcasing its features, performance improvements, and 
functionality. This demonstration highlights the system’s targeted marketing capabilities, 
real-time data analysis, security measures, and performance scalability. By the end of the demonstration, the system’s ability to handle real-world scenarios, ensure 
data security, and deliver targeted marketing content will be showcased to the stakeholders. Comprehensive documentation for the AI-Powered Personalized Marketing and Customer 
Experience system is provided to detail every aspect of the project. This includes system 
architecture, AI model details, code explanations, and usage guidelines for both users and 
administrators. Feedback from the project demonstration will be collected from instructors, stakeholders, 
and a broader group of test users. This feedback will be used to make final refinements 
before project handover. # Supply Chain Management Dashboard

## Overview

This project is a **web-based Supply Chain Management Dashboard** developed using **Python (Flask)** and **HTML/CSS**. It displays real-time data for key areas of the supply chain:
- **Suppliers**
- **Inventory**
- **Orders**
- **Deliveries**

The goal is to provide a simple, readable dashboard interface that centralizes essential supply chain data for monitoring and decision-making.

---

## Features

- Built using **Flask**, a lightweight Python web framework.
- Dynamic rendering of structured data using Jinja2 templating.
- Clean and responsive HTML/CSS design.
- Modular structure for easy expansion of suppliers, inventory, orders, and deliveries.

---

## Project Structure

```
project/
â”‚
â”œâ”€â”€ app.py                # Main Flask application
â””â”€â”€ README.md             # Documentation (this file)
```

---

## How It Works

### 1. Flask Setup

```python
from flask import Flask, render_template_string
```

- We import Flask and `render_template_string` to serve HTML content directly from Python.

### 2. Data Definitions

```python
suppliers = [...]
inventory = [...]
orders = [...]
deliveries = [...]
```

- These are **Python dictionaries** representing each section of the dashboard. This simulates backend data (could later be replaced by database queries).

### 3. HTML Template

```python
html_template = """..."""
```

- A full HTML document embedded as a Python multiline string.
- Uses **Jinja2** templating syntax (`{{ variable }}` and `{% for %}` loops) to inject dynamic content.

### 4. Flask Route

```python
@app.route("/")
def dashboard():
    return render_template_string(
        html_template,
        suppliers=suppliers,
        inventory=inventory,
        orders=orders,
        deliveries=deliveries
    )
```

- Renders the HTML template and passes data dictionaries as context variables.

### 5. Running the App

```python
if __name__ == "__main__":
    app.run(debug=True)
```

- Starts a local web server with `debug=True` for development.

---

## HTML/CSS Highlights

- Structured into four main sections: **Suppliers**, **Inventory**, **Orders**, and **Deliveries**.
- Each section has a clean `table` with headers and dynamic rows.
- CSS provides a modern and professional look:
  - Light gray background
  - White card-style sections with shadows
  - Colorful headers for emphasis (`#3498db` blue)

---

## Key Concepts and Benefits

| Concept                     | Explanation                                                                 |
|----------------------------|-----------------------------------------------------------------------------|
| Flask Web Framework        | Serves as the backend for routing and templating                           |
| Jinja2 Templating          | Allows embedding dynamic data into HTML                                     |
| Separation of Concerns     | Data, logic, and presentation are well-organized                           |
| Scalability                | Easy to integrate with databases or REST APIs later                         |
| Lightweight UI             | Minimal dependencies and fast loading                                      |

---

## How to Run

1. **Install Flask** (if not already installed):
   ```bash
   pip install flask
   ```

2. **Run the Application**:
   ```bash
   python app.py
   ```

3. **Open Your Browser**:
   Navigate to `http://127.0.0.1:5000/`

---

