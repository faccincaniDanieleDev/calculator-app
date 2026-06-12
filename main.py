import tkinter as tk
from src import CalculatorApp

def main() -> None:
    """Creates the window, launches the controller and starts the loop."""
    window = tk.Tk()
    CalculatorApp(window)
    window.mainloop()
    
if __name__ == "__main__":
    main()