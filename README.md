### This Python script is a simulation for cracking a password using timing attacks.
It demonstrates how a password can be guessed by analyzing the time it takes to validate different password attempts.

<img src="https://github.com/Triksheim/Timing-attack-bruteforce-cracker/assets/59808763/aaa3ac53-b5f9-4199-977b-9159a378bcbc" >
<img src="https://github.com/Triksheim/Timing-attack-bruteforce-cracker/assets/59808763/c15cc371-2a3f-4123-88ae-35836aa25755" width="800, height=400" >

#### This method will only work for on edge cases in very unsecure systems where:
  - passwords are stored in plaintext / not hashed
  - no attempt limit on pw validation
  - pw validation function without random time delays


.
.
.



Server Class

    Purpose: Simulates a server that holds and checks passwords.
    Methods:
        __init__(self, password): Constructor that initializes the server with a password.
        check_password(self, pw): Checks if the provided password pw matches the stored password. Returns True if it matches, False otherwise.

Cracker Class

    Purpose: Attempts to crack the password stored on the Server.
    Methods:
        __init__(self, max_length, allowed_chars, check_pw_function): Constructor that initializes the Cracker with the maximum password length, allowed characters, and the password checking function from the Server.
        random_str(self, size): Generates a random string of a given size from the allowed characters.
        find_pw_length(self): Determines the likely length of the password by measuring the time taken for password checks of different lengths.
        crack_password(self): Attempts to crack the password by timing attacks on the check password function.

Usage

    Define ALLOWED_CHARS with the characters you want to include in the password guesses.
    Initialize a Server instance with the password you want to crack.
    Create a Cracker instance, specifying the maximum password length, allowed characters, and the server's password check function.
    Run the script to see the guessed password length and then crack the password.
