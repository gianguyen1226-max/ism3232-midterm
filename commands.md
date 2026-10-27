# Terminal Record: Seabreeze Inn

## 1. Building the project


First I started by creating a folder for my Seabreeze Inn project. After that I  created the Python files 
and a tests folder to organize my work.

Theses are the commands used to set up the project:

```bash
mkdir -p ~/ism3232/seabreeze-midterm-work
cd ~/ism3232/seabreeze-midterm-work
mkdir -p tests
touch business_rules.py main.py README.md commands.md
touch tests/__init__.py tests/test_business_rules.py
```

I used nano to edit my Python files and add the hotel business rules.

```bash
nano business_rules.py
nano main.py
nano tests/test_business_rules.py
```

I also add Git so I could track changes to my project.

```bash
git init
```


## 2. The virtual environment
Command:

```bash
which python3
```

Output:

```text
/home/gianguyen1/ism3232/seabreeze-midterm-work/.venv/bin/python3
```

This output demonstrates that my virtual enivronment is active because Python is active running inside 
my .venv folder.

## 3. The project structure
Command:

```bash
tree -L 2
```

Output:

```text
.
├── README.md
├── __pycache__
│   └── business_rules.cpython-314.pyc
├── business_rules.py
├── commands.md
├── main.py
├── requirements.txt
└── tests
    ├── __init__.py
    ├── __pycache__
    └── test_business_rules.py

4 directories, 8 files
```

This commands demonstrates the files and folders that are in my project 


## 4. Every function and test

```bash
rg 'def ' business_rules.py tests/test_business_rules.py
```

Output:

```text
tests/test_business_rules.py
13:def test_room_cost_two_nights():
17:def test_room_cost_five_nights():
21:def test_room_cost_one_night():
25:def test_discount_three_nights():
29:def test_discount_four_nights():
33:def test_discount_thirteen_nights():
37:def test_discount_fourteen_nights():
41:def test_discount_corporate_guest():
45:def test_cleaning_fee_below_limit():
49:def test_cleaning_fee_at_limit():
53:def test_no_cleaning_fee_above_limit():
57:def test_stay_total_with_discount():
61:def test_credit_check_below_limit():
65:def test_credit_check_at_limit():
69:def test_welcome_package_five_nights():
73:def test_welcome_package_six_nights():
77:def test_welcome_package_below_total_limit():
81:def test_welcome_package_at_total_limit():
85:def test_total_reserved_two_stays():
94:def test_total_reserved_empty_list():
98:def test_largest_stay_two_guests():
107:def test_largest_stay_tie():
116:def test_largest_stay_empty_list():
120:def test_format_stay_line_with_yes_values():
125:def test_format_stay_line_with_no_values():

business_rules.py
1:def calculate_room_cost(nightly_rate: float, nights: int) -> float:
6:def get_stay_discount(nights: int, corporate: bool = False) -> float:
16:def calculate_stay_total(
31:def requires_credit_check(total: float) -> bool:
36:def gets_welcome_package(nights: int, total: float) -> bool:
41:def total_reserved(stays: list) -> float:
56:def largest_stay(stays: list) -> str:
75:def format_stay_line(
```

In this output it conveys the eight functions in business_rules.py and the 25 tests.


## 5. Which files print
Command:

```bash
rg -l 'print\(' --glob '*.py'
```

Output:

```text
main.py
```

Main.py is the only Python file that uses print statements.

## 6. The commit history
Command:

```bash
git log --oneline
```

Output:

```text
0baa173 (HEAD -> main) Add project README and instructions
160cc9f Add pytest tests for hotel business rules
3ce4150 Add hotel reservation report and summary
86f7458 Implement hotel pricing and reservation functions
ab737cf Create application and testing file structure
7422077 Set up Python environment and dependencies
```

These are the six commits I made while developing the project.
