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

Conclusion: A single server cannot handle this huge data on same time, it will get very difficult for that, and the server might get down also.
