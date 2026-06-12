"""Controller: connects CalculatorModel and CalculatorView.

    Args:
        window: Root tkinter window.
    """
    
import tkinter as tk
from src.calculatorModel import CalculatorModel
from src.calculatorView import CalculatorView

class CalculatorApp:
    
    def __init__(self, window: tk.Tk) -> None:
        """Initializes the controller, model and view.

        Args:
            window: Root tkinter window.
        """
        self._model = CalculatorModel()
        self._view = CalculatorView(window)
        self._view.bind_button(self._handle_button)
        self._view.bind_ce(self._handle_ce)
        
    def _handle_button(self, value: str) -> None:
        """Routes the key press to the correct method.

        Args:
            value: Label of the pressed key.
        """
        
        match value:
            case "+" | "-" | "*" | "/": self._handle_operator(value)
            case "=": self._handle_equals()
            case _: self._handle_digit(value)
            
    def _handle_operator(self, op: str) -> None:
        """Handles the press of an operator key and updates the display.

        Args:
            op: Operator pressed (+, -, *, /).
        """
        new_display, new_history = self._model.apply_operator(self._view.display, op)
        self._view.display = new_display
        self._view.history = new_history
        
    def _handle_equals(self) -> None:
        """Calculates the final result and updates the display."""
        result, history = self._model.apply_equals(self._view.display)
        self._view.history = history
        self._view.display = result
        
    def _handle_digit(self, digit: str) -> None:
        """Appends a digit to the current number on the display.

        Args:
            digit: Character pressed (0-9 or '.').
        """
        self._view.display = self._model.append_digit(self._view.display, digit)
        
    def _handle_ce(self) -> None:
        """Resets the model state and clears the display."""
        self._model.reset()
        self._view.display = "0"
        self._view.history = ""
         