# inet_4031_adduser_script

Program Description:
This program automates the process of adding multiple user accounts to a Linux system from a single input file. Without this script, a system administrator would need to manually run several commands for each user: useradd to create the account, chpasswd to set the password, and usermod to assign the user to any required groups. On a server with dozens or hundreds of accounts to create, doing this by hand is slow and error-prone. This script reads a structured input file and runs those exact same commands — useradd, chpasswd, and usermod — automatically for every user in the list, completing in seconds what could otherwise take an hour of repetitive manual work.



Program User Operation: 
To use this program, you provide a properly formatted input file containing one user per line. The script reads that file and processes each entry, either executing the system commands to create the users or printing what would be run in dry run mode. Before running the script, make sure your input file is ready and the script has executable permissions set.



Input File Format: 
The input file contains one user per line, with each line holding five fields separated by colons. Those fields, in order from left to right, are the username, password, last name, first name, and a comma-separated list of groups the user should belong to. If you want the script to skip a line entirely — for example, a user that should not be added to this particular server — place a # character at the very beginning of that line and the script will ignore it. If a user does not need to be added to any groups, place a - in the groups field rather than leaving it blank.



Command Execution :
Before running the script for the first time, you may need to grant it executable permissions by running chmod +x create-users.py. Once that is done, execute the script by redirecting your input file into it with the following command: sudo ./create-users.py < create-users.input. The < symbol is an input redirection operator that feeds the contents of create-users.input into the script as standard input, so the script processes each line of the file as though it were being typed directly at the keyboard.

Dry Run :
Before creating any real accounts on the system, it is strongly recommended to perform a dry run first. To do this, comment out the three system command lines in the script — the useradd, chpasswd, and usermod calls — so that no actual changes are made to the server. The script will still process every line of the input file and print out exactly which commands would have been executed, allowing you to verify that everything looks correct before making any real modifications. Once you have confirmed the dry run output is accurate, uncomment those three lines and run the script again with sudo to create the accounts for real.
