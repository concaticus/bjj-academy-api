# 🥋 BJJ Academy Management System

In accordance with the requirements of the Web API Server project, this application is designed to organise and manage operations at a Brazilian Jiu-Jitsu (BJJ) academy. It supports the management of students, instructors, classes, schedules, and attendance records.

The system helps academies track student progress, organise class timetables, and record attendance in a structured and efficient way.

---

## Potential Features

### Create
- **Students**: Add new students with details such as:
  - Name, email, belt rank, stripe count, join date, monthly fee
- **Instructors**: Add new instructors with details such as:
  - Name, belt rank, specialisation, contact details, hourly rate for private classes
- **Classes**: Add new classes with details such as:
  - Class type (Beginner/Fundamentals, No-Gi, Competition Training)
  - Difficulty level, maximum number of students, duration, assigned instructor
- **Schedules**: Add new class schedules with details such as:
  - Day of the week, start time, end time
- **Attendance**: Record attendance for students in scheduled classes:
  - Attendance status (present, absent) + optional notes

---

### 📖 Read
- Retrieve and view **student details** (belt rank, stripe count, contact info).
- Retrieve and view **instructor details** (belt rank, specialisation, assigned classes).
- Retrieve and view **class details** (type, difficulty, instructor, max capacity).
- Retrieve and view **schedules** (day, time, assigned class).
- Retrieve and view **attendance records** (by student, class, or date).

---

### Update
- Modify **student details** (contact info, promotions, stripe count, monthly fee).
- Modify **instructor details** (contact info, hourly rate, specialisation).
- Modify **class details** (instructor, max capacity, duration).
- Modify **schedules** (day, time, duration).
- Modify **attendance records** (status or notes).

---

### Delete
- Remove **student records** (e.g., leaves academy).
- Remove **instructor records** (e.g., stops teaching).
- Remove **classes** (e.g., discontinued).
- Remove **schedules** (e.g., cancelled).
- Remove **attendance records** (e.g., incorrect entry).

---

### Future Ideas
- Student portal for progress tracking.
- Automated fee reminders.
- Mobile-friendly class booking system.
- Analytics dashboard for attendance trends.

----
