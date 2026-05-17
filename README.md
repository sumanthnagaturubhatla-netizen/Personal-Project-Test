# Online Mock Test Web Application – Nag’s Academy

## Overview

Nag’s Academy is a full-stack Online Mock Test Web Application developed for students to practice aptitude and technical concepts for placement preparation and competitive examinations. The platform provides an interactive environment where students can register, access learning materials, attempt mock tests, and participate in final examinations.

The application was developed using HTML, CSS, JavaScript, Python Flask, and MySQL with SMTP integration for email notifications.

---

# Features

* Student Registration System
* Concepts & Syllabus Section
* Mock Test PDF Access
* Final Test Part-1
* Final Test Part-2
* Responsive User Interface
* Form Validation
* MySQL Database Integration
* Flask Backend APIs
* SMTP Email Integration

---

# Tech Stack

## Frontend

* HTML
* CSS
* JavaScript

## Backend

* Python Flask

## Database

* MySQL

## Additional Tools

* SMTP (Email Service)
* Git & GitHub

---

# Project Structure

```bash
Online-Mock-Test-Web-Application/
│
├── Frontend/
│   ├── Home.html
│   ├── Registration_form_updated.html
│   ├── FinalTestpart1_updated.html
│   ├── FinalTest2.html
│   ├── Index.html
│   ├── Aboutus.html
│   ├── Offers.html
│   ├── Mocktests.html
│   └── pdfs.html
│
├── Backend/
│   └── app.py
│
├── Database/
│   └── online_exam.sql
│
└── README.md
```

---

# Database Tables

## users

Stores student registration details.

## final_test1

Stores answers submitted for Final Test Part-1.

## final_test2

Stores answers submitted for Final Test Part-2.

---

# Installation Steps

## 1. Clone Repository

```bash
git clone https://github.com/yourusername/your-repository-name.git
```

---

## 2. Install Required Python Packages

```bash
pip install flask
pip install flask-cors
pip install mysql-connector-python
```

---

## 3. Configure MySQL Database

Create database:

```sql
CREATE DATABASE online_exam;
```

Import tables into MySQL.

---

## 4. Run Flask Server

```bash
python app.py
```

Server will run at:

```bash
http://127.0.0.1:5000
```

---

# Working of the Application

1. Students register using the registration form.
2. User details are stored in the MySQL database.
3. Students can access concepts and syllabus materials.
4. Mock test PDFs are available for practice.
5. Students attempt Final Test Part-1 and Part-2.
6. Exam responses are stored in the database.
7. Flask APIs handle frontend-backend communication.
8. SMTP integration sends notifications through email.

---

# Learning Outcomes

* Frontend Development
* Backend Development using Flask
* REST API Integration
* Database Connectivity
* Form Validation
* Full-Stack Project Development
* GitHub Project Deployment

---

# Future Enhancements

* Admin Dashboard
* Student Login Authentication
* Live Score Generation
* Leaderboard System
* Timer-Based Exams
* Performance Analytics

---

# Author

Sumanth Naga Turubhatla

---
