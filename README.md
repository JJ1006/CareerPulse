# CareerPulse: Layoff Risk Assessment Platform

Empowering professionals through data-driven layoff risk assessment.

---

## Overview

**CareerPulse** is a Django-based platform that evaluates layoff risk for professionals using machine learning. It calculates a layoff probability based on input parameters like job satisfaction, performance ratings, and career progression, offering personalized recommendations to mitigate career risks.

---

## Features

### **User Side**
1. **Layoff Risk Prediction**:
   - Users submit details like age, job role, years of experience, and satisfaction levels.
   - A pre-trained Random Forest model calculates the layoff risk score.
   - Personalized career advice is provided.

2. **API Fetching**:
   - Real-time news layoff data is fetched and displayed dynamically on the home page and after login.

3. **Interactive Interface**:
   - Clean and responsive frontend with user-friendly forms.
   - Results presented in an easy-to-understand format.

4. **Real-Time Insights**:
   - Instant feedback on layoff probability and actionable suggestions.

### **Admin Side**
1. **User Data Management**:
   - View, search, and filter user submissions via the Django Admin Panel.

2. **Dashboard**:
   - Secure admin dashboard for managing submissions.

---

## Project Components

### **Backend**
- **Framework**: Django
- **Database**: SQLite
- **Machine Learning**: Pre-trained Random Forest model using `scikit-learn`.
- **Environment Management**: Virtual environment with dependencies.

### **Frontend**
- **HTML/CSS/JavaScript**: Interactive and responsive design.
- **API Integration**: Real-time data display.
- **Responsive Design**: Optimized for all devices.

### **Workflow Automation**
- **Kestra Integration**:
  - Automates deployment processes.
  - Tasks:
    1. Apply database migrations.
    2. Update ALLOWED_HOSTS dynamically.
    3. Start Django development server.

---

## Project Structure
````markdown
careerpulse/
├── requirements.txt
├── run_django.yml
├── db.sqlite3
├── manage.py
├── server.log
├── careerpulse/
│   ├── user_management/
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   │   ├── __init__.py
│   ├── users/
│   │   ├── signals.py
│   │   ├── models.py
│   │   ├── forms.py
│   │   ├── admin.py
│   │   ├── urls.py
│   │   ├── views.py
│   │   ├── templates/
│   │   │   ├── base.html
│   │   │   ├── profile.html
│   │   │   ├── home.html
│   │   │   ├── register.html
│   │   │   ├── login.html
│   │   ├── migrations/
│   │   │   ├── 0001_initial.py
│   │   ├── layoff_prediction_model/
│   │   │   ├── scaler.pkl
│   │   │   ├── RF_MODEL.pkl
│   │   │   ├── model_training.ipynb
│   │   │   ├── predict.py
│   │   └── __init__.py
│   └── media/
│       ├── profile_images/
└── __init__.py
````

* * *

Workflow Automation with Kestra
-------------------------------

### **Kestra Workflow Tasks**

1.  **Apply Migrations**:
    *   Updates database structure.
2.  **Update Allowed Hosts**:
    *   Dynamically updates ALLOWED\_HOSTS in Django settings.
3.  **Start Server**:
    *   Starts Django development server and verifies accessibility.
4.  **Log Server Status**:
    *   Logs server readiness.

* * *

Machine Learning Workflow
-------------------------

### **Model Pipeline**

1.  **Random Forest Model**:
    
    *   Trained on workforce data considering job satisfaction, performance ratings, etc.
    *   Outputs layoff risk score.
2.  **Feature Scaling and Selection**:
    
    *   Input data is scaled using `StandardScaler`.
    *   Recursive Feature Elimination (RFE) is applied.
3.  **Personalized Career Insights**:
    
    *   Tailored advice based on the layoff probability.

* * *

How to Run the Project
----------------------

### **Prerequisites**

*   Python 3.8+
*   Kestra
*   Bash shell
*   Internet connection

### **Steps**

1.  Clone the Repository:
    
    ```bash
    git clone https://github.com/JJ1006/CareerPulse.git
    cd CareerPulse
    ```
    
2.  Start the Kestra Workflow:
    
    ```bash
    kestra workflow start --namespace my.django --id django-project-workflow
    ```
    
3.  Access the Platform:
    
    *   [http://localhost:8000](http://localhost:8000) for local development.
    *   [http://0.0.0.0:8000](http://0.0.0.0:8000) for public access.

* * *

Best Practices Followed
-----------------------

1.  **Scalable Architecture**:
    *   Separation of backend, ML, and frontend.
2.  **User-Centric Design**:
    *   Intuitive and visually appealing interface.
3.  **Optimized Admin Panel**:
    *   Secure and easy-to-use.
4.  **Code Quality**:
    *   Ensures readability, maintainability, and scalability.

* * *

Future Enhancements
-------------------

1.  Advanced Analytics:
    *   Add dashboards for visualizing workforce trends.
2.  Multi-Language Support:
    *   Expand for non-English-speaking users.
3.  Mobile App:
    *   Develop a mobile version.
4.  API Integration:
    *   Provide APIs for business integration.

* * *

Conclusion
----------

**CareerPulse** empowers individuals and organizations with actionable layoff risk insights. By leveraging machine learning and automation, it offers a seamless, user-friendly experience for career management.
