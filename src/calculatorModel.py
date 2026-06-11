from __future__ import annotations
from dataclasses import dataclass

@dataclass
class CalculatorModel:
    """Manages the state and logic of the calculator
    
       Attributes:
            first_number: First operand of the current operation
            operator: Current operator (+, -, *, /).
            expression: Expression string displayed in the history
            new_number: Flag: the next digit starts a new number.    
    """