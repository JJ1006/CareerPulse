# **CareerPulse: Layoff Risk Assessment Platform**

Empowering professionals through data-driven layoff risk assessment.

---

## **Overview**

**CareerPulse** is a comprehensive Django-based platform that evaluates layoff risks for professionals using advanced machine learning. It provides actionable insights and personalized recommendations to help users mitigate potential career risks. With seamless workflow automation powered by Kestra and an intuitive user interface, CareerPulse combines cutting-edge technology with user-centric design.

---

## **Key Features**

### **User Side**
1. **Layoff Risk Prediction:**
   - Submit information such as age, job role, years of experience, and job satisfaction levels.
   - Analyze layoff probability using a pre-trained Random Forest model.
   - Receive detailed, personalized recommendations to enhance career stability.

2. **API Integration:**
   - Displays live, dynamically fetched news related to layoffs and career trends on the homepage and user dashboard.

3. **Interactive Interface:**
   - Offers a clean, responsive design optimized for all devices.
   - Provides an intuitive experience for data submission and results interpretation.

4. **Secure Authentication:**
   - Features include sign-up, login, and password reset functionalities to ensure data privacy and security.

5. **Real-Time Insights:**
   - Offers instant layoff probability feedback and actionable career advice.

### **Admin Side**
1. **Data Management:**
   - View, search, and filter all user submissions through the Django Admin Panel.
   - Monitor layoff probability scores and provided recommendations for transparency.

2. **Admin Dashboard:**
   - Manage user data securely via a well-designed dashboard.
   - Export user data for advanced analytics or reporting.

---

## **Tech Stack**

- **Backend Framework:** Django
- **Database:** SQLite for development; PostgreSQL ready for production
- **Machine Learning:** Random Forest model with `scikit-learn`, integrated with feature scaling and selection
- **Workflow Automation:** Kestra for seamless deployment and orchestration
- **Frontend:** HTML, CSS, JavaScript with responsive design and live API integration

---

## **Workflow Automation with Kestra**

### **Kestra Workflow Tasks**
1. **Apply Migrations:**
   - Ensures the database structure is always up-to-date.
2. **Update Allowed Hosts:**
   - Dynamically configures the Django settings to allow multi-host access.
3. **Run Development Server:**
   - Starts the Django server, validates availability, and logs server readiness.
4. **Log Server Status:**
   - Ensures error-free operation by logging server activities.

---

## **Project Structure**

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


## **Machine Learning Workflow**

1. **Data Processing:**
   - Categorical variables are encoded, and numeric features are scaled using `StandardScaler`.
   - Recursive Feature Elimination (RFE) identifies key features.

2. **Model Training:**
   - A Random Forest model is trained on curated workforce data.
   - Generates a layoff risk score based on factors like job satisfaction, performance rating, and experience.

3. **Prediction:**
   - The model predicts layoff probability for user inputs.
   - Recommendations are generated based on feature importance to guide career improvement.

---

## **How to Run the Project**

### **Prerequisites**
- Python 3.8+
- Kestra installed and configured
- Bash shell for running scripts

### **Steps**
1. Clone the repository:
   ```bash
   git clone https://github.com/JJ1006/CareerPulse.git
   cd CareerPulse
   ```

2.  Start the Kestra workflow:
    
    ```bash
    kestra workflow start --namespace my.django --id django-project-workflow
    ```
    
3.  Access the platform:
    *   [http://localhost:8000](http://localhost:8000) for local access.
    *   [http://0.0.0.0:8000](http://0.0.0.0:8000) for public access.

* * *

**Future Enhancements**
-----------------------

1.  **Advanced Analytics:**
    *   Develop dashboards for workforce trend visualizations and predictive analytics.
2.  **Mobile Application:**
    *   Expand CareerPulse for mobile platforms to ensure on-the-go accessibility.
3.  **Language Support:**
    *   Add support for non-English users to expand the global reach.
4.  **API Integration:**
    *   Provide APIs for organizations to integrate layoff predictions with HR tools.

* * *

**Conclusion**
--------------

**CareerPulse** empowers individuals and organizations by combining machine learning, workflow automation, and intuitive design to mitigate layoff risks effectively. Its scalable architecture and actionable insights make it an indispensable career management tool.

Empower your career with **CareerPulse**—where data meets opportunity!
