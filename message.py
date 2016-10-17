import time

class Message:
    def __init__(self, author, time, text):
        self.author = author
        self.time = time
        self.text = text

def read_message(info_node, text_node):
    author = info_node.find("span", class_="user").get_text().strip()
    msg_time_raw = info_node.find("span", class_="meta").get_text().strip()
    msg_time = time.strptime(msg_time_raw, "%A, %B %d, %Y at %I:%M%p %Z")
    text = text_node.get_text().strip()

    return Message(author, msg_time, text)
