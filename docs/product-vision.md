# Product Vision: Calma WorkSpace

## Vision statement

> **For** students, high-school pupils, developers and entrepreneurs
> **who need** a quiet, well-equipped room to study, work alone, work in a group, hold a meeting or follow a training,
> **Calma WorkSpace** is a web application
> **that** lets them find an available room that fits their need, book it and pay for it.
> **Unlike** booking by phone or on paper, our product **guarantees no double bookings**, enforces each room's capacity, maximum duration and buffer time, and gives the staff a clear **daily planning** and **payment receipts**.

## Business goals

1. Increase room occupancy by making availability visible and booking instant.
2. Eliminate scheduling conflicts (overlaps, overbooking).
3. Simplify the staff's daily work: room setup, front-desk planning, payments.

## Actors

| Actor | Type | Main needs |
|---|---|---|
| Student (étudiant) | Client | Revise alone or in a group |
| High-school pupil (élève du secondaire) | Client | Revise; may need parental authorization (bonus) |
| Developer (développeur) | Client | Work on personal tasks, group work |
| Entrepreneur | Client | Hold meetings, organize trainings |
| Manager (gérant) | Staff | Configure rooms (type, capacity, equipment, rules, prices), manage staff accounts |
| Front desk agent (agent de suivi) | Staff | See the daily planning of all rooms |
| Cashier (agent de paiement) | Staff | Record payments and issue receipts |

## Reservation types

Individual revision · Personal task · Group revision · Meeting · Group training

## Release plan (3 sprints × 2 weeks)

| Sprint | Dates | Increment |
|---|---|---|
| Sprint 1 | 25 Nov – 8 Dec 2026 | Accounts & profiles, secure authentication, room configuration, availability search |
| Sprint 2 | 9 Dec – 22 Dec 2026 | Reservations (individual/group, by type) with overlap, capacity, max duration and buffer rules |
| Sprint 3 | 23 Dec 2026 – 5 Jan 2027 | Price calculation, payment recording + receipt, daily planning |

## Definition of Done

A story is **Done** only when:
- its code was reviewed and approved by a teammate in a Pull Request,
- its tests pass,
- its acceptance criteria are validated by the Product Owner,
- it runs in the test environment.
