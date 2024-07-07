The described architecture is designed for a messaging application that involves a central server, multiple groups, and users interacting within those groups. Here's a breakdown of its components and operations:

Components:
Central Server (Message Server):
Maintains a list of active groups with their IP addresses.
Registers and manages group servers.
Provides functionality for users to request and receive the list of available groups.

Group Servers:
Each group server manages a specific group identified by a unique UUID.
Maintains a list of users currently part of the group (USERTELE).
Stores and manages messages sent within the group, including timestamps.
Allows users to join or leave the group and exchange messages.
Handles multiple user interactions simultaneously using threads.

Users:
Can join multiple groups concurrently.
Can send messages to groups they are part of.
Can fetch messages from groups based on specified timestamps or retrieve all messages if no timestamp is provided.
Interaction with groups involves requesting to join or leave, sending and receiving messages.

Operations:
User Interactions with Message Server:
Requesting the list of available groups.
User Interactions with Groups:

Join Group: Users request to join a group by providing the group's UUID. Upon successful validation, the group adds the user to its USERTELE.
Leave Group: Users request to leave a group, and the group removes the user from its USERTELE.
Get Messages: Users request messages from a group, specifying a timestamp to fetch messages from that time onward. If no timestamp is specified, all messages are retrieved.
Send Message: Users send messages to the group, which verifies the user's membership and stores the message with a timestamp.
Group Server Interactions with Message Server:

Group servers register themselves with the message server, providing their name and IP address.
Communication Patterns:
User-Message Server Interaction:

Users request and receive information about available groups.
User-Group Interaction:

Users interact with groups to join, leave, fetch messages, and send messages.
Message Server-Group Server Interaction:

Message server manages and registers group servers, maintaining a list of active groups.
Implementation Details:
Concurrency: Utilizes threads to handle multiple user interactions concurrently within each group server.
Persistence: Messages are stored in memory on group servers to ensure availability even as users join or leave groups.
Error Handling: Provides success or failure responses for operations such as joining groups or sending messages, ensuring robustness and reliability.
This architecture supports scalable messaging functionalities, allowing users to participate in multiple groups and facilitating efficient message exchange within each group through a centralized and distributed approach.
