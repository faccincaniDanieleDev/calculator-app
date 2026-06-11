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
    
    COLOR_BG = "#1a1a1a"
    COLOR_BTN_NUM = "#333333"
    COLOR_BTN_OP = "#ff9500"
    COLOR_BTN_CE = "#ff3b30"
    COLOR_FG = "white"
    FONT_DISPLAY = ("Helvetica", 24)
    FONT_HISTORY = ("Helvetica", 12)
    FONT_BTN = ("Helvetica", 18)
    
    BUTTON_LAYOUT: list[tuple[str, int, int]] = [
        ("7", 3, 0), ("8", 3, 1), ("9", 3, 2), ("/", 3, 3),
        ("4", 4, 0), ("5", 4, 1), ("6", 4, 2), ("*", 4, 3),
        ("1", 5, 0), ("2", 5, 1), ("3", 5, 2), ("-", 5, 3),
        ("0", 6, 0), (".", 6, 1), ("+", 6, 2), ("=", 6, 3),
    ]
    OPERATORS = {"+", "-", "*", "/", "="}
    
    def __init__(self, window: tk.Tk) -> None:
        self._window = window
        self._display_var = tk.StringVar(value="0")
        self._history_var = tk.StringVar(value="")
        self._on_button_cb: Callable[[str], None] = lambda v: None
        self._on_ce_cb: Callable[[], None] = lambda: None
        self._setup_window()
        self._build_labels()
        self._build_buttons()
        
        
    @property
    def display(self) -> str:
        """Current value of the main display."""
        return self._display_var.get()
    
    @display.setter
    def display(self, value: str) -> None:
        self._display_var.set(value)
        
    @property
    def history(self) -> str:
        """Text of the history row."""
        return self._history_var.get()
    
    @history.setter
    def history(self, value: str) -> None:
        return self._history_var.set(value)
    
    def bind_button(self, callback: Callable[[str], None]) -> None:
        """Connects a callback to the numeric and operator keys.

        Args:
            callback: Function that receives the value of the pressed key.
        """
        self._on_button_cb = callback
        
    def bind_ce(self, callback: Callable[[], None]) -> None:
        """Connects a callback to the CE key.

        Args:
            callback: Function called when CE is pressed.
        """
        self._on_ce_cb = callback
        
    
    def _setup_window(self) -> None:
        """Configures the main window layout and grid."""
        self._window.title("Calculator-app")
        self._window.geometry("600x600")
        self._window.resizable(False,False)
        self._window.configure(bg=self.COLOR_BG)
        
        for col in range(4):
            self._window.columnconfigure(col, weight=1)
        
        self._window.rowconfigure(0, weight=1)
        self._window.rowconfigure(1, weight=2)
        
        for row in range(2, 7):
            self._window.rowconfigure(row, weight=2)
            
    
    def _build_labels(self) -> None:
        """Creates the history label and the main display label."""
        tk.Label(
            self._window, font=self.FONT_HISTORY, anchor="e",
            bg=self.COLOR_BG, fg=self.COLOR_FG,
            textvariable=self._history_var,
        ).grid(row=0, column=0, columnspan=4, sticky="nsew")
        
        tk.Label(
            self._window, font=self.FONT_DISPLAY, anchor="e",
            bg=self.COLOR_BG, fg=self.COLOR_FG, bd=5, relief="sunken",
            textvariable=self._display_var, 
        ).grid(row=1, column=0, columnspan=4, sticky="nsew")
        
    
    def _build_buttons(self) -> None:
        """Creates the CE button and all numeric/operator buttons."""
        tk.Button(
            self._window, text="CE", font=self.FONT_BTN,
            command=lambda: self._on_ce_cb(),
            bg=self.COLOR_BTN_CE, fg=self.COLOR_FG,
        ).grid(row=2, column=3, sticky="nsew")
        
        for label, row, col in self.BUTTON_LAYOUT:
            color = self.COLOR_BTN_OP if label in self.OPERATORS else self.COLOR_BTN_NUM
            tk.Button(
                self._window, text=label, font=self.FONT_BTN,
                command=lambda v = label: self._on_button_cb(v),
                bg=color, fg=self.COLOR_FG
            ).grid(row=row, column=col, sticky="nsew")      