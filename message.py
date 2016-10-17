from datetime import datetime

class Message:
    def __init__(self, author, time, text):
        self.author = author
        self.time = time
        self.text = text

def read_message(info_node, text_node):
    author = info_node.find("span", class_="user").get_text().strip()
    time_raw = info_node.find("span", class_="meta").get_text().strip()
    time = datetime.strptime(time_raw, "%A, %B %d, %Y at %I:%M%p %Z")
    text = text_node.get_text().strip()

    return Message(author, time, text)
