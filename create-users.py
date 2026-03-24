#!/usr/bin/python3

# INET4031
# Mirza Baig

# Importing required modules:
# os - to run system commands
# re - for regular expression matching
# sys - to read input from stdin
import os
import re
import sys

def main():
    # Read each line from the input file
    for line in sys.stdin:

        # Check if the line starts with "#" (a comment)
        # Lines starting with "#" are skipped because they are not user entries
        match = re.match("^#", line)

        # Split the line into fields using ":" as delimiter

        # Each line should contain: username:password:last:first:groups
        fields = line.strip().split(':')

        # Skip the line if it is a comment or if it does not have exactly 5 fields
        # This prevents processing invalid lines
        if match or len(fields) != 5:
            continue

        # Extract user information from the fields
        username = fields[0]                  # system username
        password = fields[1]                  # user password
        gecos = "%s %s,,," % (fields[3],fields[2])  # full name in "First Last" format, used by adduser

        # Split the groups field into a list of groups
        # A user may belong to multiple groups separated by commas
        groups = fields[4].split(',')

        # Dry-run print: indicate that we are creating an account
        print("==> Creating account for %s..." % (username))

        # Command to add the user account without setting a password yet
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos, username)
        # Dry run: print the command instead of executing it
        #print(cmd)
        os.system(cmd)

        # Dry-run print: indicate that we are setting the password
        print("==> Setting the password for %s..." % (username))

        # Command to set the password for the user
        # This uses echo and pipe to feed the password to the passwd command
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password, password, username)
        # Dry run: print the command instead of executing it
        #print(cmd)
        os.system(cmd)

        # Assign the user to each group listed
        for group in groups:
            # Skip group assignment if the group field is "-" (indicating no group)
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username, group))
                cmd = "/usr/sbin/adduser %s %s" % (username, group)
                # Dry run: print the command instead of executing it
                #print(cmd)
                os.system(cmd)

if __name__ == '__main__':
    main()
