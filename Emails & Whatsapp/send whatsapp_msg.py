import pywhatkit

# Send message to a contact
phone_number = input("Enter phone number: ")

pywhatkit.sendwhatmsg(phone_number, "message", 6, 40)
# numbers represnt hour, minute


# Send message to a group
group_id = input("Enter group id: ")

pywhatkit.sendwhatmsg_to_group(group_id, "message", 4, 31)
