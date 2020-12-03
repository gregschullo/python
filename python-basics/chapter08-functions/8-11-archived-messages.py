messages = ['sup', 'yo', 'hey', 'howdy']
sent_messages = []

def send_message(message):
    """this function takes a list of messages, displays them, and moves them to a new list"""
    while message:
        current_message = message.pop()
        print(current_message)
        sent_messages.append(current_message)

send_message(messages[:])

print(messages)
print(sent_messages)
