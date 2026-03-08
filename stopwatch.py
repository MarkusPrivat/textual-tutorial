from textual.app import App, ComposeResult
from textual.containers import ScrollableContainer
from textual.widgets import Footer, Header, Static, Button


class TimeDisplay(Static):
    """Custom TimeDisplay widget."""
    pass


class StopwatchWidget(Static):
    """Custom Stopwatch widget."""
    def compose(self) -> ComposeResult:
        yield Button( "Start", id="start", variant="success")
        yield Button("Stop", id="stop", variant="error")
        yield Button("Reset", id="reset")
        yield TimeDisplay("00:00:00.00")


class Stopwatch(App):
    """A Textual app to manage stopwatches."""
    BINDINGS = [
        ("d", "toggle_dark_mode","Toggle dark mode")
    ]

    CSS_PATH = "styles.css"


    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header(show_clock=True)
        with ScrollableContainer(id="stopwatchs"):
            yield StopwatchWidget()
            yield StopwatchWidget()
        yield Footer()

    def action_toggle_dark_mode(self):
        """An action to toggle dark mode."""
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )


if __name__ == '__main__':
    Stopwatch().run()
