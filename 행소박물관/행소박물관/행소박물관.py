from graphics import *

# -----------------------------
# 좌표 및 기본 도형 함수
# -----------------------------

def map_coord(x, y):
    """160×100 좌표계를 800×500 graphics 좌표계로 변환"""
    return Point(x * 5, 500 - y * 5)


def draw_rect(win, x, y, w, h, fill_color, outline_color=None):
    left = x * 5
    top = 500 - (y + h) * 5
    right = (x + w) * 5
    bottom = 500 - y * 5

    rect = Rectangle(Point(left, top), Point(right, bottom))
    rect.setFill(fill_color)

    if outline_color:
        rect.setOutline(outline_color)
    else:
        rect.setOutline(fill_color)

    rect.draw(win)


def draw_oval(win, cx, cy, w, h, fill_color):
    center = map_coord(cx, cy)

    rx = (w / 2) * 5
    ry = (h / 2) * 5

    oval = Oval(
        Point(center.getX() - rx, center.getY() - ry),
        Point(center.getX() + rx, center.getY() + ry)
    )

    oval.setFill(fill_color)
    oval.setOutline(fill_color)
    oval.draw(win)


def draw_line(win, x1, y1, x2, y2, color, width=1):
    line = Line(map_coord(x1, y1), map_coord(x2, y2))
    line.setFill(color)
    line.setWidth(width)
    line.draw(win)


# -----------------------------
# 메인 프로그램
# -----------------------------

def main():

    win = GraphWin("University Museum", 800, 500)
    win.setBackground(color_rgb(135, 206, 235))

    # -------------------------
    # 배경
    # -------------------------

    # 하늘
    for i in range(40):
        c = color_rgb(
            int((0.53 + i * 0.005) * 255),
            int((0.81 - i * 0.003) * 255),
            int((0.98 - i * 0.005) * 255)
        )
        draw_rect(win, 0, 60 + i, 160, 1.5, c, c)

    # 잔디
    draw_rect(win, 0, 0, 160, 38, color_rgb(106, 170, 74))

    # 도로
    draw_rect(win, 0, 0, 160, 28, color_rgb(136, 136, 136))

    # -------------------------
    # 건물
    # -------------------------

    # 본관 건물
    draw_rect(win, 5, 38, 150, 32,
              color_rgb(139, 58, 58))

    # 지붕
    roof_bg = Polygon(
        map_coord(5, 70),
        map_coord(25, 78),
        map_coord(135, 78),
        map_coord(155, 70)
    )

    roof_bg.setFill(color_rgb(90, 90, 90))
    roof_bg.setOutline(color_rgb(70, 70, 70))
    roof_bg.draw(win)

    # 좌우 기둥
    draw_rect(win, 43, 38, 10, 36,
              color_rgb(232, 224, 208))

    draw_rect(win, 107, 38, 10, 36,
              color_rgb(232, 224, 208))

    # 중앙 본관
    draw_rect(win, 61, 38, 38, 46.4,
              color_rgb(232, 224, 208))

    center_tri = Polygon(
        map_coord(61, 84.4),
        map_coord(99, 84.4),
        map_coord(80, 99.8)
    )

    center_tri.setFill(color_rgb(232, 224, 208))
    center_tri.setOutline(color_rgb(170, 160, 144))
    center_tri.draw(win)

    draw_line(
        win,
        61, 84.4,
        99, 84.4,
        color_rgb(170, 160, 144),
        3
    )

    # 외벽 장식 띠
    for rx, rw in [(5, 38), (117, 38)]:
        draw_rect(
            win,
            rx, 51.15,
            rw, 2.4,
            color_rgb(232, 224, 208)
        )

    # -------------------------
    # 창문
    # -------------------------

    # 중앙 양옆 벽 창문
    for wx in [54, 58, 100, 104]:

        draw_rect(
            win,
            wx - 0.5, 38,
            3, 5,
            color_rgb(122, 154, 170)
        )

        draw_rect(
            win,
            wx - 0.5, 58.1,
            3, 1.2,
            color_rgb(232, 224, 208)
        )

        draw_rect(
            win,
            wx - 0.5, 59.3,
            3, 5,
            color_rgb(122, 154, 170)
        )

        tri = Polygon(
            map_coord(wx - 0.5, 64.3),
            map_coord(wx + 2.5, 64.3),
            map_coord(wx + 1, 65.5)
        )

        tri.setFill(color_rgb(232, 224, 208))
        tri.setOutline(color_rgb(232, 224, 208))
        tri.draw(win)

    # 좌측 창문
    for wx, ax in zip(
        [17, 21, 26.5, 30.5, 36, 40],
        [17, 17, 26.5, 26.5, 36, 36]
    ):

        if wx in [17, 26.5, 36]:

            draw_rect(
                win,
                ax, 38,
                6, 8,
                color_rgb(122, 154, 170)
            )

            draw_oval(
                win,
                ax + 3, 46,
                6, 6,
                color_rgb(122, 154, 170)
            )

            draw_rect(
                win,
                ax - 0.5, 38,
                7, 11.5,
                "",
                color_rgb(122, 85, 85)
            )

        draw_rect(
            win,
            wx - 0.5, 58.1,
            3, 1.2,
            color_rgb(232, 224, 208)
        )

        draw_rect(
            win,
            wx - 0.5, 59.3,
            3, 5,
            color_rgb(122, 154, 170)
        )

        tri = Polygon(
            map_coord(wx - 0.5, 64.3),
            map_coord(wx + 2.5, 64.3),
            map_coord(wx + 1, 65.5)
        )

        tri.setFill(color_rgb(232, 224, 208))
        tri.setOutline(color_rgb(232, 224, 208))
        tri.draw(win)

    # 우측 창문
    for wx, ax in zip(
        [118, 122, 127.5, 131.5, 137, 141],
        [118, 118, 127.5, 127.5, 137, 137]
    ):

        if wx in [118, 127.5, 137]:

            draw_rect(
                win,
                ax, 38,
                6, 8,
                color_rgb(122, 154, 170)
            )

            draw_oval(
                win,
                ax + 3, 46,
                6, 6,
                color_rgb(122, 154, 170)
            )

            draw_rect(
                win,
                ax - 0.5, 38,
                7, 11.5,
                "",
                color_rgb(122, 85, 85)
            )

        draw_rect(
            win,
            wx - 0.5, 58.1,
            3, 1.2,
            color_rgb(232, 224, 208)
        )

        draw_rect(
            win,
            wx - 0.5, 59.3,
            3, 5,
            color_rgb(122, 154, 170)
        )

        tri = Polygon(
            map_coord(wx - 0.5, 64.3),
            map_coord(wx + 2.5, 64.3),
            map_coord(wx + 1, 65.5)
        )

        tri.setFill(color_rgb(232, 224, 208))
        tri.setOutline(color_rgb(232, 224, 208))
        tri.draw(win)

    # 기둥 창문
    for wx in [45.5, 49.5]:
        draw_rect(win, wx - 0.5, 38, 3, 5,
                  color_rgb(122, 154, 170))
        draw_rect(win, wx - 0.5, 59.3, 3, 5,
                  color_rgb(122, 154, 170))

    for wx in [109.5, 113.5]:
        draw_rect(win, wx - 0.5, 38, 3, 5,
                  color_rgb(122, 154, 170))
        draw_rect(win, wx - 0.5, 59.3, 3, 5,
                  color_rgb(122, 154, 170))

    # 중앙 창문
    window_color = color_rgb(122, 154, 170)

    draw_rect(win, 73, 74, 4, 6, window_color)
    draw_rect(win, 78, 74, 4, 6, window_color)
    draw_rect(win, 83, 74, 4, 6, window_color)

    # -------------------------
    # 현관
    # -------------------------

    door_color = color_rgb(90, 90, 90)

    draw_rect(win, 63.5, 38, 7, 16, door_color)
    draw_rect(win, 73, 38, 14, 32, door_color)
    draw_rect(win, 89.5, 38, 7, 16, door_color)

    # 계단
    stair_colors = [
        color_rgb(208, 200, 184),
        color_rgb(200, 192, 176),
        color_rgb(192, 184, 168),
        color_rgb(184, 176, 160),
        color_rgb(176, 168, 152)
    ]

    for i, color in enumerate(stair_colors):
        draw_rect(
            win,
            53 + i * 2,
            33 + i,
            54 - i * 4,
            2,
            color
        )

    # -------------------------
    # 제목
    # -------------------------

    title = Text(map_coord(80, 16), "행소박물관")
    title.setSize(20)
    title.setTextColor("white")
    title.setStyle("bold")
    title.draw(win)

    sub_title = Text(
        map_coord(80, 11),
        "Hengso Museum of Keimyung University"
    )

    sub_title.setSize(12)
    sub_title.setTextColor(color_rgb(230, 230, 230))
    sub_title.draw(win)

    win.getMouse()
    win.close()


if __name__ == '__main__':
    main()