import turtle

# РЎРѕР·РґР°РµРј СЌРєСЂР°РЅ РґР»СЏ СЂРёСЃРѕРІР°РЅРёСЏ
screen = turtle.Screen()
screen.bgcolor("white")


# РћР±Р»РѕРєРѕ 1
def draw_sky():
    turtle.color("skyblue")
    turtle.begin_fill()
    turtle.forward(800)
    turtle.right(90)
    turtle.forward(250)
    turtle.right(90)
    turtle.forward(1600)
    turtle.right(90)
    turtle.forward(250)
    turtle.right(90)
    turtle.forward(800)
    turtle.end_fill()


def draw_cloud():
    turtle.penup()
    turtle.goto(-200, 200)
    turtle.pendown()
    turtle.color("white")
    turtle.begin_fill()
    turtle.circle(30)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(-170, 220)
    turtle.pendown()
    turtle.color("white")
    turtle.begin_fill()
    turtle.circle(40)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(-130, 210)
    turtle.pendown()
    turtle.color("white")
    turtle.begin_fill()
    turtle.circle(30)
    turtle.end_fill()


# РѕР±Р»РѕРєРѕ 2
def draw_sky2():
    turtle.color("skyblue")
    turtle.begin_fill()
    turtle.forward(800)
    turtle.right(90)
    turtle.forward(250)
    turtle.right(90)
    turtle.forward(1600)
    turtle.right(90)
    turtle.forward(250)
    turtle.right(90)
    turtle.forward(800)
    turtle.end_fill()


def draw_cloud2():
    turtle.penup()
    turtle.goto(200, 230)
    turtle.pendown()
    turtle.color("white")
    turtle.begin_fill()
    turtle.circle(30)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(230, 250)
    turtle.pendown()
    turtle.color("white")
    turtle.begin_fill()
    turtle.circle(40)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(270, 240)
    turtle.pendown()
    turtle.color("white")
    turtle.begin_fill()
    turtle.circle(30)
    turtle.end_fill()


# РЎРѕР»РЅС†Рµ
def draw_sun():
    turtle.penup()
    turtle.goto(-600, 400)
    turtle.pendown()
    turtle.color("yellow")
    turtle.begin_fill()
    for _ in range(36):
        turtle.forward(200)
        turtle.right(170)
    turtle.end_fill()


# РЈСЃС‚Р°РЅРѕРІРєР° РЅР°С‡Р°Р»СЊРЅС‹С… РїР°СЂР°РјРµС‚СЂРѕРІ
turtle.speed(0)
turtle.hideturtle()
turtle.bgcolor("lightblue")

# Р’С‹РІРѕРґ СЂРёСЃСѓРЅРєРѕРІ РІ РЅСѓР¶РЅРѕРј РїРѕСЂСЏРґРєРµ
draw_sky()
draw_sun()
draw_cloud()
draw_cloud2()

# Р”РѕСЂРѕРіР°
turtle.penup()
turtle.goto(-400, -450)
turtle.pendown()
turtle.color("grey")
turtle.begin_fill()
turtle.forward(1300)
turtle.right(90)
turtle.forward(200)
turtle.right(90)
turtle.forward(2000)
turtle.right(90)
turtle.forward(200)
turtle.end_fill()

# (РџРµСЂРІС‹Р№ РґРѕРј) РџРµСЂРІР°СЏ С‡Р°СЃС‚СЊ РґРѕРјР°
pen = turtle.Turtle()
pen.penup()
pen.goto(-100, -450)
pen.pendown()
pen.fillcolor("grey")
pen.begin_fill()
for _ in range(4):
    pen.forward(200)
    pen.left(90)
pen.end_fill()

# Р’С‚РѕСЂР°СЏ С‡Р°СЃС‚СЊ РґРѕРјР°
pen = turtle.Turtle()
pen.penup()
pen.goto(-100, -250)
pen.pendown()
pen.fillcolor("grey")
pen.begin_fill()
for _ in range(4):
    pen.forward(200)
    pen.left(90)
pen.end_fill()

# РѕРєРЅРѕ 1
pen.penup()
pen.goto(-75, -400)
pen.pendown()
pen.fillcolor("white")
pen.begin_fill()
for _ in range(2):
    pen.forward(50)
    pen.left(90)
    pen.forward(75)
    pen.left(90)
pen.end_fill()

# РѕРєРЅРѕ 2
pen.penup()
pen.goto(-75, -200)
pen.pendown()
pen.fillcolor("white")
pen.begin_fill()
for _ in range(2):
    pen.forward(50)
    pen.left(90)
    pen.forward(75)
    pen.left(90)
pen.end_fill()

# РѕРєРЅРѕ 3
pen.penup()
pen.goto(20, -200)
pen.pendown()
pen.fillcolor("white")
pen.begin_fill()
for _ in range(2):
    pen.forward(50)
    pen.left(90)
    pen.forward(75)
    pen.left(90)
pen.end_fill()

# РѕРєРЅРѕ 4
pen.penup()
pen.goto(20, -400)
pen.pendown()
pen.fillcolor("white")
pen.begin_fill()
for _ in range(2):
    pen.forward(50)
    pen.left(90)
    pen.forward(75)
    pen.left(90)
pen.end_fill()

# (Р’С‚РѕСЂРѕР№ РґРѕРј) РџРµСЂРІР°СЏ С‡Р°СЃС‚СЊ РґРѕРјР°
pen = turtle.Turtle()
pen.penup()
pen.goto(130, -450)
pen.pendown()
pen.fillcolor("grey")
pen.begin_fill()
for _ in range(4):
    pen.forward(200)
    pen.left(90)
pen.end_fill()

# Р’С‚РѕСЂР°СЏ С‡Р°СЃС‚СЊ РґРѕРјР°
pen = turtle.Turtle()
pen.penup()
pen.goto(130, -250)
pen.pendown()
pen.fillcolor("grey")
pen.begin_fill()
for _ in range(4):
    pen.forward(200)
    pen.left(90)
pen.end_fill()

# РўСЂРµС‚СЊСЏ С‡Р°СЃС‚СЊ РґРѕРјР°
pen = turtle.Turtle()
pen.penup()
pen.goto(130, -50)
pen.pendown()
pen.fillcolor("grey")
pen.begin_fill()
for _ in range(4):
    pen.forward(200)
    pen.left(90)
pen.end_fill()

# РѕРєРЅРѕ 1
pen.penup()
pen.goto(155, -400)
pen.pendown()
pen.fillcolor("white")
pen.begin_fill()
for _ in range(2):
    pen.forward(50)
    pen.left(90)
    pen.forward(75)
    pen.left(90)
pen.end_fill()

# РѕРєРЅРѕ 2
pen.penup()
pen.goto(155, -200)
pen.pendown()
pen.fillcolor("white")
pen.begin_fill()
for _ in range(2):
    pen.forward(50)
    pen.left(90)
    pen.forward(75)
    pen.left(90)
pen.end_fill()

# РѕРєРЅРѕ 3
pen.penup()
pen.goto(250, -200)
pen.pendown()
pen.fillcolor("white")
pen.begin_fill()
for _ in range(2):
    pen.forward(50)
    pen.left(90)
    pen.forward(75)
    pen.left(90)
pen.end_fill()

# РѕРєРЅРѕ 4
pen.penup()
pen.goto(250, -400)
pen.pendown()
pen.fillcolor("white")
pen.begin_fill()
for _ in range(2):
    pen.forward(50)
    pen.left(90)
    pen.forward(75)
    pen.left(90)
pen.end_fill()

# РѕРєРЅРѕ 5
pen.penup()
pen.goto(250, 0)
pen.pendown()
pen.fillcolor("white")
pen.begin_fill()
for _ in range(2):
    pen.forward(50)
    pen.left(90)
    pen.forward(75)
    pen.left(90)
pen.end_fill()

# РѕРєРЅРѕ 6
pen.penup()
pen.goto(155, 0)
pen.pendown()
pen.fillcolor("white")
pen.begin_fill()
for _ in range(2):
    pen.forward(50)
    pen.left(90)
    pen.forward(75)
    pen.left(90)
pen.end_fill()

# РњР°РіР°Р·РёРЅ
pen = turtle.Turtle()
pen.penup()
pen.goto(360, -450)
pen.pendown()
pen.fillcolor("green")
pen.begin_fill()
for _ in range(4):
    pen.forward(200)
    pen.left(90)
pen.end_fill()

pen.penup()
pen.goto(360, -300)
pen.pendown()
pen.fillcolor("purple")
pen.begin_fill()
for _ in range(2):
    pen.forward(200)
    pen.left(90)
    pen.forward(50)
    pen.left(90)
pen.end_fill()

# РџРѕР»РѕСЃР° СЂР°Р·РґРµР»РµРЅРёСЏ
pen.penup()
pen.goto(600, -500)
pen.pendown()
pen.fillcolor("white")
pen.begin_fill()
for _ in range(2):
    pen.forward(40)
    pen.left(90)
    pen.forward(10)
    pen.left(90)
pen.end_fill()

pen.penup()
pen.goto(550, -500)
pen.pendown()
pen.fillcolor("white")
pen.begin_fill()
for _ in range(2):
    pen.forward(40)
    pen.left(90)
    pen.forward(10)
    pen.left(90)
pen.end_fill()

pen.penup()
pen.goto(500, -500)
pen.pendown()
pen.fillcolor("white")
pen.begin_fill()
for _ in range(2):
    pen.forward(40)
    pen.left(90)
    pen.forward(10)
    pen.left(90)
pen.end_fill()

pen.penup()
pen.goto(450, -500)
pen.pendown()
pen.fillcolor("white")
pen.begin_fill()
for _ in range(2):
    pen.forward(40)
    pen.left(90)
    pen.forward(10)
    pen.left(90)
pen.end_fill()

pen.penup()
pen.goto(400, -500)
pen.pendown()
pen.fillcolor("white")
pen.begin_fill()
for _ in range(2):
    pen.forward(40)
    pen.left(90)
    pen.forward(10)
    pen.left(90)
pen.end_fill()

pen.penup()
pen.goto(350, -500)
pen.pendown()
pen.fillcolor("white")
pen.begin_fill()
for _ in range(2):
    pen.forward(40)
    pen.left(90)
    pen.forward(10)
    pen.left(90)
pen.end_fill()

pen.penup()
pen.goto(300, -500)
pen.pendown()
pen.fillcolor("white")
pen.begin_fill()
for _ in range(2):
    pen.forward(40)
    pen.left(90)
    pen.forward(10)
    pen.left(90)
pen.end_fill()

pen.penup()
pen.goto(250, -500)
pen.pendown()
pen.fillcolor("white")
pen.begin_fill()
for _ in range(2):
    pen.forward(40)
    pen.left(90)
    pen.forward(10)
    pen.left(90)
pen.end_fill()

pen.penup()
pen.goto(200, -500)
pen.pendown()
pen.fillcolor("white")
pen.begin_fill()
for _ in range(2):
    pen.forward(40)
    pen.left(90)
    pen.forward(10)
    pen.left(90)
pen.end_fill()

pen.penup()
pen.goto(150, -500)
pen.pendown()
pen.fillcolor("white")
pen.begin_fill()
for _ in range(2):
    pen.forward(40)
    pen.left(90)
    pen.forward(10)
    pen.left(90)
pen.end_fill()

pen.penup()
pen.goto(100, -500)
pen.pendown()
pen.fillcolor("white")
pen.begin_fill()
for _ in range(2):
    pen.forward(40)
    pen.left(90)
    pen.forward(10)
    pen.left(90)
pen.end_fill()

pen.penup()
pen.goto(50, -500)
pen.pendown()
pen.fillcolor("white")
pen.begin_fill()
for _ in range(2):
    pen.forward(40)
    pen.left(90)
    pen.forward(10)
    pen.left(90)
pen.end_fill()

pen.penup()
pen.goto(0, -500)
pen.pendown()
pen.fillcolor("white")
pen.begin_fill()
for _ in range(2):
    pen.forward(40)
    pen.left(90)
    pen.forward(10)
    pen.left(90)
pen.end_fill()

pen.penup()
pen.goto(-50, -500)
pen.pendown()
pen.fillcolor("white")
pen.begin_fill()
for _ in range(2):
    pen.forward(40)
    pen.left(90)
    pen.forward(10)
    pen.left(90)
pen.end_fill()

pen.penup()
pen.goto(-100, -500)
pen.pendown()
pen.fillcolor("white")
pen.begin_fill()
for _ in range(2):
    pen.forward(40)
    pen.left(90)
    pen.forward(10)
    pen.left(90)
pen.end_fill()

pen.penup()
pen.goto(-150, -500)
pen.pendown()
pen.fillcolor("white")
pen.begin_fill()
for _ in range(2):
    pen.forward(40)
    pen.left(90)
    pen.forward(10)
    pen.left(90)
pen.end_fill()

pen.penup()
pen.penup()
pen.goto(-200, -500)
pen.pendown()
pen.fillcolor("white")
pen.begin_fill()
for _ in range(2):
    pen.forward(40)
    pen.left(90)
    pen.forward(10)
    pen.left(90)
pen.end_fill()

pen.penup()
pen.penup()
pen.goto(-250, -500)
pen.pendown()
pen.fillcolor("white")
pen.begin_fill()
for _ in range(2):
    pen.forward(40)
    pen.left(90)
    pen.forward(10)
    pen.left(90)
pen.end_fill()

pen.penup()
pen.goto(-300, -500)
pen.pendown()
pen.fillcolor("white")
pen.begin_fill()
for _ in range(2):
    pen.forward(40)
    pen.left(90)
    pen.forward(10)
    pen.left(90)
pen.end_fill()

pen.penup()
pen.goto(-350, -500)
pen.pendown()
pen.fillcolor("white")
pen.begin_fill()
for _ in range(2):
    pen.forward(40)
    pen.left(90)
    pen.forward(10)
    pen.left(90)
pen.end_fill()

pen.penup()
pen.goto(-400, -500)
pen.pendown()
pen.fillcolor("white")
pen.begin_fill()
for _ in range(2):
    pen.forward(40)
    pen.left(90)
    pen.forward(10)
    pen.left(90)
pen.end_fill()

pen.penup()
pen.goto(-450, -500)
pen.pendown()
pen.fillcolor("white")
pen.begin_fill()
for _ in range(2):
    pen.forward(40)
    pen.left(90)
    pen.forward(10)
    pen.left(90)
pen.end_fill()

pen.penup()
pen.goto(-500, -500)
pen.pendown()
pen.fillcolor("white")
pen.begin_fill()
for _ in range(2):
    pen.forward(40)
    pen.left(90)
    pen.forward(10)
    pen.left(90)
pen.end_fill()

pen.penup()
pen.goto(-550, -500)
pen.pendown()
pen.fillcolor("white")
pen.begin_fill()
for _ in range(2):
    pen.forward(40)
    pen.left(90)
    pen.forward(10)
    pen.left(90)
pen.end_fill()

pen.penup()
pen.goto(-600, -500)
pen.pendown()
pen.fillcolor("white")
pen.begin_fill()
for _ in range(2):
    pen.forward(40)
    pen.left(90)
    pen.forward(10)
    pen.left(90)
pen.end_fill()

pen.penup()
pen.goto(-650, -500)
pen.pendown()
pen.fillcolor("white")
pen.begin_fill()
for _ in range(2):
    pen.forward(40)
    pen.left(90)
    pen.forward(10)
    pen.left(90)
pen.end_fill()

# РњР°С€РёРЅР°
turtle.fillcolor("red")
car = turtle.Turtle()
car.fillcolor("red")

# Р РёСЃСѓРµРј РєСѓР·РѕРІ РјР°С€РёРЅРєРё
car.penup()
car.goto(100, -460)
car.pendown()
car.fillcolor("red")
car.forward(100)
car.left(90)
car.forward(20)
car.left(90)
car.forward(20)
car.left(-45)
car.forward(20)
car.left(45)
car.forward(50)
car.left(45)
car.forward(20)
car.right(45)
car.forward(25)
car.left(20)
car.forward(4)
car.left(25)
car.forward(16)
car.left(60)
car.forward(8)
car.left(75)
car.forward(50)
car.left(90)
car.forward(6)
car.fillcolor("red")

# Р РёСЃСѓРµРј РєРѕР»РµСЃР° РјР°С€РёРЅРєРё
car.penup()
car.goto(100, -460)
car.pendown()
car.color("black")
car.dot(25)
car.penup()
car.goto(170, -460)
car.pendown()
car.dot(25)

t = turtle.Turtle()
t.speed(0)


def draw_tree(x, y, trunk_length, trunk_width, leaf_size, leaf_color):
    t.up()
    t.goto(x, y)
    t.down()

    # Р РёСЃРѕРІР°РЅРёРµ РєРѕСЂРёС‡РЅРµРІРѕРіРѕ СЃС‚РІРѕР»Р°
    t.width(trunk_width)
    t.color("brown")
    t.right(270)
    t.forward(trunk_length)

    # Р РёСЃРѕРІР°РЅРёРµ Р·РµР»РµРЅС‹С… Р»РёСЃС‚СЊРµРІ
    t.left(90)
    t.color(leaf_color)
    t.up()
    t.forward(trunk_width * 2)
    t.down()
    for _ in range(3):
        t.circle(leaf_size)
        t.up()
        t.backward(leaf_size * 1.5)
        t.right(120)
        t.down()


draw_tree(-400, -450, 100, 10, 20, "green")
t.up()
t.goto(-400, -200)
t.down()


def draw_tree(x, y, trunk_length, trunk_width, leaf_size, leaf_color):
    t.up()
    t.goto(x, y)
    t.down()

    # Р РёСЃРѕРІР°РЅРёРµ РєРѕСЂРёС‡РЅРµРІРѕРіРѕ СЃС‚РІРѕР»Р° 2
    t.width(trunk_width)
    t.color("brown")
    t.right(90)
    t.forward(trunk_length)

    # Р РёСЃРѕРІР°РЅРёРµ Р·РµР»РµРЅС‹С… Р»РёСЃС‚СЊРµРІ 2
    t.left(90)
    t.color(leaf_color)
    t.up()
    t.forward(trunk_width * 2)
    t.down()
    for _ in range(3):
        t.circle(leaf_size)
        t.up()
        t.backward(leaf_size * 1.5)
        t.right(120)
        t.down()


draw_tree(-600, -450, 100, 10, 20, "green")
t.up()
t.goto(-400, -200)
t.down()


def draw_tree(x, y, trunk_length, trunk_width, leaf_size, leaf_color):
    t.up()
    t.goto(x, y)
    t.down()

    # Р РёСЃРѕРІР°РЅРёРµ РєРѕСЂРёС‡РЅРµРІРѕРіРѕ СЃС‚РІРѕР»Р° 2
    t.width(trunk_width)
    t.color("brown")
    t.right(90)
    t.forward(trunk_length)

    # Р РёСЃРѕРІР°РЅРёРµ Р·РµР»РµРЅС‹С… Р»РёСЃС‚СЊРµРІ 2
    t.left(90)
    t.color(leaf_color)
    t.up()
    t.forward(trunk_width * 2)
    t.down()
    for _ in range(3):
        t.circle(leaf_size)
        t.up()
        t.backward(leaf_size * 1.5)
        t.right(120)
        t.down()


draw_tree(-300, -450, 100, 10, 20, "green")
t.up()
t.goto(-400, -200)
t.down()

t = turtle.Turtle()
t.speed(0)

# РќР°СЂРёСЃСѓРµРј РєРѕСЂРїСѓСЃ СЃРІРµС‚РѕС„РѕСЂР°
t.color("black")
t.width(5)

t.up()
t.goto(-200, -400)
t.down()
t.forward(50)
t.left(90)
t.forward(100)
t.left(90)
t.forward(50)
t.left(90)
t.forward(100)
t.left(90)

pen.penup()
pen.goto(-178, -485)
pen.pendown()
pen.fillcolor("black")
pen.begin_fill()
for _ in range(2):
    pen.forward(5)
    pen.left(90)
    pen.forward(85)
    pen.left(90)
pen.end_fill()

# РќР°СЂРёСЃСѓРµРј С„РѕРЅР°СЂРё СЃРІРµС‚РѕС„РѕСЂР°
t.up()
t.goto(-175, -330)
t.down()
t.color("red")
t.begin_fill()
t.circle(10)
t.end_fill()

t.up()
t.goto(-175, -360)
t.down()
t.color("yellow")
t.begin_fill()
t.circle(10)
t.end_fill()

t.up()
t.goto(-175, -390)
t.down()
t.color("green")
t.begin_fill()
t.circle(10)
t.end_fill()

turtle.done()

car.hideturtle()
turtle.done()