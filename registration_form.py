import sys
import mysql.connector
from PyQt5.QtWidgets import QApplication, QPushButton, QLabel, QLineEdit, QGridLayout, QDialog

class RegistrationForm(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Registration')
        self.resize(400, 200)
        self.setStyleSheet("background-color: #B22222;")

        layout = QGridLayout()

        label_name = QLabel('<font size="4" color="white">Username:</font>')
        self.lineEdit_username = QLineEdit()
        layout.addWidget(label_name, 0, 0)
        layout.addWidget(self.lineEdit_username, 0, 1)

        label_email = QLabel('<font size="4" color="white">Email:</font>')
        self.lineEdit_email = QLineEdit()
        layout.addWidget(label_email, 1, 0)
        layout.addWidget(self.lineEdit_email, 1, 1)

        label_password = QLabel('<font size="4" color="white">Password:</font>')
        self.lineEdit_password = QLineEdit()
        layout.addWidget(label_password, 2, 0)
        layout.addWidget(self.lineEdit_password, 2, 1)

        button_register = QPushButton('Register')
        button_register.clicked.connect(self.register_user)
        layout.addWidget(button_register, 3, 0, 1, 2)

        self.setLayout(layout)

    def register_user(self):
        # Retrieve user input from the registration form
        username = self.lineEdit_username.text()
        email = self.lineEdit_email.text()
        password = self.lineEdit_password.text()

        # Establishing a connection to the MySQL database
        db_config = {
            'host': 'localhost',          # Host where MySQL is running
            'user': 'root',               # Your MySQL username
            'password': 'Qwerty@123',     # Your MySQL password
            'database': 'user_registration',  # The name of your database
        }

        try:
            connection = mysql.connector.connect(**db_config)
            cursor = connection.cursor()

            # Insert the user data into the MySQL database
            insert_query = "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)"
            cursor.execute(insert_query, (username, email, password))

            # Commit the changes to the database
            connection.commit()

            print("Registration successful!")

        except mysql.connector.Error as e:
            # Handle database errors, e.g., duplicate username
            print(f"Error: {e}")
            print("Registration failed. Please try again.")

        finally:
            # Close the cursor and the database connection
            cursor.close()
            connection.close()


        # Close the registration form after successful registration
        self.accept()
