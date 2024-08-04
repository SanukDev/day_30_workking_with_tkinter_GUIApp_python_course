Password Manager

This is a simple Password Manager application built with Python and Tkinter. It allows users to generate, save, and retrieve passwords securely. The application uses JSON for data storage.

Features

Password Generation: Generate random, secure passwords.
Save Passwords: Save website, username, and password information securely.
Search Functionality: Search for saved credentials by website.

Code Overview

Password Generation
The random_password function generates a random password using a combination of letters, numbers, and symbols. The password is then displayed in the password input field and copied to the clipboard using pyperclip.

Search Data
The search function allows users to search for saved credentials by website. It reads the data from the data.json file and displays the username and password for the specified website.

Save Password
The save function saves the website, username, and password information to a JSON file (data.json). If the file does not exist, it creates a new one. If it does exist, it updates the file with the new credentials.

Try-Except Structure in save Function:

The function attempts to open and read the data.json file. If the file does not exist, an exception is caught, and a new file is created with the new credentials.
If the file exists, it updates the data with the new credentials and saves it back to the file.

UI Setup
The UI is built using Tkinter and includes labels, input fields, and buttons for interacting with the application. The UI layout is defined in the UI SETUP section of the code.
