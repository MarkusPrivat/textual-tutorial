from textual.app import App, ComposeResult
from textual.widgets import Footer, Header


class Stopwatch(App):
    """A Textual app to manage stopwatches."""
    BINDINGS = [
        ("d", "toggle_dark_mode","Toggle dark mode")
    ]
    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header(show_clock=True)
        yield Footer()

    def action_toggle_dark_mode(self):
        """An action to toggle dark mode."""
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )


if __name__ == '__main__':
    Stopwatch().run()
