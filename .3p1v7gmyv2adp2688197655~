In this project, you will create a phonebook app that stores phone numbers and emails of your friends. The app should allow the user to add, modify, delete, show, and fetch phone numbers and emails from the phonebook.

The app should always print all the options available to the users, and after an action is finished, it should show all the options again. Here are the options that should be available and their details.

1. `new contact`: This option creates a new contact info. When chosen, it asks the user to enter the following:
    * Name of contact.
    * Phone Number of Contact
    * Email of Contact.

    If the entered name of contact, already exists, then the program should ask the user if they want to overwrite the already existing information.

2. `delete contact`: This option asks the user for the name of the contact to be deleted. If the name exists, the information about the contact is deleted. If the name does not exist in the phonebook, the program should tell the user that the desired number does not exist.

3. `modify phone number`: This option asks for the name of the contact which they want to modify their phone number, and asks the user to enter the new phone number to overwrite the old one. If given name does not exist, signal this to user and abort the operation.

4. `modify email`: This option asks for the name of the contact which they want to modify their email, and asks the user for the new email to overwrite the old one. If given name does not exist, signal this to the user and abort the operation

5. `show contacts`: This option prints all contacts, one contact per line in the following format:
    ```
    Erwin Smith, 09104200013, esmith@gmail.com
    Historia Reis, 05139343333, hreis@gmail.com
    ...
    ```
6. `quit`: Exits and closes the program, but before closing it saves the contacts in `.txt` file in the same format in the `show contacts` command.

You must use function in this project, such that each functionality is encapsulated in its own function. So you need to implement the following functions:   
1. `run_program`: This is the main function that runs the program loop and it is called only once to start the program.   
2. `show_options`: shows the user the options and reads the input which represents the users chosen option.   
3. `create_new_contact`: creates or overwrites a new contact.    
4. `delete_contact`: deletes an entry from the phone book.  
5. `modify_phone_number`: modifies a phone number of a particular name in the phonebook.   
6. `modify_email`: modifies the email of a particular name in the phonebook.     
7. `show_contacts`: prints contacts to the console.   
8. `save_phonebook`: saves the contents of the phonebook into a `.txt` file.


**Hints**:
* The phonebook needs to represented by some data structure, what do you think we can use. We might need to use more than one.
* The phonebook should be modified from different functions, what is the best way to make the phonebook accessible and modifiable from different function ? There are several ways.

## Bonus
* when using the `show contacts` option, can you make so that the contacts are sorted by alphabetical order
* When the program asks the user to enter a phone number and an email, the user might enter something that is not numerical for the phone number, like text or symbols, or something which is not a valid email. Can you handle this case by checking if the phone number is numerical and if the email is valid ? An email is valid if it has the following format:
    ```
    [lower_case_alphabets or number or symbols: .-]@gmail.com
    ```
