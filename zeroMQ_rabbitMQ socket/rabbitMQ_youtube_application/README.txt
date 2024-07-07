Components:

1. YouTubeServer.py
   - Functionality: Acts as the central server handling user and YouTuber interactions via RabbitMQ messages.
   - Methods:
     - `consume_user_requests()`: Listens for login and subscription/unsubscription requests from users. Prints messages upon user actions.
     - `consume_youtuber_requests()`: Listens for new video upload requests from YouTubers. Prints messages upon video uploads.
     - `notify_users()`: Sends notifications to all subscribed users when a YouTuber uploads a new video.

2. Youtuber.py
   - Functionality: Represents the service for YouTubers to upload videos.
   - Methods:
     - `publishVideo(youtuber, videoName)`: Sends a video upload request to `YouTubeServer.py` via RabbitMQ. Prints "SUCCESS" upon successful receipt of the video.

3. User.py
   - Functionality: Represents the service for users to log in, subscribe/unsubscribe to YouTubers, and receive notifications.
Methods:
     - `updateSubscription(user, action, youtuber)`: Sends subscription/unsubscription requests to `YouTubeServer.py` via RabbitMQ. Prints "SUCCESS" upon successful completion.
     - `receiveNotifications(user)`: Listens for notifications from `YouTubeServer.py` via RabbitMQ. Prints new video upload notifications in real-time.


Flow of Service:

1. Start YouTubeServer.py:
   - Initializes the server to handle incoming messages from users and YouTubers.
   - Sets up message queues for handling login, subscription/unsubscription requests from users, and video upload requests from YouTubers.

2. Run Youtuber.py:
   - YouTubers execute this script to upload videos to the server.
   - Sends video upload requests to `YouTubeServer.py` via RabbitMQ.
   - Receives "SUCCESS" confirmation upon successful transmission.

3. Run User.py:
   - Users execute this script to perform actions such as login, subscription, unsubscription, and receive notifications.
   - Submits login and subscription/unsubscription requests to `YouTubeServer.py` via RabbitMQ.
   - Subscribes to real-time notifications for video uploads by subscribed YouTubers.
   - Prints notifications for new video uploads in real-time.

4. Simultaneous Execution:
   - Multiple instances of `Youtuber.py` and `User.py` can run concurrently.
   - Multiple users can log in simultaneously and receive notifications concurrently for videos uploaded by subscribed YouTubers.

This architecture utilizes RabbitMQ for asynchronous communication between the YouTube server, YouTubers, and users, enabling scalable and concurrent operations. It ensures real-time updates for users subscribed to YouTubers and supports seamless interaction across multiple users and YouTubers simultaneously.
