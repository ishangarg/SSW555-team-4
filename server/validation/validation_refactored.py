from datetime import datetime
import phonenumbers

'''
This is the refactored file with 2 user stories:

1) Error handling for unknown input
2) Emergency contact validation

The code is easier to read and has removed unncessary print statements and comments.

The toold used for refactoring was PyLint, and the two smells were:

a) Unused variables
b) Unreachable code
c) Commented codes

pylint validation_refactored.py
Testing result Screenshot: test_after_refactor.png

'''

def validate_conversations(data):
    errors = []
    
    def add_error(message):
        errors.append(message)
    
    if not isinstance(data, dict):
        add_error("The data is not of type 'object'")
        return errors
    
    user_id = data.get("user_id")
    messages = data.get("messages")

    if user_id is None and not isinstance(user_id, str):
        add_error("'user_id' must be present")
        return errors
    
    if messages is None and not isinstance(messages, list):
        add_error("'messages' must be present")
        return errors
        
    for i, message in enumerate(messages):
        if not isinstance(message, dict):
            add_error(f"messages[{i}] is not of type 'object'")
            continue  
        
        query = message.get("query")
        response = message.get("response")
        
        if query is None and not isinstance(query, str):
            add_error(f"'query' must be present in messages[{i}]")
            continue
        
        if response is None and not isinstance(query, str):
            add_error(f"'response' must be present in messages[{i}]")
            continue
    
    return errors

def validate_timestamp(timestamp):
    try:
        valid_timestamp = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
        return True
    except ValueError:
        return False
    
def validate_contact(data):
    err = []
    if not isinstance(data, dict):
        err.append("The data is not of type 'object'")
        return err
    if "user_id" not in data and not isinstance(data.get("user_id"), str):
        err.append("'user_id' must be present")

    if "contacts" not in data and not isinstance(data.get("contacts"), list):
       err.append("'contacts' must be present")

    if err:
        return err
    
    for contact in data["contacts"]:
        if "contact_name" not in contact and not isinstance(contact.get("contact_name"), str):
            err.append("'contact_name' must be present")
            continue

        if "phone_number" not in contact and not isinstance(contact.get("phone_number"), str):
            err.append("'phone_number' must be present")
            continue


        parsed_number = phonenumbers.parse(contact.get("phone_number"), "US")
        
        if not phonenumbers.is_valid_number(parsed_number):
            err.append(f"The 'phone_number': {contact.get('phone_number')} is invalid")
            continue

        contact["phone_number"] = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)
        contact["contact_name"] = contact["contact_name"].strip()
        
    return err