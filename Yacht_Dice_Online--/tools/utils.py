import pygame
import pygame.gfxdraw

# 안이 비어있는 둥근 사각형을 그린다
def emptyRoundRect(surf, color, rect, radius=10, border=2, incolor=(0, 0, 0)):
    if min(rect[2], rect[3]) > 2 * (radius + border):
        solidRoundRect(surf, color, rect, radius)
        rect = (rect[0] + border, rect[1] + border, rect[2] -2*border, rect[3] - 2*border)
        solidRoundRect(surf, incolor, rect, radius)

# 안이 차 있는 둥근 사각형을 그린다
def solidRoundRect(surf, color, rect, r):
    for x, y in [(rect[0] + r, rect[1] + r),
                (rect[0] + rect[2] - r - 1, rect[1] + r),
                (rect[0] + r, rect[1] + rect[3] - r - 1),
                (rect[0] + rect[2] - r - 1, rect[1] + rect[3] - r - 1)]:
        pygame.gfxdraw.aacircle(surf, x, y, r, color)
        pygame.gfxdraw.filled_circle(surf, x, y, r, color)

    pygame.draw.rect(surf, color, (rect[0] + r, rect[1], rect[2] - 2*r, rect[3]))
    pygame.draw.rect(surf, color, (rect[0], rect[1] + r, rect[2], rect[3] - 2*r))

    