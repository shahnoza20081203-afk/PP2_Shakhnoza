from datetime import datetime
from pathlib import Path

import pygame

from tools import draw_shape, flood_fill


WINDOW_W = 1000
WINDOW_H = 700
TOOLBAR_H = 92
STATUS_H = 48

CANVAS_RECT = pygame.Rect(
    12,
    TOOLBAR_H + 10,
    WINDOW_W - 24,
    WINDOW_H - TOOLBAR_H - STATUS_H - 20,
)

BG = (232, 236, 242)
INK = (28, 32, 40)
BUTTON = (250, 251, 253)
ACCENT = (65, 116, 220)

TOOLS = [
    ("pencil", "Pencil"),
    ("line", "Line"),
    ("rectangle", "Rect"),
    ("square", "Square"),
    ("circle", "Circle"),
    ("triangle", "Triangle"),
    ("right_triangle", "Right tri"),
    ("rhombus", "Rhombus"),
    ("eraser", "Eraser"),
    ("fill", "Fill"),
    ("picker", "Picker"),
    ("text", "Text"),
]

PALETTE = [
    (28, 32, 40),
    (220, 55, 65),
    (245, 135, 45),
    (245, 205, 55),
    (45, 165, 95),
    (50, 145, 220),
    (105, 85, 200),
    (235, 90, 165),
    (255, 255, 255),
    (135, 145, 160),
]


class PaintApp:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("SIS 2 Paint")

        self.screen = pygame.display.set_mode((WINDOW_W, WINDOW_H))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 22)
        self.small_font = pygame.font.Font(None, 18)

        self.canvas = pygame.Surface(CANVAS_RECT.size)
        self.canvas.fill("white")

        self.tool = "pencil"
        self.color = pygame.Color(28, 32, 40)
        self.brush = 5

        self.drawing = False
        self.start = None
        self.previous = None

        self.text_active = False
        self.text_position = None
        self.text_value = ""

        self.message = "Ready"

        self.buttons = {}
        self.swatches = []
        self.brush_buttons = {}

        self._layout_toolbar()

    def _layout_toolbar(self):
        x0 = 10
        y0 = 8
        button_w = 82
        button_h = 32
        gap = 5

        for index, (name, _) in enumerate(TOOLS):
            row, col = divmod(index, 6)

            self.buttons[name] = pygame.Rect(
                x0 + col * (button_w + gap),
                y0 + row * (button_h + 5),
                button_w,
                button_h,
            )

        for index, color in enumerate(PALETTE):
            col = index % 5
            row = index // 5
            rect = pygame.Rect(540 + col * 26, 12 + row * 27, 20, 20)
            self.swatches.append((rect, color))

        for index, size in enumerate((2, 5, 10)):
            self.brush_buttons[size] = pygame.Rect(
                690 + index * 52,
                17,
                44,
                30,
            )

        self.save_button = pygame.Rect(860, 17, 120, 30)
        self.clear_button = pygame.Rect(860, 54, 120, 30)

    def _canvas_pos(self, position):
        return (
            position[0] - CANVAS_RECT.x,
            position[1] - CANVAS_RECT.y,
        )

    def _inside_canvas(self, position):
        return CANVAS_RECT.collidepoint(position)

    def _draw_pencil_segment(self, start, end):
        pygame.draw.line(
            self.canvas,
            self.color,
            start,
            end,
            self.brush,
        )

        radius = max(1, self.brush // 2)
        pygame.draw.circle(self.canvas, self.color, start, radius)

    def _save_canvas(self):
        folder = Path("saved_images")
        folder.mkdir(exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
        filename = f"paint_{timestamp}.png"

        pygame.image.save(self.canvas, folder / filename)
        self.message = f"Saved: saved_images/{filename}"

    def _confirm_text(self):
        if self.text_value.strip() and self.text_position:
            image = self.font.render(
                self.text_value,
                True,
                self.color,
            )
            self.canvas.blit(image, self.text_position)

        self.text_active = False
        self.text_position = None
        self.text_value = ""

    def _handle_toolbar_click(self, position):
        for name, rect in self.buttons.items():
            if rect.collidepoint(position):
                self.tool = name
                self.message = f"Tool: {name.replace('_', ' ')}"
                return

        for rect, color in self.swatches:
            if rect.collidepoint(position):
                self.color = pygame.Color(color)
                self.message = "Color selected"
                return

        for size, rect in self.brush_buttons.items():
            if rect.collidepoint(position):
                self.brush = size
                self.message = f"Brush: {size}px"
                return

        if self.save_button.collidepoint(position):
            self._save_canvas()
            return

        if self.clear_button.collidepoint(position):
            self.canvas.fill("white")
            self.message = "Canvas cleared"

    def _mouse_down(self, position):
        if position[1] < TOOLBAR_H:
            self._handle_toolbar_click(position)
            return

        if not self._inside_canvas(position):
            return

        point = self._canvas_pos(position)

        if self.tool == "picker":
            self.color = pygame.Color(self.canvas.get_at(point))
            self.message = "Color picked"

        elif self.tool == "fill":
            flood_fill(self.canvas, point, self.color)
            self.message = "Area filled"

        elif self.tool == "text":
            if self.text_active:
                self._confirm_text()

            self.text_active = True
            self.text_position = point
            self.text_value = ""
            self.message = "Type text; Enter confirms, Escape cancels"

        else:
            self.drawing = True
            self.start = point
            self.previous = point

            if self.tool == "pencil":
                self._draw_pencil_segment(point, point)

            elif self.tool == "eraser":
                radius = max(1, self.brush // 2)
                pygame.draw.circle(
                    self.canvas,
                    "white",
                    point,
                    radius,
                )

    def _mouse_move(self, position):
        if not self.drawing or not self._inside_canvas(position):
            return

        point = self._canvas_pos(position)

        if self.tool == "pencil":
            self._draw_pencil_segment(self.previous, point)
            self.previous = point

        elif self.tool == "eraser":
            pygame.draw.line(
                self.canvas,
                "white",
                self.previous,
                point,
                self.brush,
            )
            pygame.draw.circle(
                self.canvas,
                "white",
                point,
                max(1, self.brush // 2),
            )
            self.previous = point

    def _mouse_up(self, position):
        if not self.drawing:
            return

        self.drawing = False

        if self.tool not in ("pencil", "eraser"):
            if self._inside_canvas(position):
                end = self._canvas_pos(position)
                draw_shape(
                    self.canvas,
                    self.tool,
                    self.color,
                    self.start,
                    end,
                    self.brush,
                )

    def _draw_interface(self):
        self.screen.fill(BG)
        pygame.draw.rect(
            self.screen,
            (216, 222, 232),
            (0, 0, WINDOW_W, TOOLBAR_H),
        )

        for name, label in TOOLS:
            rect = self.buttons[name]
            selected = self.tool == name

            pygame.draw.rect(
                self.screen,
                ACCENT if selected else BUTTON,
                rect,
                border_radius=5,
            )

            text_color = "white" if selected else INK
            label_image = self.small_font.render(
                label,
                True,
                text_color,
            )
            self.screen.blit(label_image, (rect.x + 6, rect.y + 9))

        for rect, color in self.swatches:
            is_selected = pygame.Color(color) == self.color

            pygame.draw.rect(
                self.screen,
                color,
                rect,
                border_radius=3,
            )

            pygame.draw.rect(
                self.screen,
                ACCENT if is_selected else (125, 130, 140),
                rect,
                2 if is_selected else 1,
                border_radius=3,
            )

        brush_label = self.small_font.render("Brush", True, INK)
        self.screen.blit(brush_label, (690, 50))

        for size, rect in self.brush_buttons.items():
            selected = self.brush == size

            pygame.draw.rect(
                self.screen,
                ACCENT if selected else BUTTON,
                rect,
                border_radius=4,
            )

            text_color = "white" if selected else INK
            size_image = self.small_font.render(
                str(size),
                True,
                text_color,
            )
            self.screen.blit(size_image, (rect.x + 16, rect.y + 8))

        for rect, label in (
            (self.save_button, "Save (Ctrl+S)"),
            (self.clear_button, "Clear"),
        ):
            pygame.draw.rect(
                self.screen,
                BUTTON,
                rect,
                border_radius=4,
            )

            label_image = self.small_font.render(label, True, INK)
            self.screen.blit(label_image, (rect.x + 9, rect.y + 8))

        self.screen.blit(self.canvas, CANVAS_RECT.topleft)
        pygame.draw.rect(self.screen, (150, 158, 170), CANVAS_RECT, 1)

        if self.drawing and self.tool not in ("pencil", "eraser"):
            mouse_position = pygame.mouse.get_pos()

            if self._inside_canvas(mouse_position):
                preview = self.canvas.copy()

                draw_shape(
                    preview,
                    self.tool,
                    self.color,
                    self.start,
                    self._canvas_pos(mouse_position),
                    self.brush,
                )

                self.screen.blit(preview, CANVAS_RECT.topleft)

        if self.text_active:
            preview_text = self.font.render(
                self.text_value + "|",
                True,
                self.color,
            )

            self.screen.blit(
                preview_text,
                (
                    CANVAS_RECT.x + self.text_position[0],
                    CANVAS_RECT.y + self.text_position[1],
                ),
            )

        pygame.draw.rect(
            self.screen,
            (216, 222, 232),
            (0, WINDOW_H - STATUS_H, WINDOW_W, STATUS_H),
        )

        help_text = (
            "1/2/3: brush 2/5/10px   "
            "Ctrl+S: save   "
            "Enter: confirm text   "
            "Esc: cancel text"
        )

        self.screen.blit(
            self.small_font.render(help_text, True, INK),
            (12, WINDOW_H - 39),
        )

        self.screen.blit(
            self.small_font.render(self.message[:115], True, (65, 75, 90)),
            (12, WINDOW_H - 18),
        )

        pygame.display.flip()

    def run(self):
        running = True

        while running:
            self.clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE and self.text_active:
                        self.text_active = False
                        self.text_value = ""
                        self.message = "Text cancelled"

                    elif self.text_active:
                        if event.key in (
                            pygame.K_RETURN,
                            pygame.K_KP_ENTER,
                        ):
                            self._confirm_text()
                            self.message = "Text placed"

                        elif event.key == pygame.K_BACKSPACE:
                            self.text_value = self.text_value[:-1]

                        elif event.unicode and event.unicode.isprintable():
                            self.text_value += event.unicode

                    elif event.key == pygame.K_ESCAPE:
                        running = False

                    elif (
                        event.key == pygame.K_s
                        and event.mod & pygame.KMOD_CTRL
                    ):
                        self._save_canvas()

                    elif event.unicode in ("1", "2", "3"):
                        self.brush = {
                            "1": 2,
                            "2": 5,
                            "3": 10,
                        }[event.unicode]
                        self.message = f"Brush: {self.brush}px"

                elif (
                    event.type == pygame.MOUSEBUTTONDOWN
                    and event.button == 1
                ):
                    self._mouse_down(event.pos)

                elif event.type == pygame.MOUSEMOTION:
                    self._mouse_move(event.pos)

                elif (
                    event.type == pygame.MOUSEBUTTONUP
                    and event.button == 1
                ):
                    self._mouse_up(event.pos)

            self._draw_interface()

        pygame.quit()


if __name__ == "__main__":
    PaintApp().run()