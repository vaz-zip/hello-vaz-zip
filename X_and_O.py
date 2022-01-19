def rul_game():
    print("$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("$       ! ИГРА !        $")
    print("$  !КРЕСТИКИ И НОЛИКИ!  $")
    print("$   задай  координаты   $")
    print("$   клетки,на которую   $")
    print("$     будешь ходить     $")
    print("$   x - горизонталь     $")
    print("$   y - вертикаль       $")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$")


def field_screen():
    print()
    print("   | 0 | 1 | 2 |")
    print("----------------")
    for i, row in enumerate(playing_field):
        row_str = f"{i}  | {' | '.join(row)} |"
        print(row_str)
        print("----------------")


def coordinates():
    while True:
        coord = input("Ходите!!!: ").split()

        if len(coord) != 2:
            print(" Введите 2 координаты! ")
            continue

        x, y = coord

        if not (x.isdigit()) or not (y.isdigit()):
            print(" Ввод координат! ")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print(" Координаты за пределом поля! ")
            continue

        if playing_field[x][y] != " ":
            print(" Клетка занята! ")
            continue

        return x, y


def check_win():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        sign = []
        for c in cord:
            sign.append(playing_field[c[0]][c[1]])
        if sign == ["X", "X", "X"]:
            print("Победил Х КРЕСТИК Х!!!")
            return True
        if sign == ["0", "0", "0"]:
            print("Победил 0 НОЛИК 0!!!")
            return True
    return False


rul_game()
playing_field = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]

]
count = 0
while True:
    count += 1
    field_screen()
    if count % 2 == 1:
        print("Ход: 'X'")
    else:
        print("Ход: '0'")

    x, y = coordinates()

    if count % 2 == 1:
        playing_field[x][y] = "X"
    else:
        playing_field[x][y] = "0"

    if check_win():
        break

    if count == 9:
        print(" Ничья!")
        break
