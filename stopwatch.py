from textual.app import App, ComposeResult
from textual.widgets import Footer, Header


class Stopwatch(App):
    """A Textual app to manage stopwatches."""
    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header(show_clock=True)
        yield Footer()

if __name__ == '__main__':
    Stopwatch().run()
