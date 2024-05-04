# -edu-learning-platform
A comprehensive educational platform built with Django, offering courses, quizzes, discussions, and resources for both students and teachers.



Project Name: Educational Website Backend API

Project Description:
This project is the backend API for an educational website. It provides endpoints for managing users, courses, lessons, enrollments, quizzes, discussion forums, comments, and resources. The API is built using Django and Django REST Framework.

API Endpoints:

1. User Endpoints:
   - GET /api/users/          # Retrieve list of users
   - POST /api/users/         # Create a new user
   - GET /api/users/{id}/     # Retrieve user details
   - PUT /api/users/{id}/     # Update user details
   - DELETE /api/users/{id}/  # Delete a user
   
2. Course Endpoints:
   - GET /api/courses/           # Retrieve list of courses
   - POST /api/courses/          # Create a new course
   - GET /api/courses/{id}/      # Retrieve course details
   - PUT /api/courses/{id}/      # Update course details
   - DELETE /api/courses/{id}/   # Delete a course
   
3. Lesson Endpoints:
   - GET /api/lessons/           # Retrieve list of lessons
   - POST /api/lessons/          # Create a new lesson
   - GET /api/lessons/{id}/      # Retrieve lesson details
   - PUT /api/lessons/{id}/      # Update lesson details
   - DELETE /api/lessons/{id}/   # Delete a lesson
   
4. Enrollment Endpoints:
   - GET /api/enrollments/           # Retrieve list of enrollments
   - POST /api/enrollments/          # Create a new enrollment
   - GET /api/enrollments/{id}/      # Retrieve enrollment details
   - PUT /api/enrollments/{id}/      # Update enrollment details
   - DELETE /api/enrollments/{id}/   # Delete an enrollment
   
5. Quiz Endpoints:
   - GET /api/quizzes/           # Retrieve list of quizzes
   - POST /api/quizzes/          # Create a new quiz
   - GET /api/quizzes/{id}/      # Retrieve quiz details
   - PUT /api/quizzes/{id}/      # Update quiz details
   - DELETE /api/quizzes/{id}/   # Delete a quiz
   
6. Discussion Forum Endpoints:
   - GET /api/discussion-forums/           # Retrieve list of discussion forums
   - POST /api/discussion-forums/          # Create a new discussion forum
   - GET /api/discussion-forums/{id}/      # Retrieve discussion forum details
   - PUT /api/discussion-forums/{id}/      # Update discussion forum details
   - DELETE /api/discussion-forums/{id}/   # Delete a discussion forum
   
7. Comment Endpoints:
   - GET /api/comments/           # Retrieve list of comments
   - POST /api/comments/          # Create a new comment
   - GET /api/comments/{id}/      # Retrieve comment details
   - PUT /api/comments/{id}/      # Update comment details
   - DELETE /api/comments/{id}/   # Delete a comment
   
8. Resource Endpoints:
   - GET /api/resources/           # Retrieve list of resources
   - POST /api/resources/          # Create a new resource
   - GET /api/resources/{id}/      # Retrieve resource details
   - PUT /api/resources/{id}/      # Update resource details
   - DELETE /api/resources/{id}/   # Delete a resource

Usage:
1. Ensure you have Django installed on your machine.
2. Clone the repository from [repository link].
3. Navigate to the project directory.
4. Run the Django development server using the command: python manage.py runserver
5. You can now make requests to the API endpoints using tools like cURL, Postman, or directly from your frontend application.

Note: Make sure to set up authentication tokens or sessions for protected endpoints that require authentication.

For any questions or issues, please contact 01143681203.

