# Import from both the python script for both the classes
from loginpage import QApplication, loginPage, sys
from registration_form import RegistrationForm

# Main Method to structure, order, and execute the different python classes in different python scripts
if __name__ == '__main__':

    #Start the APP
    app = QApplication(sys.argv)
    
    # Create an instance of the LoginPage
    login_page = loginPage()
    login_page.show()

    # Create an instance of the RegistrationForm
    registration_form = RegistrationForm()  
    
    #ByeBye APP
    sys.exit(app.exec_())

 