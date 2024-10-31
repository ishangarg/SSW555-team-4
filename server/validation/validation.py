import phonenumbers
from phonenumbers import NumberParseException
from datetime import datetime

def validate_conversations(data):
    err = []
    if not isinstance(data, dict):
        err.append("The data is not of type 'object'")
        return err
    if "user_id" not in data:
        err.append("'user_id' must be present")
    elif not isinstance(data.get("user_id"), str):
        err.append("'user_id' must be a string")
    if "messages" not in data:
       err.append("'messages' must be present")
    elif not isinstance(data.get("messages"), list):
        err.append("'messages' must be a list")
    else:
        for i, message in enumerate(data["messages"]):
            if not isinstance(message, dict):
                err.append(f"messages[{i}] is not of type 'object'")
            # if "timestamp" not in message:
            #     err.append(f"'timestamp' must be present in messages[{i}]")
            # elif not isinstance(message.get("timestamp"), str):
            #     err.append(f"messages[{i}].timestamp must be a string")
            # elif not validate_timestamp(message.get("timestamp")):
            #     err.append(f"messages[{i}].timestamp is not valid")
            if "query" not in message:
                err.append(f"'query' must be present in messages[{i}]")
            elif not isinstance(message.get("query"), str):
                err.append(f"messages[{i}].query must be a string")
            if "response" not in message:
                err.append(f"'response' must be present in messages[{i}]")
            elif not isinstance(message.get("response"), str):
                err.append(f"messages[{i}].response must be a string")
    return err

def validate_timestamp(timestamp):
    try:
        valid_timestamp = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
        return True
    except ValueError:
        return False
    
def validate_contact(data):
    err = []
    print(data)
    if not isinstance(data, dict):
        err.append("The data is not of type 'object'")
        return err
    if "user_id" not in data:
        err.append("'user_id' must be present")
    elif not isinstance(data.get("user_id"), str):
        err.append("'user_id' must be a string")
    if "contacts" not in data:
       err.append("'contacts' must be present")
    elif not isinstance(data.get("contacts"), list):
        err.append("'contacts' must be a list")
    if err:
        return err
    else: 
        for i, contact in enumerate(data["contacts"]):
            if "contact_name" not in contact:
                err.append("'contact_name' must be present")
            elif not isinstance(contact.get("contact_name"), str):
                err.append("'contact_name' must be a string")
            elif "phone_number" not in contact:
                err.append("'phone_number' must be present")
            elif not isinstance(contact.get("phone_number"), str):
                err.append("'phone_number' must be a string")
            else:
                parsed_number = phonenumbers.parse(contact.get("phone_number"), "US")
                print(parsed_number)
                if phonenumbers.is_valid_number(parsed_number) == False:
                    err.append(f"The 'phone_number': {contact.get("phone_number")} is invalid")
                else:
                    contact["phone_number"] = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)
                    contact["contact_name"] = contact["contact_name"].strip()
            return err
    return err
        
    
        