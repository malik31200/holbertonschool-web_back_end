Stage 1 Report – Team Formation & MVP Definition
1. Kick-Off Meeting Overview

The purpose of the initial meeting was to:

Introduce team members and their backgrounds

Define technical and organizational roles

Establish communication and collaboration rules

Identify project stakeholders

Set a solid foundation for the project execution

2. Team Formation & Roles
    Christophe BARRERE

Primary Role: Project Manager & Lead Back-End Developer
Skills: Back-end architecture, database management, business logic, project coordination
Strengths: Global project vision, structured workflow, strong back-end expertise

    Malik BOUANANI

Primary Role: Lead Front-End Developer & UX/UI Designer
Skills: Web integration, UX design, UI design, user flow optimization
Strengths: Strong visual sense, design coherence, user-centric thinking

    Technical Roles Breakdown
Project Manager — Christophe

Task planning and prioritization

Progress tracking

Team coordination

Communication with external stakeholders

Front-End Development

Lead: Malik

Support: Christophe
Reason: Malik ensures visual and UX consistency; Christophe provides integration support as needed.

Back-End Development

Lead: Christophe

Support: Malik
Reason: Christophe manages server logic, security, API design, and databases; Malik assists to ensure front/back alignment.

UX/UI Designer — Malik

Wireframes & prototypes

User flows

UI design and branding consistency

3. Tools & Communication Workflow

Discord → Internal communication

Trello → Project management

GitHub → Version control

Figma → Design & mockups

Google Drive → Documentation & file sharing

Team Norms

Clear and respectful communication

Daily check-ins + weekly progress review

Advance planning of weekly tasks

Technical decisions discussed by both developers

Quick reporting of issues/blockers

Commitment to deadlines

Mandatory documentation of code

4. Stakeholder Analysis
    Internal Stakeholders
1. Development Team

Designs, builds, tests, and maintains the application.

2. Project Manager

Clarifies requirements

Prioritizes features

Organizes the workflow

Communicates with external stakeholders

    External Stakeholders
1. Actual (Project Sponsor)

Defines scope and priorities

Validates deliverables

Expects a reliable solution to manage sports classes

2. Gym Administrators

Create and manage classes

Track registrations

Manage users and payments
They act as admin users.

3. Sports Coach

Maintains class schedules

Communicates availability

Impacted by class occupancy and cancellations

4. Actual Employees (End Users)

View the schedule

Book or cancel classes

Buy session passes

Manage their account and history

5. Payment Service Provider

Handles secure transactions

Sends payment confirmations

Influences accounting workflows

6. Holberton / SWE / Mentors

Provide guidance

Review technical quality

Evaluate the project

5. Brainstorming & Idea Exploration
5.1 Research Phase

Each team member conducted research involving:

Real-world business problems

Trends in sports, wellness, and web applications

Analysis of existing solutions (booking apps, sport platforms, payment systems)

Key identified needs:

Limited and controlled class reservations

A centralized management tool

Automated payment tracking

Better user experience for employees

Reduced manual workload for administrators

5.2 Brainstorming Session
Methods Used

SCAMPER Framework

“How Might We” (HMW) questions

Comparative analysis of existing apps

SCAMPER Examples

Substitute: Replace paper/Excel management with a digital platform

Combine: Schedule + payment + reservation in one tool

Adapt: Adapt gym management apps to a corporate context

Modify: Add session pass/carnet features

Eliminate: Remove manual errors and overbooking

Reverse: Provide flexible reservation instead of coach-fixed schedules

HMW Questions

How might we simplify class registration?

How might we avoid overbooking?

How might we secure payments?

How might we improve schedule visibility?

How might we enhance the employee experience?

6. Project Idea Evaluation
6.1 Evaluation Criteria

Technical feasibility

User impact

Team skill alignment

Technical risks

Scalability

Complexity

Value added to the company

6.2 Ideas Explored
🟢 Idea 1 — Sports Class Management App (Actual)

View schedule

Register for classes

Online payment

Session pass & history

Admin panel for courses and users

🟡 Idea 2 — Amateur Football Social Network (Occitanie)

Calendar, results, media sharing

Likes, comments, follow system

🟠 Idea 3 — Pottery Class Booking App

Booking calendar

Presentation of courses

Online payments

6.3 Project Ranking
Project	Feasibility	Risks	Impact	Scalability	Rank
Sports App (Actual)	⭐⭐⭐⭐⭐	⭐⭐	⭐⭐⭐⭐⭐	⭐⭐⭐⭐	🥇 1
Football Social Network	⭐⭐	⭐⭐⭐⭐⭐	⭐⭐⭐⭐	⭐⭐⭐⭐⭐	🥈 2
Pottery Classes	⭐⭐⭐⭐⭐	⭐⭐	⭐⭐⭐⭐	⭐⭐⭐⭐	🥉 3
7. Final MVP Selection & Refinement
✔ Selected MVP: Web Application for Sports Class Management (Actual)
7.1 Problem Statement

The current management of sports classes suffers from:

Manual processes

No centralized system

High risk of overbooking

Manual payment handling

No clear tracking of user history

Time-consuming admin tasks

    Main Problem:
A lack of a simple, reliable, and centralized digital solution to manage classes, registrations, and payments.

7.2 Proposed Solution
For Employees:

View class schedule

Register online

Pay securely

Track session history and pass usage

For Administrators:

Create and manage classes

Set capacity limits

Manage users

Track payments

    Main Goal:
To centralize and automate sports class management, improving organization and user experience.

8. Target Audience
Primary Users:

Employees of Actual

Secondary Users:

Gym administrators

Sports coach

9. Application Type

Web Application

Fully responsive (desktop, tablet, mobile)

User roles: Admin, Employee

10. Why This MVP Was Selected

This solution was chosen because:

It solves a real, concrete problem

It offers high impact for the company

It is technically feasible within the timeline

It aligns perfectly with team skills:

Front-End

Back-End

UX/UI

It provides strong future scalability (statistics, mobile app, AI coaching, etc.)

Other ideas were rejected due to:

Higher risks

Lack of alignment with real needs

More complexity or less relevance

11. Key Features & SMART Objectives
Key MVP Features

Class booking system

Secure online payment

Class management for administrators

SMART Objectives

S1: Allow a user to book a class in under 2 minutes

S2: Guarantee 100% respect of class capacity limits

S3: Allow an admin to create a new class in under 1 minute

12. Project Scope
✔ In Scope

Web application

User authentication (admin + employee)

Class creation and management

Class registration

Online payments

Session pass (carnet)

Reservation history

User management

❌ Out of Scope

Native mobile application

Advanced analytics

AI coaching

Physical performance tracking

SMS notifications

13. Risks & Mitigation Strategies
Risk	Mitigation
Limited experience with payment systems	Tutorials, sandbox testing, official documentation
Data security issues	Secure authentication, best security practices
High workload	Clear task distribution, weekly progress follow-up
14. Final Outcome

By the end of Stage 1, the team has:

A clearly defined MVP

A well-established scope

Measurable objectives

A solid foundation for Stage 2 (Planning & Architecture)

Stage 2: Project Planning
1. High-Level Timeline (Mandatory)

Below is the simple timeline mapping the major stages of the project, as required:

Stage 1: Idea Development

Stage 2: Project Planning

Stage 3: Technical Documentation

Stage 4: MVP Development

Stage 5: Project Closure

Gantt Chart Timeline
gantt
    title Project Timeline - ACTUAL Sports App
    dateFormat  YYYY-MM-DD
    axisFormat  "Week %W"

    section Project Stages
    Stage 1 – Idea Development        :done,    s1, 2025-12-01, 14d
    Stage 2 – Project Planning        :active,  s2, 2025-12-15, 7d
    Stage 3 – Technical Documentation :         s3, 2025-12-22, 21d
    Stage 4 – MVP Development         :         s4, 2026-01-12, 56d
    Stage 5 – Project Closure         :         s5, 2026-03-09, 7d
