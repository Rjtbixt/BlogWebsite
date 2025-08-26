Create a virtual environment:
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

Install dependencies:
pip install -r requirements.txt

Create a .env file in the project root:
MY_EMAIL=your_email@gmail.com
MY_EMAIL_PASSWORD=your_app_password
TO_EMAIL=recipient_email@gmail.com

Run the Flask app

