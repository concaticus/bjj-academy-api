# Planning Document – BJJ Academy Management System

This document contains the **planning stage** of the BJJ Academy Management System project. In order to systematise and bring greater coherence to this projects documentation, a separate file here has been created to document the **planning stage**. The project's README.md can be found [here](./README.md).

It includes the entity relationship diagram (ERD), normalisation process, database justification, API design, validation/error-handling strategies, and a log of feedback incorporated during development.

---

## 1) Entity Relationship Diagram (ERD)

### 1.1 Diagram
The following ERD represents the entities, attributes, and relationships in the system:

![ERD Diagram](./docs/ERD.png)
- add screenshot of ERD

### 1.2 DBML Definition

// Use DBML to define your database structure
// Docs: https://dbml.dbdiagram.io/docs

Table students {
  student_id int [pk, increment]
  name varchar(100)
  email varchar(120) [unique, not null]
  phone varchar(20) // Added phone field
  belt_rank varchar(20) [not null] // White, Blue, Purple, Brown, Black
  stripe_count int [default: 0, note: 'Should be 0-4']
  join_date date [not null]
  monthly_fee numeric(10,2) [not null]
  is_active boolean [default: true] // Added instead of deleting records
}

Table instructors {
  instructor_id int [pk, increment]
  name varchar(100)
  email varchar(120) [unique, not null]
  phone varchar(20) // Added phone field
  belt_rank varchar(20) [not null] // Purple, Brown, Black
  hourly_rate numeric(10,2)
}

Table class_instructors {
  instructor_id int [ref: > instructors.instructor_id]
  class_id int [ref: > classes.class_id]
  role varchar(50) // e.g. Head Coach, Assistant
  primary key (instructor_id, class_id)
}

Table classes {
  class_id int [pk, increment]
  class_type varchar(100) [not null] // e.g. Gi Fundamentals, No-Gi
  difficulty_level varchar(50) [not null] // Beginner, Intermediate, Advanced
  max_students int [not null]
  duration int [not null] // in minutes
}

Table class_schedules {
  schedule_id int [pk, increment]
  class_id int [not null, ref: > classes.class_id]
  day_of_week varchar(20) [not null] // Mon-Sun
  start_time time [not null]
  end_time time [not null]
}

Table attendance {
  attendance_id int [pk, increment]
  student_id int [not null, ref: > students.student_id]
  schedule_id int [not null, ref: > class_schedules.schedule_id]
  attendance_date date [not null]
  status varchar(20) [not null] // present, absent, late
  notes text
}

---
## 2) Normalisation (3NF)

The database for the BJJ Academy Management System has been designed to meet the requirements of **Third Normal Form (3NF)**. This ensures that the data is structured efficiently, avoids redundancy, and maintains integrity.

### First Normal Form (1NF)
- All tables have a primary key.
- All attributes are atomic (e.g. `name`, `email`, `belt_rank` are single values, not lists).
- There are no repeating groups or multi‑valued attributes.

### Second Normal Form (2NF)
- 2NF only applies to tables with **composite primary keys**.
- In this schema, the `class_instructors` table has a composite key (`instructor_id, class_id`). Its non‑key attribute (`role`) depends on the whole key, not part of it, so it satisfies 2NF.
- All other tables use a single‑column surrogate primary key (e.g. `student_id`, `class_id`, `attendance_id`). These are automatically in 2NF if they are in 1NF.
- The `attendance` table uses a surrogate PK (`attendance_id`). To prevent duplicate check‑ins, a **candidate key** (`student_id, schedule_id, attendance_date`) could be enforced with a UNIQUE constraint.

### Third Normal Form (3NF)
- All non‑key attributes depend only on the key, the whole key, and nothing but the key.
- For example:
  - In `students`, attributes such as `belt_rank`, `stripe_count`, and `monthly_fee` depend only on `student_id` and not on each other.
  - In `instructors`, `hourly_rate` depends only on `instructor_id`, not on `belt_rank`.
  - In `attendance`, `status` and `notes` depend only on `attendance_id`.

### Conclusion
Each table in the system is in **3NF**. This design avoids redundancy (e.g. instructor details are not duplicated in classes), ensures data integrity (e.g. attendance records must link to valid students and schedules), and supports efficient queries.

---
## 3) Database Choice & Comparisons

### 3.1 Chosen Database – PostgreSQL
For this project, PostgreSQL was selected as the database system of choice. As a relational database management system (RDBMS), PostgreSQL is well suited to applications requiring structured data, clearly defined relationships, and strong data integrity.In the context of the BJJ Academy Management System, the data model relies heavily on relationships between entities such as students, instructors, classes, schedules, and attendance records. PostgreSQL thus provides the relational structure and enforcement of constraints (primary keys, foreign keys, unique values) that are essential for this type of system.

### 3.2 Comparison to Non-Relational

- MongoDB

### 3.3 Comparison to Other Relational DBs
Other relational systems such as MySQL and SQLite were also considered.

- MySQL
- SQLite


### Conclusion: PostgreSQL balances robustness, relational integrity, and learning relevance.


- more familiar with postgreSQL
- learning materials

---
## 4) API Design

### 4.1 Planned Endpoints

Students:
- GET /students – list students
- GET /students/<id> – view student details
- POST /students – create student
- PUT /students/<id> – update student
- DELETE /students/<id> – remove student

Instructors (repeat pattern)
Classes (CRUD)
Class Schedules (CRUD)
Attendance (CRUD)

### 4.2 HTTP Verbs
- Using correct verbs for CRUD: GET, POST, PUT/PATCH, DELETE.
---

## 5) Validation & Sanitisation Plan
---


## 6) Error Handling Strategy
- Ensure application handles all categories of errors gracefully.

## 7) DRY Principles
---

## 8) Feedback Log:


## Feedback Log

| Date       | Source     | Feedback |
|------------|------------|----------|
| 2025-08-22 | Teacher    | Instructors and classes: one-to-many or many-to-many? |
| YYYY-MM-DD | Peer/Other | _(Add feedback here)_ |

---

### Details

**2025-08-22 – Teacher Feedback**
- **Response:** Changed to **many-to-many** via `class_instructors`.
- **Justification:** This reflects the real-world scenario: a class may have multiple instructors (head coach, assistant), and instructors often teach multiple classes.

**YYYY-MM-DD – Peer/Other Feedback**
- **Response:** _(Write your change here)_
- **Justification:** _(Explain why the change was appropriate or why you chose not to change anything)_

---


## 9) Deployment Plan (Preview)
---

## 10) Potential Roadmap (Future Enhancements)

- Authentication (admin/instructor logins).
- Student portal for attendance & belt progress.
- Automated fee reminders.
- Analytics dashboard for attendance/class utilisation.
