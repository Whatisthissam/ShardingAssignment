# Day 3-4: Starter Code

class Message:
    def __init__(self, user_id, channel_id, content):
        self.user_id = user_id
        self.channel_id = channel_id
        self.content = content


class ChatServer:
    def __init__(self):
        self.messages = []

    def send_message(self, message):
        self.messages.append(message)

    def stats(self):
        print("Total messages:", len(self.messages))


server = ChatServer()

for _ in range(10):  # _ convention means: “I dont care about this variable” 
    server.send_message(Message(1, 1, "hello"))

server.stats()

for _ in range(10000):
    server.send_message(Message(1, 1, "hello"))

server.stats()