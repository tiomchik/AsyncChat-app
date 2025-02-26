# AsyncChat-App

Welcome to **AsyncChat**, a portfolio project designed to demonstrate the capabilities of real-time chat protocols, making it ideal for live communication scenarios.

![Screenshot from 2024-07-10 09-50-59](https://github.com/gaurav-jo1/AsyncChat-app/assets/93304640/8beea5b0-ae83-4e51-b05e-08da6b084d1c)

![Screenshot from 2024-07-10 09-51-37](https://github.com/gaurav-jo1/AsyncChat-app/assets/93304640/426db404-74a9-4ab5-9a1a-cd87286facd9)


## Technologies Used

**Backend:** 🌐 Built with Python and Django, AsyncChat-App ensures secure and scalable server-side operations. Integration of Redis enhances performance, while PostgreSQL handles data storage efficiently.

**Frontend:** 🎨 Utilizing TypeScript and React, AsyncChat-App offers a dynamic and responsive user interface. SCSS is employed for streamlined styling, ensuring a visually appealing and intuitive user experience.

**Infrastructure:** 🐳 Docker and GitHub Actions are instrumental in automating deployment and continuous integration processes, maintaining project reliability and consistency. AsyncChat-App's architecture is adaptable, suitable for scaling and building infrastructures similar to advanced systems like ChatGPT.

**Testing:** 🧪 Pytest is implemented for rigorous backend testing, ensuring code quality and reliability throughout development cycles.

## Getting Started 🔥

To get started with the project, follow these steps:

1. **Clone the repository to your local machine:**
   ```sh
   git clone https://github.com/gaurav-jo1/AsyncChat-app
   ```

2. **Navigate to the project directory:**
   ```sh
   cd AsyncChat-app
   ```

3. **Install frontend dependencies:**
   ```sh
   cd frontend && npm install
   ```

4. **Set up the backend environment (optional for development):**
   - Create a virtual environment:
     ```sh
     cd backend && virtualenv venv
     ```
   - Activate the virtual environment and install dependencies:
     ```sh
     source ./venv/bin/activate && pip install -r requirements.txt
     ```

5. **Set up the database configuration:**
   - Navigate to the database directory and create the `postgres_auth.txt` file:
     ```sh
     cd database/ && echo "postgres" > postgres_auth.txt
     ```

6. **Run the application:**
   - Navigate to the root directory and start the services with Docker:
     ```sh
     docker compose up
     ```

## User Authentication 🚀

The following table contains the usernames and passwords for the sample users included in this application. You can use these credentials to log in and test the application.

| Username | Password        |
|----------|-----------------|
| John     | securepassword  |
| Anya     | securepassword  |
| Danny    | securepassword  |
| Alice    | securepassword  |
| Bob      | securepassword  |

These credentials are meant for testing and demonstration purposes only.

## Access the Application

Access the application at: 🔗 http://localhost:5173

That's it! You should now be able to get started with the project and use Docker Compose to run the application. If you have any questions or issues, feel free to open an issue on the repository. Thanks for using my project!
