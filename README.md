* * *

*Team Name - CodeChase Kohli*
======================================

* * *

*CareerPulse - Hackathon Submission*
======================================

* * *

*Tagline:* - *Empowering Professionals Through Data-Driven Layoff Risk Assessment*

* * *

*Overview*
------------

*CareerPulse* is a Django-based platform that evaluates the layoff risk for professionals by leveraging machine learning. It calculates a layoff probability based on several input parameters like job satisfaction, performance ratings, and career progression. CareerPulse offers personalized recommendations to users, helping them mitigate career risks and improve job security.

The backend integrates with *Kestra*, an orchestration tool, to automate workflows such as applying migrations, updating settings, and starting the server. The system is highly scalable, with a clear division between the backend (Django code), machine learning models, and frontend assets.

CareerPulse now includes a dynamic API fetching feature, which allows users to fetch and view real-time data both on the home page and after signing in. This provides a seamless and interactive user experience.

* * *

*Features*
------------

### *User Side:*

1.  *Layoff Risk Prediction*:
    
    *   Users submit a form containing details such as age, job role, years of experience, and satisfaction levels.
    *   The system uses a pre-trained Random Forest model to calculate the layoff risk score.
    *   Personalized career advice is generated based on user inputs to help mitigate the risk of layoffs.
2.  *API Fetching*:
    
    *   Real-time data is fetched from the backend and displayed dynamically on both the home page and after the user has signed in.
    *   This includes the latest predictions, layoff risks, and career advice for the user.
3.  *Interactive Interface*:
    
    *   The frontend is built with HTML, CSS, and JavaScript, ensuring a clean and responsive design.
    *   It provides users with an intuitive form for input and presents the results in an easy-to-understand manner.
4.  *Real-Time Insights*:
    
    *   The system provides instant feedback on layoff probability, as well as actionable suggestions to improve job security.

### *Admin Side:*

1.  *User Data Management*:
    
    *   Admins can access the *Django Admin Panel* to view all submitted user data, including layoff scores and their corresponding features.
    *   Data is well-organized for easy filtering and analysis.
2.  *Admin Dashboard*:
    
    *   A secure admin dashboard to manage and review user submissions.
    *   Features such as exporting user data in CSV format and filtering submissions by various parameters (e.g., job role, layoff probability) are provided.

* * *

*Project Components*
----------------------

### *Backend:*

*   *Framework*: Django
*   *Database*: SQLite (for simplicity and scalability during development)
*   *Machine Learning: Pre-trained **Random Forest* model using *scikit-learn*.
*   *Environment Management*: Virtual environment with necessary dependencies installed.

### *Frontend:*

*   *HTML/CSS/JavaScript*: User-friendly design for seamless interactions.
*   *API Integration*: The frontend dynamically fetches and displays data from APIs in real time for a more interactive user experience.
*   *Responsive Design*: Optimized for desktop, tablet, and mobile views.

### *Workflow Automation*:

*   *Kestra Integration*: Automates deployment processes, including database migrations, settings updates, and server startup.
*   *Tasks*:
    *   Apply database migrations.
    *   Update ALLOWED_HOSTS dynamically.
    *   Start Django development server and check server availability.

* * *

*Workflow Automation with Kestra*
-----------------------------------

### *Kestra Workflow Tasks:*

1.  *Apply Migrations*:
    
    *   Ensures that the database structure is up to date by applying necessary migrations.
2.  *Update Allowed Hosts*:
    
    *   Dynamically updates the ALLOWED_HOSTS in the Django settings to ensure the app can accept requests from various endpoints.
3.  *Start Server*:
    
    *   Starts the Django development server and verifies its accessibility.
4.  *Log Server Status*:
    
    *   Logs the server's readiness and ensures users can access the platform via http://localhost:8000 or http://0.0.0.0:8000.

* * *

*Machine Learning Workflow*
-----------------------------

### *Model Pipeline*

1.  *Random Forest Model*:
    
    *   The model was trained on workforce data, taking into account various features like job satisfaction, performance ratings, years at the company, etc.
    *   The model outputs a layoff risk score for each user based on the inputs provided.
2.  *Feature Scaling and Selection*:
    
    *   The input data is scaled using StandardScaler to normalize the feature set.
    *   *Recursive Feature Elimination (RFE)* is applied to identify the most important features that influence layoff probability, enhancing model performance.
3.  *Personalized Career Insights*:
    
    *   After predicting the layoff probability, the system provides tailored advice to each user, helping them improve job security.

* * *

*Admin Panel*
---------------

### *Admin Features:*

1.  *View User Submissions*:
    
    *   The Django Admin Panel allows admins to view all user submissions, including layoff scores, user data, and personalized advice.
2.  *Data Export*:
    
    *   Admins can export user data into CSV format for further analysis.
3.  *Search and Filter Submissions*:
    
    *   Admins can search and filter submissions by parameters like:
        *   Layoff risk score.
        *   Job role.
        *   Performance ratings.
4.  *Security*:
    
    *   Admin access is restricted to authorized personnel only.

* * *

*How to Run the Project*
--------------------------

### *Prerequisites:*

*   *Python 3.8+*
*   *Kestra* (for workflow automation)
*   *Bash shell* for running commands
*   *Internet connection* (to install dependencies)

### *Steps:*

1.  *Clone the Repository*:
    
    bash
    git clone https://github.com/JJ1006/CareerPulse.git
    cd CareerPulse
    
    
2.  *Start the Kestra Workflow*:
    
    bash
    kestra workflow start --namespace my.django --id django-project-workflow
    
    
3.  *Access the Platform*:
    
    *   Open your browser and navigate to:
        *   http://localhost:8000 (local development)
        *   http://0.0.0.0:8000 (for public access)

* * *

*Project Structure*
---------------------

graphql
CareerPulse/
│
├── user_management/              # Main Django project folder (user management app)
│   ├── __init__.py
│   ├── settings.py               # Django settings (database, app configs, etc.)
│   ├── urls.py                   # URL routing for the application
│   ├── wsgi.py                   # WSGI configuration for deployment
│   ├── asgi.py                   # ASGI configuration for real-time connections
│   └── admin.py                  # Admin configurations for user data management
│
├── users/                        # User-related Django files
│   ├── __init__.py
│   ├── models.py                 # Database models, including user data and layoff predictions
│   ├── forms.py                  # Django forms for collecting user data (e.g., layoff prediction form)
│   ├── views.py                  # Logic for handling user data, predictions, and displaying results
│   ├── urls.py                   # URL routing for the user app (user profile, results)
│   ├── admin.py                  # Admin configurations for managing user submissions
│   ├── templates/                # HTML templates for frontend
│   │   ├── home.html             # Layoff prediction form
│   │   ├── result.html           # Results page for layoff prediction
│   │   └── admin_dashboard.html  # Admin dashboard template for viewing user data
│   ├── static/                   # Static files like CSS, JS, and images
│   │   ├── css/
│   │   │   └── styles.css        # Custom styles for user interface
│   │   ├── js/
│   │   │   └── script.js         # JavaScript files (form validation, interactive UI)
│   
│   
│
├── layoff_prediction_model/      # Machine learning model and processing files
│   ├── RF_MODEL.pkl              # Pre-trained Random Forest Model
│   ├── scaler.pkl                # Scaler for feature scaling
│   ├── RFE.pkl                   # Recursive Feature Elimination file
│   ├── predict.py                # Python script to load models and make predictions
│   ├── data_processing.py        # Data pre-processing and feature engineering scripts
│   └── model_training.py         # Code for training the model (if re-training is needed)
│
├── workflow/                     # Kestra workflow files for deployment automation
│   ├── workflow.yaml             # Kestra workflow configuration (migrations, server start, etc.)
│
├── manage.py                     # Django project management script
├── requirements.txt              # Project dependencies
├── settings.py                    # Django configuration
├── server.log                     # Log file for server output and errors
└── docker-compose.yml            # Optional: Docker setup for local and production environments (if applicable)


* * *

### *Best Practices Followed*

1.  *Scalable Architecture*:
    
    *   The project is organized with clear separation between the backend (Django), machine learning components, and frontend assets.
2.  *User-Centric Design*:
    
    *   The user interface is intuitive, responsive, and visually appealing, ensuring a smooth experience.
3.  *Optimized Admin Panel*:
    
    *   Provides a secure and easy-to-use interface for admins to manage user submissions and data.
4.  *Code Quality*:
    
    *   The code follows best practices, ensuring readability, maintainability, and scalability.

* * *

### *Future Enhancements*

1.  *Advanced Analytics*:
    
    *   Add dashboards for visualizing workforce trends, layoff risks, and predictive analytics.
2.  *Multi-Language Support*:
    
    *   Expand the platform to support non-English-speaking users.
3.  *Mobile App*:
    
    *   Develop a mobile version of CareerPulse for on-the-go access.
4.  *API Integration*:
    
    *   Provide APIs for businesses to integrate the layoff predictions with their HR systems.

* * *

### *Conclusion*

*CareerPulse* is an innovative platform designed to empower individuals and organizations by providing actionable insights into layoff risks. By leveraging machine learning, the platform offers personalized career advice, helping professionals navigate their careers with confidence. The seamless integration with Kestra for automation and the user-friendly interface ensures a comprehensive and scalable solution for workforce management.
