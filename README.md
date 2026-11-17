# PLP1 - OOP Activity 1: Airline Ticket Booking System

African Leadership University - Introduction to Python Programming and Databases

## Group members
| Member | GitHub | Part |
|--------|--------|------|
|Ryan kamana Iganze | ryaniganze | Project leader, Passenger parent class |
| Tona Faradowza | Tona-tech-byte |
| Fiorella Demba Keza| DembaFiorella| Business class, method overriding |
| Jeremie Rufora | jrufora-eng | First Class |
| Shekinah Eva Kamikazi | Shekinah2807 | Input validation and interactive booking system |
| KAREMERA Imanzi Ochri| ochr1 | Main program, testing, documentation |

## Design
- `Passenger` (parent): name, location, destination, date; `get_passenger_info()`, `get_weight_allowance()` (default 20 kg).
- `Economy`: adds `seat_preference`.
- `Business`: adds `lounge_pass_code` and overrides `get_weight_allowance()` to return 100 kg (method overriding).
- `FirstClass`: adds `suite_number` and `chauffeur_service` (True or False); keeps the default 20 kg.
- Every child class calls `super().__init__()` to reuse the parent's attributes (inheritance).
- Class-specific data is only requested for the ticket class the user selected.

## Error handling
- Menu choices outside 1 to 3 are rejected and the user is asked again.
- Empty strings are rejected for every text field.
- The chauffeur answer must be yes or no (y or n also accepted).

## How to run
    python PLP1_OOP_Activity1.py

Only the Python standard library is used (no external libraries).

## Testing
Manually tested all three ticket classes (Economy 20 kg, Business 100 kg, First Class 20 kg),
an invalid menu choice (5), empty fields, and an invalid chauffeur answer (maybe).