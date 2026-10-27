# ISM3232 Midterm: Seabreeze Inn

- **Name:** Gia Nguyen
- **Version:** DELTA
- **Date:** October 27, 2026

## What This Program Does
This Python program calculates hotel reservation costs for Seabreeze Inn. It utilizes different possible 
discounts, verfies whether if cleaning fees will be used, and determines
which reservations need credit checks or welcome packages.
In addition,This program creates a report showing each guest's total and
a summary of all reservations. 

## Business Rules
1. Room cost is calculated by multiplying the number of nights by the nightly rate.
2. If it stays under 4 nights there would be no discount, but if it stays between 4 to 13 nights they would receive 6% discount
   and if they stays for 14 more nights then they receive 18% off.
3. For corporate guests they are guaranteed to receive at least a 6% discount regardless of the length of stay.
4. There will be a $40 cleaning fee is added when the discounted room cost is $300 or less.
5. If the reservations has a total $2,000 or more then it will require a credit check.
6. Guests staying more than 5 nights with a total of at least $1,000
   receive a welcome package.

## How to Run

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
python3 main.py
```

## How to Test

I wrote 25 tests to check that the program works correctly.

```bash
ruff format --check .
ruff check .
pytest -v
```

## Files in This Repository
business_rules.py
main.py
tests/test_business_rules.py
.gitignore
README.md
commands.md

## AI Use Statement
I used AI assistance to help me understand Python functions, troubleshoot errors, write and test code, 
and complete the project as a learning exercise after the original submission deadline.
My goal was to better understand the material.
