# FindPasswords
FindPasswords is a simple tool designed for educational purposes that aims to find passwords by monitoring the usage of the "@" symbol. Please note that it should only be used for educational purposes and with proper authorization.

# Setup
To set up FindPasswords, follow these steps:

Clone the repository or download all the files and place them in the same folder.
Run the "keytrack img.pyw" script. This script will record every character you type and take a screenshot whenever the "@" symbol is pressed.
To search for passwords, run the "look 4 @.py" script.

# How it works
FindPasswords operates by monitoring keystrokes and capturing screenshots. Here's an overview of how it works:

The "keytrack img.pyw" script records every character you type.
Whenever the "@" symbol is pressed, a screenshot is taken to capture the context in which the symbol was used.
The password finder, implemented in the "look 4 @.py" script, searches for instances of "@" in the recorded text.
Once a match is found, the script retrieves the 30 characters typed before the "@" symbol and the following 50 characters.
With this information, it is assumed that the password can be determined.

Please keep in mind that FindPasswords is a simple demonstration and should not be used for any unauthorized activities.
