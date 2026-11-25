# Product Backlog: Calma WorkSpace

**Product Owner (Sprint 1):** Ayoub · **Last update:** 25 Nov 2026
**Priority (MoSCoW):** Must / Should / Could · **Estimation:** story points (1, 2, 3, 5, 8)

| ID | User story | Priority | Points | Sprint |
|---|---|---|---|---|
| US1 | As a **visitor**, I want to register by choosing my profile (student, pupil, developer, entrepreneur) so that I can use the service | Must | 3 | 1 |
| US2 | As a **user**, I want to log in and log out securely so that my account is protected | Must | 3 | 1 |
| US3 | As a **staff member**, I want to have my own role (manager, front desk, cashier) so that I only see the features I need | Must | 2 | 1 |
| US4 | As a **manager**, I want to create a room (name, type, capacity, equipment) so that clients can book it | Must | 3 | 1 |
| US5 | As a **manager**, I want to edit or deactivate a room so that the offer stays up to date | Must | 2 | 1 |
| US6 | As a **manager**, I want to set the max duration, buffer time and prices of a room so that booking rules are applied | Must | 2 | 1 |
| US7 | As a **client**, I want to search for available rooms by date, time slot and number of persons so that I find a suitable room | Must | 5 | 1 |
| US8 | As a **client**, I want to book a room alone or as a group, choosing the reservation type, so that my place is guaranteed | Must | 5 | 2 |
| US9 | As a **client**, I want the system to refuse overlapping bookings so that a room is never double-booked | Must | 5 | 2 |
| US10 | As a **client**, I want the system to block bookings above capacity, above max duration or without buffer time so that the rules are respected | Must | 5 | 2 |
| US11 | As a **client**, I want to see my reservations so that I can keep track of them | Should | 2 | 2 |
| US12 | As a **client**, I want to see the price (per hour / per day) before confirming so that I know what I will pay | Must | 3 | 3 |
| US13 | As a **cashier**, I want to record a payment so that the reservation is marked as paid | Must | 3 | 3 |
| US14 | As a **cashier**, I want to generate a receipt so that the client has proof of payment | Must | 3 | 3 |
| US15 | As a **front desk agent**, I want to see the daily planning of all rooms so that I can welcome clients | Must | 5 | 3 |
| US16 | As a **client**, I want to cancel a reservation so that the room becomes free again | Could | 2 | Bonus |
| US17 | As a **client**, I want to take a monthly subscription so that I pay less as a regular user | Could | 5 | Bonus |
| US18 | As a **parent of a pupil**, I want to give an authorization so that my minor child can book a room | Could | 3 | Bonus |
| US19 | As a **client**, I want to receive notifications about my bookings so that I don't forget them | Could | 3 | Bonus |
| US20 | As a **manager**, I want a dashboard (occupancy, revenue) so that I can follow the activity | Could | 5 | Bonus |

**Total:** 69 points · Sprint 1: 20 pts · Sprint 2: 17 pts · Sprint 3: 14 pts · Bonus: 18 pts

---

## Acceptance criteria: Sprint 1

**US1: Register with profile**
- The form asks for username, email, password (twice) and profile type.
- An already used username or email is refused with a clear message.
- The password is stored hashed (never in plain text).
- After registration, the user is redirected to the login page.

**US2: Log in / log out**
- A wrong username or password shows an error message.
- After login, the user's name appears in the navigation bar.
- Logout returns the user to the home page.
- Pages that require an account redirect anonymous visitors to the login page.

**US3: Staff roles**
- Staff accounts (manager, front desk, cashier) can only be created by the manager / administrator.
- A client cannot open manager pages (access refused or redirected).

**US4: Create a room**
- Only the manager can access the room creation form.
- Capacity must be greater than 0.
- The room name is unique.
- The new room appears in the room list.

**US5: Edit / deactivate a room**
- Changes are saved and visible in the room list.
- A deactivated room no longer appears in search results.

**US6: Room rules and prices**
- Max duration > 0, buffer time ≥ 0, hourly and daily prices ≥ 0.
- The values are displayed on the room detail page.

**US7: Search available rooms**
- The end time must be after the start time, otherwise an error is shown.
- Only active rooms with capacity ≥ number of persons are listed.
- If no room matches, the message "No room available" is shown.
