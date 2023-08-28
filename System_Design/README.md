[System Design for Beginners Course](https://www.youtube.com/watch?v=m8Icp_Cid5o&loop=0)


https://www.youtube.com/watch?v=i7twT3x5yv8&loop=0

# Interview framework
[5 Tips for System Design Interviews](https://www.youtube.com/watch?v=CtmBGH8MkX4)
- Always seek for feedback (wait for response)
- don't deep dive or focus on details early, always take a step back
- always back up your decision
- think current state vs target state
- abstract the function (database) vs the technology (MySQL)
- Think black box, this service receives X and returns Y
- For Functional requirements, simplify to the maximum, E.g User A wants to send a message to User B


- Introduction 5 minutes
    - Clarify functional requirements , NFRs
    - create 2 columns for each
        -  FR = As a User, NFR = SLA
    - data questions
      - what kind of data needs to be stored? eg music file in s3, user metadat in nosql, transacation data in sql
      - - what data can be cached? static, blob, query often

hl 

- HL architecture (functional requirement focus)
    - Components/Services
    - how they can meet
- Deep Dive (NFR)
    - each components, infrastructure/tool
    - NFR


# Common architecture
- Model View Controller
- Message Queue = producer/consumer = 1to1
- Notification = publisher/subscriber
- Microservice vs Monolith
- Client Side vs Server Side rendering
- Single point of failure vs HA vs DR
- HA vs DR
- RTO, RPO
- Stateless vs Stateful
- Qorum
- Reverse Proxy
- Long Polling vs Short Polling
- Sharding vs Partitioning
- TCP vs WebSocket
- Error Handling: Retry, exponential backoff
- Rate limiting, throttling

# Chat Messaging
[Whatsapp System Design: Chat Messaging Systems for Interviews](https://www.youtube.com/watch?v=vvhC64hQZMk&loop=0)

# Payment system
[Design a Payment System - System Design Interview](https://www.youtube.com/watch?v=olfaBgJrUBI&loop=0)

intro question



- for relational data, what can the table schema look like?
- acceptancecriteria
    - user journey for a specific use case flow through
    

deep dives

- sql is slow for join/ query on many records