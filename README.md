**Vendor Management System with Performance Metrics**

---

This project is a Vendor Management System developed using Django and Django REST Framework. It facilitates the management of vendor profiles, tracks purchase orders, and calculates vendor performance metrics.

*Note: This project was completed as an assignment. Please refrain from copying if you encounter a similar assignment.*

---

### How to Run

1. **Setup Environment**:
   - Ensure you have Python3 installed .
```console
$ # create virtual environment 

$ python3 -m venv <name of your virtual environment>[.env] # in my case 

$ # activate virtual environment 
$ .env/bin/activate
```

2. **Install Dependencies**:
   - Once the requirements.txt file is available, install the required libraries using pip:
     ```console 
     $ pip install -r requirements.txt
     ```

3. **Run Server**:
   - Navigate to the project directory.
   - Run the Django development server:
     ```console
     $ python manage.py makemigrations 
     $ python manage.py migrate 
     $ python manage.py runserver
     ```

4. **Test Endpoints**:
   - Access the application at http://localhost:8000/.
   - Use the provided endpoints to manage vendor profiles and track purchase orders.
   - Test the functionality of each endpoint to ensure proper operation.
---

Thank you for reviewing the project! If you have any questions or feedback, feel free to reach out.