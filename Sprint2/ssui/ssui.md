# Sprint 2

**Name**: Samuel Sui  
**Github ID**: SamJSui  
**Group name**:  Watchtower  

### What you planned to do
(Give a short bulleted list of the items you planned to do for this sprint. Include the github issue number and link to the issue)
- [#28](https://github.com/utk-cs340-spring23/Watchtower/issues/28)
- [#29](https://github.com/utk-cs340-spring23/Watchtower/issues/29)
- [#30](https://github.com/utk-cs340-spring23/Watchtower/issues/30)

### What you did not do
- Connect backend to frontend

### What problems you encountered
- Inconsistencies with executing SQL queries and commands through Python libraries

### Issues you worked on
- [#28](https://github.com/utk-cs340-spring23/Watchtower/issues/28)
- [#29](https://github.com/utk-cs340-spring23/Watchtower/issues/29)
- [#30](https://github.com/utk-cs340-spring23/Watchtower/issues/30)

### Files you worked on
- *Watchtower/backend/app.py*
- *Watchtower/backend/db.py*

### What you accomplished
- The sensors collect a variety of different types of data, such as CPU, RAM, network, etc.
  - Hello payload
    - The initial payload that is sent by the sensors at run time that contains one-time-only day, such as RAM installed.
    - My flask backend processes that data and inserts it into a **machines** database (and table), housing all the devices currently supported by the application
  - Checkin payload
    - These are the recurrent payloads that are consistently sent every 5 (configurable, but this is the default) seconds and are constantly updating the database
    - The **database structure** for these: each machine gets their own table within a categorized target of data collection (my desktop machine gets its own table within the **battery** database)