"""Builds and manages all tkinter widgets.

    The View is passive: it has no knowledge of the calculation logic.
    It exposes display and history as properties, and two bind_*
    methods to connect the Controller callbacks.

    Args:
        window: Root tkinter window to build the UI on.
    """
    
import tkinter as tk
from typing import Callable

class CalculatorView:
    pass