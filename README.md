# Todo-Lists

##Todo List Application

This is a simple Todo List application built with Django and Django REST Framework. It allows users to create tasks, add descriptions and tags, set due dates, and track the status of tasks.

##Features-->

-> User-friendly interface to create, view, update, and delete tasks.
-> Ability to add descriptions and tags to tasks.
-> Setting due dates for tasks.
-> Tracking the status of tasks (open, working, done, or overdue).
-> Basic authentication for API endpoints using Basic Authentication.
-> Pagination of task results in the API.

##Installation
1. Clone the repository:
```bash
git clone <git@github.com:Parassirohi/Todo-Lists.git>
cd todo-list-app
```

2. Install the dependencies:
```
pip install -r requirements.txt
```

3. Apply the database migrations:
```
python manage.py makemigrations
python manage.py migrate
```

4. Start the development server:
```
python manage.py runserver
```
5. Access the application in your web browser at http://127.0.0.1:8000/todo/tasks
   this application is deployed on 

##API Endpoints
The Todo List application provides the following API endpoints:

/todo/tasks/:

>GET: Retrieve a list of tasks or create a new task.
>POST: Create a new task.

/todo/tasks/{task_id}/:
>GET: Retrieve a specific task.
>PUT: Update a specific task.
>DELETE: Delete a specific task.

/todo/tags/:
>GET: Retrieve a list of tags or create a new tag.
>POST: Create a new tag.

/todo/tags/{tag_id}/:
>GET: Retrieve a specific tag.
>PUT: Update a specific tag.
>DELETE: Delete a specific tag.

##Authentication-->
The API endpoints require Basic Authentication for access. When making requests to the API, include the username and password in the request headers using Basic Authentication.


##Contribution-->
Contributions to the Todo List application are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request on the project repository.

