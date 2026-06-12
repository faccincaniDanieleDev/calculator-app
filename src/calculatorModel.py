"""Manages the state and logic of the calculator
    
       Attributes:
            first_number: First operand of the current operation
            operator: Current operator (+, -, *, /).
            expression: Expression string displayed in the history
            new_number: Flag: the next digit starts a new number.    
    """

from __future__ import annotations
from dataclasses import dataclass

@dataclass
class CalculatorModel:
    
    first_number: str = ""
    operator: str = ""
    expression: str = ""
    new_number: bool = False
    ERROR_DIVISION  = "Error"
    ERROR_NO_INPUT  = "Insert a value"
    
    @property
    def has_operator(self) -> bool:
        """returns True if an operator has already been entered."""
        return self.operator != ""
    
    def reset(self) -> None:
        """reset de calculator state completely (CE)"""
        self.first_number = ""
        self.operator = ""
        self.expression = ""
        self.new_number = False
        
        
    def apply_operator(self, current_display: str, op: str) -> tuple[str,str]:
        """Handles the press of an operator key
        
                Args:
                    current_display: Value currently shown on the display
                    op: Operator pressed (+, -, *, /)
                    
                Returns:
                    Tuple (new_dislay, new_history)
        """
        
        if self.has_operator:
            result = self._evaluate(self.first_number,self.operator, current_display)
            self.expression += current_display + op
            self.first_number = result
            display = result
            
        else:
            self.expression += current_display + op
            self.first_number = current_display
            display = current_display
            
        self.operator = op
        self.new_number = True
        return display, self.expression
    
    
    def apply_equals(self, current_display: str) -> tuple[str,str]:
        """Calculates the final result of the expression.

        Args:
            current_display: Second operand shown on the display.

        Returns:
            Tuple (result, history). On error returns
            ("Error", "") or ("Insert a value", "").
        """
        
        if not self.first_number:
            return self.ERROR_NO_INPUT, ""
        
        history = self.expression + current_display + "="
        
        try:
            result = self._evaluate(self.first_number,self.operator,current_display)
            
        except ZeroDivisionError:
            self.reset()
            return self.ERROR_DIVISION, ""
        
        self.reset()
        self.new_number = True
        return result, history
    
    
    def append_digit(self, current_display: str, digit: str) -> str:
        """Appends a digit to the current number on the display.

        Args:
            current_display: Value currently shown on the display.
            digit:           Character to append (0-9 or '.').

        Returns:
            New value to show on the display.
        """
        
        if current_display in (self.ERROR_NO_INPUT, self.ERROR_DIVISION) or self.new_number:
            self.new_number = False
            return digit
        
        if digit == "." and "." in current_display:
            return current_display
        
        if current_display == "0" and digit != ".":
            return digit
        
        return current_display + digit
    
    @staticmethod
    def _evaluate(a: str, op: str, b: str) -> str:
        """Evaluates a op b and returns the result as a string.

        Args:
            a:  First operand.
            op: Operator (+, -, *, /).
            b:  Second operand.

        Returns:
            Result rounded to 10 decimal places.

        Raises:
            ZeroDivisionError: If b == "0" and op == "/".
        """
        fa, fb = float(a), float(b)
        
        match op:
            case "+": result = fa + fb
            case "-": result = fa - fb
            case "*": result = fa * fb
            
            case "/":
                if fb == 0:
                    raise ZeroDivisionError
                result = fa / fb
                
            case _: result = fb
            
        result = round(result, 10)
        
        if result.is_integer():
            return str(int(result))
        
        return str(result)