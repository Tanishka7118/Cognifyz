def valid_email(email):
    if email.count('@') != 1:        # Check if there is  "@" symbol or not
        return False
    local_part, domain_part = email.split('@')       # Split the email into local part and domain part
    if not local_part or '.' not in domain_part:         # Check if local part is not empty and domain part contains a dot
        return False
    domain_name, *rest = domain_part.split('.')           # Check if the domain part has at least one character before and after the dot
    if not domain_name or not rest:
        return False
    
    return True
email = input("Enter an email address: ")
if valid_email(email):
    print("The email address is valid.")
else:
    print("The email address is invalid.")
