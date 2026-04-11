Day 1–2: System Thinking

Situation:
A sudden event:
    50,000 users join in 5 minutes
    1 channel gets 80% of traffic

Problem:
    If you had only one server:
        what fails first?

(where bottlenecks will occur): basically if such situation happens and we try handle that using one server only
1) We'll see that memory will rapidly starts getting full as the messages will start getting stored in one place(server).
2) CPU will getting overloaded due to continuous message incoming
3) System will get slow, as it is containing only 1 server which is getting loaded with tons of messages

(what data grows fastest): The fastest growing data in this system will be "Messages and Active Users"

At small scale like 10 users, everything will works smoothly.
But when users increase to thousands:

1) System will becomes slow
2) Data handling will becomes very much difficult

Conclusion: A single server cannot handle this huge data on same time, it will get very difficult for that, and the server might get down also. We need multiple servers (sharding).

---

Day 3–4: Building a Single Server System

We see that system will works fine with a small number of users, but when the number of messages increases, memory keeps growing without limit.

we'll face problem like:

1) No load distribution
2) Risk of system crash

---

Day 5: Introducing Shards

Multiple servers basically (shards) are introduced, Messages which are coming basically the load is getting distributed randomly into the shards and not any server is getting as such any load.

We Observation that:

1) Load is now splitted
2) But there is still no proper logic exists

Conclusion: We still need a better routing strategy


---

Day 6: User-Based Sharding

As you can see the messages are routed based on user ID, but one active user overloaded a shard

Conclusion: This strategy will get failed when a user generates heavy traffic.

---

Day 7: Channel-Based Sharding

You can observe that messages are routed based on channel ID, but one viral channel overloaded a shard

Conclusion: By observing we can see that its not suitable for spike situations.

---