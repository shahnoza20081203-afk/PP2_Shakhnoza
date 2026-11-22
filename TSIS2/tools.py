import math
import pygame


def flood_fill(surface, start, fill_color):
    """Заливает связную область пикселей выбранным цветом."""
    width, height = surface.get_size()
    start_x, start_y = start

    if not (0 <= start_x < width and 0 <= start_y < height):
        return

    fill_color = pygame.Color(fill_color)
    target_color = surface.get_at((start_x, start_y))

    if target_color == fill_color:
        return

    visited = bytearray(width * height)
    stack = [(start_x, start_y)]

    while stack:
        x, y = stack.pop()

        if not (0 <= x < width and 0 <= y < height):
            continue

        index = y * width + x

        if visited[index]:
            continue

        visited[index] = 1

        if surface.get_at((x, y)) != target_color:
            continue

        surface.set_at((x, y), fill_color)

        stack.append((x + 1, y))
        stack.append((x - 1, y))
        stack.append((x, y + 1))
        stack.append((x, y - 1))


def shape_rect(start, end, square=False):
    """Возвращает прямоугольник между начальной и конечной точками."""
    x1, y1 = start
    x2, y2 = end

    if square:
        side = max(abs(x2 - x1), abs(y2 - y1))
        x2 = x1 + side if x2 >= x1 else x1 - side
        y2 = y1 + side if y2 >= y1 else y1 - side

    left, right = sorted((x1, x2))
    top, bottom = sorted((y1, y2))

    return pygame.Rect(
        left,
        top,
        max(1, right - left),
        max(1, bottom - top),
    )


def draw_shape(surface, tool, color, start, end, width):
    """Рисует геометрическую фигуру активным цветом и толщиной кисти."""
    color = pygame.Color(color)
    rect = shape_rect(start, end, square=(tool == "square"))

    if tool in ("rectangle", "square"):
        pygame.draw.rect(surface, color, rect, width)

    elif tool == "circle":
        radius = max(1, round(math.hypot(rect.width, rect.height) / 2))
        pygame.draw.circle(surface, color, rect.center, radius, width)

    elif tool == "triangle":
        # Равносторонний треугольник.
        side = max(
            1,
            min(rect.width, round(rect.height * 2 / math.sqrt(3))),
        )
        height = max(1, round(side * math.sqrt(3) / 2))

        points = [
            (rect.centerx, rect.centery - height // 2),
            (rect.centerx - side // 2, rect.centery + height // 2),
            (rect.centerx + side // 2, rect.centery + height // 2),
        ]

        pygame.draw.polygon(surface, color, points, width)

    elif tool == "right_triangle":
        points = [
            (rect.left, rect.top),
            (rect.left, rect.bottom),
            (rect.right, rect.bottom),
        ]

        pygame.draw.polygon(surface, color, points, width)

    elif tool == "rhombus":
        points = [
            (rect.centerx, rect.top),
            (rect.right, rect.centery),
            (rect.centerx, rect.bottom),
            (rect.left, rect.centery),
        ]

        pygame.draw.polygon(surface, color, points, width)

    elif tool == "line":
        pygame.draw.line(surface, color, start, end, width)