# 🧮 Python Calculator

A lightweight desktop calculator built with Python and tkinter, structured with a clean **MVC architecture**.

---

## Features

- Basic operations: addition, subtraction, multiplication, division
- Live expression history shown above the display
- Edge case handling: division by zero, empty input, duplicate decimal point
- Clean OOP architecture: Model / View / Controller

---

## Project Structure
```
calculator-app/
│
├── src/
│   ├── __init__.py
│   ├── model.py        # State and calculation logic
│   ├── view.py         # tkinter UI, no logic
│   └── controller.py   # Connects model and view
│
├── tests/
│   └── test_model.py
│
├── main.py
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md
```
---

## Requirements

- Python 3.10+
- tkinter — included in the Python standard library

---

## Getting Started

```bash
git clone https://github.com/faccincaniDanieleDev/calculator-app.git
cd calculator-app
python main.py
```

---

## Running Tests

```bash
pip install pytest
pytest tests/
```

---

## License

MIT License — see [LICENSE](LICENSE) for details.
