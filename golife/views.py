import curses
from time import sleep

from golife.grid import LifeGrid


class CursesView:
    def __init__(self, pattern, gen=8, frame_rate=10, bbox=(0, 0, 50, 50)):
        self.pattern = pattern
        self.gen = gen
        self.frame_rate = frame_rate
        self.bbox = bbox

    def show(self):
        curses.wrapper(self._draw)

    def _draw(self, screen):
        current_grid = LifeGrid(self.pattern)
        curses.curs_set(0)
        screen.clear()

        try:
            screen.addstr(0, 0, current_grid.as_string(self.bbox))
        except curses.error:
            raise ValueError(
                f"Error: terminal too small for pattern '{self.pattern.name}'"
            )

        for _ in range(self.gen):
            current_grid.evolve()
            screen.addstr(0, 0, current_grid.as_string(self.bbox))
            screen.refresh()
            sleep(1 / self.frame_rate)
