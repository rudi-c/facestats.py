import re

from message import read_message

class MessageThread:
    def __init__(self, name, messages):
        self.name = name
        self.messages = sorted(messages, key=lambda msg: msg.time)

    def tally_messages(self):
        counts = {}
        for message in self.messages:
            # http://stackoverflow.com/questions/19410018/how-to-count-the-number-of-words-in-a-sentence
            words = len(re.findall(r'\w+', message.text))
            if message.author in counts:
                msg_count, word_count = counts[message.author]
                counts[message.author] = (msg_count + 1, word_count + words)
            else:
                counts[message.author] = (1, words)

        counts = { author: (msg_count, word_count, float(word_count) / msg_count)
                   for author, (msg_count, word_count)
                   in counts.iteritems() }
        return counts

def read_message_thread(full_name, thread_node):
    people = thread_node.find(text=True, recursive=False).strip().split(", ")
    if full_name in people:
        people.remove(full_name)
    else:
        # TODO: Handle case where people are shown as id@facebook.com
        # instead of their full name.
        # TODO: Handle other cases where the full name might be missing. If
        # people change their facebook names for example?
        return

    if len(people) == 0:
        # TODO: Can this happen?
        raise Error("Nobody but yourself is in this conversation!")
    elif len(people) > 1:
        # TODO: Handle group conversations
        return

    message_infos = thread_node.find_all("div", class_="message")
    message_texts = thread_node.find_all("p")

    if len(message_infos) != len(message_texts):
        raise Error("Number of message infos does not match messages?")

    messages = [read_message(info, text)
                for info, text
                in zip(message_infos, message_texts)]

    return MessageThread(people[0], messages)