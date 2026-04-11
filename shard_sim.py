#importing libraries
import random

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


# Day 5: Introducing Shards

class Shard:
    def __init__(self, shard_id):
        self.id = shard_id
        self.messages = []

    def store(self, message):
        self.messages.append(message)


class ShardManager:
    def __init__(self, num_shards):
        self.shards = [Shard(i) for i in range(num_shards)]

    def send_message(self, message):
        shard = random.choice(self.shards)
        shard.store(message)

    def print_stats(self):
        for shard in self.shards:
            print(f"Shard {shard.id}: {len(shard.messages)} messages")


manager = ShardManager(3)

for _ in range(5000):
    manager.send_message(Message(1, 1, "hello"))

print("\nShard Distribution:")
manager.print_stats()


# Day 6: User-Based Sharding

class UserShardManager(ShardManager):

    def get_shard(self, user_id):
        return self.shards[user_id % len(self.shards)]

    def send_message(self, message):
        shard = self.get_shard(message.user_id)
        shard.store(message)


user_manager = UserShardManager(3)

for _ in range(2000):
    user_manager.send_message(Message(2, 1, "hello"))

for _ in range(5000):
    user_manager.send_message(Message(99, 1, "spam"))

print("\nUser-Based Sharding:")
user_manager.print_stats()


# Day 7: Channel-Based Sharding

class ChannelShardManager(ShardManager):

    def get_shard(self, channel_id):
        return self.shards[channel_id % len(self.shards)]

    def send_message(self, message):
        shard = self.get_shard(message.channel_id)
        shard.store(message)


channel_manager = ChannelShardManager(3)

for _ in range(2000):
    channel_manager.send_message(Message(1, 2, "hello"))

for _ in range(5000):
    channel_manager.send_message(Message(1, 7, "viral"))

print("\nChannel-Based Sharding:")
channel_manager.print_stats()

