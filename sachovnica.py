import PIL
from PIL import Image, ImageDraw

chessboard = []
counter = 0


def createchessboard():
    global chessboard
    # chessboard = [row] * 8
    for i in range(8):
        row = [0] * 8
        chessboard.append(row)


def chceckit(x, y):
    for i in range(0, 8):
        if chessboard[y][i] == 1:
            return False
        if chessboard[i][x] == 1:
            return False
    for i in range(0, 8):
        for j in range(0, 8):
            if i + j == y + x:
                if chessboard[i][j] == 1:
                    return False
            if i - j == y - x:
                if chessboard[i][j] == 1:
                    return False
    return True


def queens(n):
    global chessboard
    global counter
    if n == 8:
        createImage()
        print(chessboard)
        counter += 1
        print('-------------------------------------------------')
    else:
        for i in range(0, 8):
            if chceckit(i, n):
                chessboard[n][i] = 1
                queens(n + 1)
                chessboard[n][i] = 0


def createImage():
    img = Image.new('RGB',(1600, 1600), "white")
    draw = ImageDraw.Draw(img)
    for i in range(0, 1601, 200):
        for j in range(0, 1601, 200):
            if (i + j) % 400 == 0:
                draw.rectangle([i, j, i + 200, j + 200], fill='black')
    for row in range(8):
        for col in range(8):
            if chessboard[row][col] == 1:
                draw.ellipse(((col * 200)+30, (row *200)+30 , (col*200) + 200 - 30, (row*200) + 200- 30), fill='red')

    img.save('chessboard3.png')


createchessboard()
queens(0)
print(counter)