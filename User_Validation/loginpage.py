import sys
import mysql.connector
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout, QMessageBox, QDialog
from registration_form import RegistrationForm


class loginPage(QWidget):

    def  __init__(self):

        super().__init__()

        self.setWindowTitle('Login Page')
        self.resize(500, 120)
        self.setStyleSheet("background-color: #FFAABB;")

        layout = QGridLayout()

        label_name = QLabel(' <font size = "4" color = "white"> Username : </font> ')
        self.lineEdit_username = QLineEdit()
        self.lineEdit_username.setPlaceholderText("Enter your UserName ")
        layout.addWidget(label_name, 0, 0)
        layout.addWidget(self.lineEdit_username, 0, 1)

        label_password = QLabel(' <font size = "4" color = "white"> Password : </font> ')
        self.lineEdit_password = QLineEdit()
        self.lineEdit_password.setPlaceholderText("Enter your Password ")
        layout.addWidget(label_password, 1, 0)
        layout.addWidget(self.lineEdit_password, 1, 1)

        button_login = QPushButton('Login')
        button_login.clicked.connect(self.validate_login)
        layout.addWidget(button_login, 2, 0, 1, 2)

        button_register = QPushButton('Register')  # Create the "Register" button
        button_register.clicked.connect(self.open_registration_page)  # Connect to a function for registration
        layout.addWidget(button_register, 3, 0, 1, 2)  # Add "Register" button to the layout

        layout.setRowMinimumHeight(2, 75)

        self.setLayout(layout)

    def open_registration_page(self):
        registration_form = RegistrationForm()
        result = registration_form.exec_()  # Show the registration form as a dialog

        # Check the result to see if registration was successful
        if result == QDialog.Accepted:
            QMessageBox.information(self, 'Registration', 'Registration successful!')


    def validate_login(self):

        username = self.lineEdit_username.text()
        password = self.lineEdit_password.text()
        
        #Database Configurations
        db_config = {
            'host' : 'localhost',
            'user' : 'root',
            'password' : 'Qwerty@123',
            'database' : 'user_registration'
        }

        try:
            #Using MySQL to connect to the DB that is created
            connection = mysql.connector.connect(**db_config)
            #Cursor is like navigator within the DB
            cursor = connection.cursor()
            #Execute does the SQL queries onto the DB
            cursor.execute("SELECT password FROM users WHERE username = %s", (username,))
            #It gets as tuple
            result = cursor.fetchone()

            if result:
                #Since we get one, we need the first part of it, hence result[0]
                stored_password = result[0]
                
                #Optional to just see the stored pass in DB and password entered
                print(f"Stored Password: {stored_password}")
                print(f"Entered Password: {password}")
                
                #Logical part to see if the username and password matches
                if password == stored_password:
                    QMessageBox.information(self, 'Login', "Login Successful!")
                else:
                    QMessageBox.warning(self, 'Login', 'Incorrect Password!')

            else:
                QMessageBox.warning(self, 'Login', 'Username not found!')
        
        #Incase if an error
        except mysql.connector.Error as e:
            print(f"Error: {e}")
            QMessageBox.critical(self, 'Error', 'Login failed. Please try again.')

        #Have to close both of these once their work is done
        finally:
            cursor.close()
            connection.close()

            



        

