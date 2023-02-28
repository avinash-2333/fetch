"My Data Engineering Takehome Project"

This project is titled "My Data Engineering  Takehome Project".

Overview

The goal of this project is to demonstrate my ability to set up and use Localstack and Postgres to create a simple application that utilizes an SQS queue to store and retrieve data. The application allows a user to add a new item to the queue and also retrieve an existing item from the queue.

Prerequisites

Before running this project, the following prerequisites need to be installed on your local machine:

Docker
Docker Compose
Posstgres sql

To set up this project on your local machine, follow these steps:

Clone the repository: git clone https://github.com/avinash-2333/fetch.git

create docker.yml as given in git link

create login_processor.py as given in git link

Run docker-compose up to start both the Postgres and Localstack containers.

Run docker ps to se container name,id

Open a new terminal window and navigate to the project directory.

Run awslocal sqs receive-message --queue-url http://localhost:4566/000000000000/login-queue to create an SQS queue.


Running the Application


To run the application, follow these steps:


Open a new terminal window and navigate to the project directory.

Run python login_processor.py to start the application.

Run docker exec -it app-postgres-1 psql -d postgres -U postgres -p 5432 -h localhost -c "SELECT * FROM user_logins;" to see the table with masked ip and masked device id.


Troubleshooting

If you encounter any issues with running this project, try the following steps:


Make sure that Docker and Docker Compose are installed on your local machine.

Check that there are no other processes running on port 5432, as that may cause issues with starting the Postgres container.

Make sure that you have created the SQS queue using the command awslocal sqs receive-message --queue-url http://localhost:4566/000000000000/login-queue

Check that you have set up the database and created the necessary tables using the command python setup.py.

If you encounter any other issues, feel free to contact me for assistance.


Conclusion


Thank you for reviewing my data engineering takehome project. If you have any questions or feedback, please feel free to contact me at your earliest convenience.


