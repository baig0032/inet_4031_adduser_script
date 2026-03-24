#!/usr/bin/python3
# INET4031
# Mirza Baig

# create-users2.py
# This script adds multiple users and assigns them to groups.
# It can run in "dry-run" mode, where commands are printed instead of executed.
# Dry-run is useful for testing without modifying the system.

import os
import re

def main():
    # Prompt the user to select dry-run mode
    # Dry-run (Y) means no users/groups will be created; commands will just be printed
    # Normal mode (N) executes all system commands
    dry_run_input = input("Run in dry-run mode? (Y/N): ").strip().upper()
    dry_run = dry_run_input == "Y"

    # Prompt the user to enter the input filename
    input_file = input("Enter input filename: ").strip()

    try:
        # Open the input file for reading
        with open(input_file, "r") as f:
            for line in f:
                line = line.strip()

                # Skip empty lines
                if not line:
                    continue

                # Skip lines starting with '#' (comment lines)
                match = re.match("^#", line)

                # Split each line into fields using colon ':' as delimiter
                fields = line.split(":")

                # If line is a comment or does not have exactly 5 fields, skip it
                if match or len(fields) != 5:
                    if dry_run:
                        if match:
                            print(f"Skipping line: {line} (marked to skip)")
                        else:
                            print(f"Error: line does not have enough fields: {line}")
                    continue

                username = fields[0]

                # Stop processing after user08; ignore any lines after this
                if username > "user08":
                    break

                password = fields[1]
                gecos = f"{fields[3]} {fields[2]},,,"
                groups = fields[4].split(",")

                # --- Create user ---
                print(f"==> Creating account for {username}...")
                cmd = f"/usr/sbin/adduser --disabled-password --gecos '{gecos}' {username}"
                if dry_run:
                    # In dry-run mode, just print the command
                    print(f"Would run: {cmd}")
                else:
                    # In normal mode, execute the system command
                    os.system(cmd)

                # --- Set user password ---
                print(f"==> Setting the password for {username}...")
                cmd = f"/bin/echo -ne '{password}\n{password}' | /usr/bin/sudo /usr/bin/passwd {username}"
                if dry_run:
                    print(f"Would run: {cmd}")
                else:
                    os.system(cmd)

                # --- Assign groups ---
                for group in groups:
                    if group != "-":
                        print(f"==> Assigning {username} to the {group} group...")
                        cmd = f"/usr/sbin/adduser {username} {group}"
                        if dry_run:
                            print(f"Would run: {cmd}")
                        else:
                            os.system(cmd)

    except FileNotFoundError:
        # If the input file does not exist, print an error
        print(f"Error: Input file '{input_file}' not found.")
        return

if __name__ == "__main__":
    main()
