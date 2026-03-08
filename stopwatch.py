from time import monotonic


from textual import on, events
from textual.app import App, ComposeResult
from textual.containers import ScrollableContainer
from textual.reactive import reactive
from textual.widgets import Footer, Header, Static, Button


class TimeDisplay(Static):
    """Custom TimeDisplay widget."""
    time_elapsed = reactive(0)
    start_time = monotonic()
    accumulated_time = 0

    def on_mount(self):
        self.update_timer = self.set_interval(
            1 / 60,
            self.update_time_elapsed,
            pause=True
        )

    def update_time_elapsed(self):
        self.time_elapsed = (
                self.accumulated_time +
                (monotonic() - self.start_time)
        )

    def watch_time_elapsed(self):
        time = self.time_elapsed
        time, seconds = divmod(time, 60)
        hours, minutes = divmod(time, 60)
        time_str = f"{hours:02,.0f}:{minutes:02.0f}:{seconds:05.2f}"
        self.update(time_str)

    def start(self):
        """Start keep track of the time elapsed."""
        self.start_time = monotonic()
        self.update_timer.resume()

    def stop(self):
        """Stop keep track of the time elapsed."""
        self.accumulated_time   = self.time_elapsed
        self.update_timer.pause()

    def reset(self):
        """Reset the time elapsed."""
        self.accumulated_time = 0
        self.time_elapsed = 0
        self.update_timer.pause()


class StopwatchWidget(Static):
    """Custom Stopwatch widget."""

    @on(Button.Pressed, "#start")
    def start_stopwatch(self):
        self.add_class("started")
        self.query_one(TimeDisplay).start()

    @on(Button.Pressed, "#stop")
    def stop_stopwatch(self):
        self.remove_class("started")
        self.query_one(TimeDisplay).stop()

    @on(Button.Pressed, "#reset")
    def reset_stopwatch(self):
        self.remove_class("started")
        self.query_one(TimeDisplay).reset()

    def compose(self) -> ComposeResult:
        yield Button(
            "Start",
            id="start",
            variant="success"
        )
        yield Button(
            "Stop",
            id="stop",
            variant="error"
        )
        yield Button(
            "Reset",
            id="reset"
        )
        yield TimeDisplay("00:00:00.00")


class Stopwatch(App):
    """A Textual app to manage stopwatches."""
    BINDINGS = [
        ("d", "toggle_dark_mode","Toggle dark mode"),
        ("a", "add_stopwatch", "add"),
        ("r", "remove_stopwatch", "remove")
    ]

    CSS_PATH = "styles.css"


    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header(show_clock=True)
        with ScrollableContainer(id="stopwatches"):
            yield StopwatchWidget()
        yield Footer()

    def action_toggle_dark_mode(self):
        """An action to toggle dark mode."""
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )

    def action_add_stopwatch(self):
        """An action to add a stopwatch."""
        stopwatch = StopwatchWidget()
        container = self.query_one("#stopwatches")
        container.mount(stopwatch)
        stopwatch.scroll_visible()

    def action_remove_stopwatch(self):
        """An action to remove a stopwatch."""
        stopwatches = self.query(StopwatchWidget)
        if stopwatches:
            stopwatches.last().remove()

if __name__ == '__main__':
    Stopwatch().run()
