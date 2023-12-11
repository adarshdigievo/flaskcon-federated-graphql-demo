# Demo 2 - GraphQL Federation

Assuming venv is activated and requirements are already installed.

### For each service (users and posts):
1. CD to the path of the service (users-service and posts-service)
2. Run 'init_db.py' to add dummy data to DB
3. Run 'app.py' to run the Flask application. Both apps should run in parallel on ports 5001 and 5002

### For federating:

1. Install the rover cli using [this guide](https://www.apollographql.com/docs/rover/getting-started/)
2. Use 'rover dev --url http://localhost:5001' command to add users service. Name it as 'users' when prompted. Repeat the same for 'posts' also in a new terminal window and change the port to 5002 where the posts service is running.
3. Navigate to http://localhost:4000 to access the Federation router and to explore the supergraph