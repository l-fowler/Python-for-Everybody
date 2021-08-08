"""
Exercise 5: This program records the domain name (instead of the address) where the
message was sent from instead of who the mail came from (i.e., the whole email address).
At the end of the program, print out the contents of your dictionary.

You can download the file from:
https://www.py4e.com/code3/mbox-short.txt
"""

domains = {} # Dictionary

fhand = input("Enter file: ")
try:
    file = open(fhand)
except:
    print("Invalid file")
    quit()

for line in file:
    words = line.split()
    # Ignore empty lines and lines that don't start with 'From'
    if len(words) == 0 or words[0] != 'From':
        continue
    else:
        email = words[1]
        # print(email)
        email_domain = email.split('@')
        # print(email_domain)
        domain = email_domain[1]
        # print(domain)
        # Make domain = 1 if not in {}, else +1
        if domain not in domains:
            domains[domain] = 1
        elif domain in domains:
            domains[domain] += 1
print(domains)
