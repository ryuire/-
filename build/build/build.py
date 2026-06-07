from graphics import *

# ──────────────────────────────────────────
# 좌표 변환
# ──────────────────────────────────────────
def map_coord(x, y):
    return Point(x * 5, 500 - y * 5)

def to_logic(px, py):
    return px / 5, (500 - py) / 5

def draw_rect(win, x, y, w, h, fill_color, outline_color=None):
    rect = Rectangle(Point(x*5, 500-(y+h)*5), Point((x+w)*5, 500-y*5))
    rect.setFill(fill_color)
    rect.setOutline(outline_color if outline_color else fill_color)
    rect.draw(win)

def draw_oval(win, cx, cy, w, h, fill_color):
    center = map_coord(cx, cy)
    rx = (w/2)*5; ry = (h/2)*5
    oval = Oval(Point(center.getX()-rx, center.getY()-ry),
                Point(center.getX()+rx, center.getY()+ry))
    oval.setFill(fill_color); oval.setOutline(fill_color); oval.draw(win)

# ──────────────────────────────────────────
# 고정 배경
# ──────────────────────────────────────────
def draw_fixed(win):
    # 하늘
    for i in range(40):
        c = color_rgb(int((0.53+i*0.005)*255),
                      int((0.81-i*0.003)*255),
                      int((0.98-i*0.005)*255))
        draw_rect(win, 0, 60+i, 160, 1.5, c, c)
    # 잔디
    draw_rect(win, 0, 0, 160, 38, color_rgb(106,170,74))
    # 도로
    draw_rect(win, 0, 0, 160, 28, color_rgb(136,136,136))
    # 빨간 본관 벽체
    draw_rect(win, 5, 38, 150, 32, color_rgb(139,58,58))
    # 지붕
    roof = Polygon(map_coord(5,70), map_coord(25,78),
                   map_coord(135,78), map_coord(155,70))
    roof.setFill(color_rgb(90,90,90)); roof.setOutline(color_rgb(70,70,70)); roof.draw(win)

# ──────────────────────────────────────────
# 팔레트 도형들
# ──────────────────────────────────────────

# 창문: 파란 직사각형
def place_window(win, cx, cy):
    draw_rect(win, cx-1.5, cy, 3, 5, color_rgb(122,154,170))

# 창문3: 아치형 
def place_window3(win, cx, cy):
    draw_rect(win, cx-3, cy, 6, 8, color_rgb(122,154,170))
    draw_oval(win, cx, cy+8, 6, 6, color_rgb(122,154,170))
    r = Rectangle(Point((cx-3.5)*5, 500-(cy+11.5)*5), Point((cx+3.5)*5, 500-cy*5))
    r.setFill(""); r.setOutline(color_rgb(122,85,85)); r.draw(win)

# 흰 기둥
def place_column(win, cx, cy):
    draw_rect(win, cx-5, cy, 10, 36, color_rgb(232,224,208))

# 중앙 본관 + 페디먼트 + 현관 3개 + 상단 창문 3개 포함
def place_pediment(win, cx, cy):
    # 중앙 직사각형
    draw_rect(win, cx-19, cy, 38, 46.4, color_rgb(232,224,208))
    # 삼각형 페디먼트
    tri = Polygon(map_coord(cx-19, cy+46.4),
                  map_coord(cx+19, cy+46.4),
                  map_coord(cx,    cy+61.8))
    tri.setFill(color_rgb(232,224,208)); tri.setOutline(color_rgb(170,160,144)); tri.draw(win)
    # 페디먼트 아랫선
    l = Line(map_coord(cx-19, cy+46.4), map_coord(cx+19, cy+46.4))
    l.setFill(color_rgb(170,160,144)); l.setWidth(3); l.draw(win)
    # 외벽 장식 띠 좌우
    draw_rect(win, cx-19, cy+13.15, 19, 2.4, color_rgb(232,224,208))
    draw_rect(win, cx,    cy+13.15, 19, 2.4, color_rgb(232,224,208))
    # 현관 입구 3개 (회색 직사각형) — museum.py 기준 cx=80 기준
    draw_rect(win, cx-16.5, cy,  7, 16, color_rgb(90,90,90))  # 좌
    draw_rect(win, cx- 7,   cy, 14, 32, color_rgb(90,90,90))  # 중앙
    draw_rect(win, cx+ 9.5, cy,  7, 16, color_rgb(90,90,90))  # 우
    # 상단 창문 3개 (파란 직사각형)
    for ox in [-5, 0, 5]:
        draw_rect(win, cx+ox-2, cy+36, 4, 6, color_rgb(122,154,170))

# 계단: i=0이 맨 아래(가장 넓음), i=4가 맨 위(가장 좁음)
# cy = 계단 맨 아래 y좌표
def place_stairs(win, cx, cy):
    sc = [color_rgb(208,200,184), color_rgb(200,192,176), color_rgb(192,184,168),
          color_rgb(184,176,160), color_rgb(176,168,152)]
    for i, c in enumerate(sc):
        w = (54 - i*4) / 2
        # i=0 맨 아래 넓음, 위로 갈수록 좁아짐
        draw_rect(win, cx-w, cy+i*2, w*2, 2, c)

# ──────────────────────────────────────────
# 팔레트 정의
# ──────────────────────────────────────────
PALETTE = [
    ("창문1",       "파란 직사각형 창",      place_window),
    ("창문2",      "아치형 창문",           place_window3),
    ("흰 기둥",    "좌우 기둥",             place_column),
    ("중앙",  "현관/창문 포함 중앙부", place_pediment),
    ("계단",       "현관 앞 계단",      place_stairs),
]

PANEL_W  = 160
CANVAS_W = 800
WIN_W    = CANVAS_W + PANEL_W
WIN_H    = 500
ITEM_H   = WIN_H // len(PALETTE)

# ──────────────────────────────────────────
# 팔레트 패널
# ──────────────────────────────────────────
def draw_palette(win, selected, placed):
    for i, (name, desc, _) in enumerate(PALETTE):
        y0 = i * ITEM_H
        y1 = y0 + ITEM_H
        pcx = CANVAS_W + PANEL_W // 2
        pcy = (y0 + y1) // 2

        if i in placed:
            bg_col = color_rgb(30,80,40)
        elif i == selected:
            bg_col = color_rgb(50,100,200)
        else:
            bg_col = color_rgb(25,25,45)

        bg = Rectangle(Point(CANVAS_W, y0), Point(WIN_W, y1))
        bg.setFill(bg_col); bg.setOutline(color_rgb(55,55,85)); bg.draw(win)

        mark = "✓ " if i in placed else ("▶ " if i == selected else "  ")
        t = Text(Point(pcx, pcy-10), mark + name)
        t.setSize(10); t.setStyle("bold"); t.setTextColor("white"); t.draw(win)

        d = Text(Point(pcx, pcy+8), desc)
        d.setSize(8)
        tc = color_rgb(160,220,255) if i==selected else (color_rgb(100,180,100) if i in placed else color_rgb(110,110,130))
        d.setTextColor(tc); d.draw(win)

    sep = Line(Point(CANVAS_W,0), Point(CANVAS_W,WIN_H))
    sep.setFill(color_rgb(80,80,130)); sep.setWidth(2); sep.draw(win)

# ──────────────────────────────────────────
# 메인
# ──────────────────────────────────────────
def main():
    win = GraphWin("행소박물관 - 직접 그려보기", WIN_W, WIN_H)
    win.setBackground(color_rgb(135,206,235))

    draw_fixed(win)
    draw_palette(win, 0, set())

    guide = Text(Point(CANVAS_W//2, 14),
                 "오른쪽 팔레트 선택 후 캔버스 클릭! 클릭 위치가 도형 기준점입니다.")
    guide.setSize(9); guide.setStyle("bold")
    guide.setTextColor(color_rgb(255,255,180)); guide.draw(win)

    selected = 0
    placed   = set()

    while True:
        click = win.getMouse()
        if click is None:
            break

        px, py = click.getX(), click.getY()

        # 팔레트 클릭
        if px >= CANVAS_W:
            i = int(py // ITEM_H)
            if 0 <= i < len(PALETTE):
                selected = i
                draw_palette(win, selected, placed)
        # 캔버스 클릭 → 배치
        else:
            lx, ly = to_logic(px, py)
            PALETTE[selected][2](win, lx, ly)
            placed.add(selected)

            if len(placed) == len(PALETTE):
                guide.undraw()
                done = Text(Point(CANVAS_W//2, WIN_H//2),
                            "완성! museum.py 와 비교해보세요 :)")
                done.setSize(16); done.setStyle("bold")
                done.setTextColor(color_rgb(255,230,50)); done.draw(win)
                win.getMouse(); break

            for j in range(len(PALETTE)):
                if j not in placed:
                    selected = j
                    break
            draw_palette(win, selected, placed)

    win.close()

if __name__ == '__main__':
    main()
