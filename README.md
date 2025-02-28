# Bug-Tracking-System---Web-Application


Bug Reporting: Allows testers to submit detailed bug reports including title, description, priority, severity, and file attachments.
Dashboard for Testers: Testers can view the list of all submitted bugs and their current status.
Bug Status Tracking: Developers and project managers can update bug statuses, ensuring real-time visibility into bug progress.
File Attachments: Users can attach relevant screenshots or log files to help developers understand the issue better.
Role-Based Access: Different user roles (Tester, Developer, Manager) with varying levels of access and functionality.
User-Friendly Interface: Simple, clean UI for easy interaction.

Technologies Used
Frontend: HTML, CSS
Backend: Flask (Python)
File Handling: Flask’s file upload functionality
Data Storage: (Not mentioned in this description - adjust as per your database choice)
Template Engine: Jinja2 (for rendering dynamic content)

# Project Structure
/templates
    - report_bug.html
    - dashboard.html
/static
    - styles.css (if applicable)
/uploads
    - (for uploaded bug attachments)
app.py

# Key Functionalities
Report Bug Page: Form to submit new bugs.
Dashboard Page: Lists all reported bugs.
Status Management: Ability to change and track bug status.
File Upload Handling: Save attachments to server storage.

# How to Run
Clone the repository.
Install the required dependencies:
pip install -r requirements.txt
# Run the application:
python app.py
Open the browser and visit:
cpp
Copy
Edit
http://your id /
