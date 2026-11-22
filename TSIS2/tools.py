import math
import pygame

def flood_fill(surface, start, fill_color):
    width, height = surface.get_size()
    start_x, start_y = start

    if not (0 <= start_x < width and 0 <= start_y < height):
        return

    target_color = surface.get_at((start_x, start_y))

    if target_color == fill_color:
        return

    pixels = surface.get_size()
    visited = bytearray(pixels[0] * pixels[1])
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


def shape_rect(start, end, tool):
    x1, y1 = start
    x2, y2 = end

    if tool == "square":
        side = max(abs(x2 - x1), abs(y2 - y1))
        x2 = x1 + side if x2 >= x1 else x1 - side
        y2 = y1 + side if y2 >= y1 else y1 - side

    return pygame.Rect(x1, y1, x2 - x1, y2 - y1).normalize()


def draw_shape(surface, tool, color, start, end, width):
    rect = shape_rect(start, end, tool)

    if tool in ("rectangle", "square"):
        pygame.draw.rect(surface, color, rect, width)

    elif tool == "circle":
        center = rect.center
        radius = max(1, int(math.hypot(rect.width, rect.height) / 2))
        pygame.draw.circle(surface, color, center, radius, width)

    elif tool == "triangle":
        points = [
            (rect.centerx, rect.top),
            (rect.left, rect.bottom),
            (rect.right, rect.bottom),
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