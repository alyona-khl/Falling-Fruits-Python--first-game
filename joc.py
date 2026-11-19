import turtle
import random
import time
#ecran
fereastra=turtle.Screen()
fereastra.title("Falling Fruits")
fereastra.bgcolor("#1FB7ED")
fereastra.setup(width=600, height=600)
fereastra.tracer(0) #fluiditate(se opreste animatia)

#variabile
scor=0
vieti=3
viteza_obiecte=2

#fructe
fructe=[("blue","afina"),("yellow","banana"),("orange","portocala"),("green","kiwi")]

#cos
cos=turtle.Turtle()
cos.speed(0)
cos.shape("square")
cos.color("#47341A")
cos.shapesize(stretch_wid=4,stretch_len=4)
cos.penup()
cos.goto(0,-250)

#obiecte cazatoare(fructe)
fruct=turtle.Turtle()
fruct.speed(0)
fruct.shape("circle")
fruct.penup()
def reseteaza_fruct():
    if fructe:
        culoare,nume=random.choice(fructe)
        fruct.color(culoare)
    fruct.goto(random.randint(-280,280),280)
#obiect de evitat
obiect_x=turtle.Turtle()
obiect_x.speed(0)
obiect_x.shape("square")
obiect_x.color("red")
obiect_x.penup()

#text
text_x=turtle.Turtle()
text_x.hideturtle()
text_x.penup()
text_x.color("white")
def reseteaza_x():
    nou_x=random.randint(-280,280)
    while abs(nou_x-fruct.xcor())<80:
        nou_x=random.randint(-280,280)
    obiect_x.goto(nou_x,280)

#scor, vieti, mesaje
hud=turtle.Turtle()
hud.speed(0)
hud.color("white")
hud.penup()
hud.hideturtle()
def actualiz_afisaj():
    hud.clear()
    hud.goto(0,260)
    hud.write(f"Scor:{scor}, ❤️Vieti:{vieti}", align="center", font=("Arial",16,"bold"))
    
#buton restart
restart=turtle.Turtle()
restart.speed(0)
restart.shape("square")
restart.color("#0E8C4A")
restart.shapesize(stretch_wid=2, stretch_len=7)
restart.penup()

#text buton restart
text_btnrestart=turtle.Turtle()
text_btnrestart.hideturtle()

text_btnrestart.penup()
text_btnrestart.color("white")

#miscare cos
def misca_stg():
    if joc_activ:
        x=cos.xcor()
        if x>-240:
           cos.setx(x-30)
def misca_dr():
    if joc_activ:
        x=cos.xcor()
        if x<240:
            cos.setx(x+30)
fereastra.listen()
fereastra.onkeypress(misca_stg, "Left")
fereastra.onkeypress(misca_dr, "Right")

#functie pornire/resetare joc
def porneste(x=0,y=0):
    global scor, vieti, viteza_obiecte, joc_activ
     #resetare variabile stare initiala
    scor=0
    vieti=3
    viteza_obiecte=2
    joc_activ=True
    #buton si text de game over ascunse
    restart.hideturtle()
    text_btnrestart.clear()
    hud.clear()
    #repozitionare obiecte
    cos.goto(0,-250)
    reseteaza_fruct()
    reseteaza_x()
    actualiz_afisaj()
    #pornire bucla de joc
    ruleaza_bucla()

#functie sfarsit joc
def opreste():
    global joc_activ
    joc_activ=False
    #ascund x
    text_x.clear()
    #afisare game over
    hud.goto(0,60)
    hud.color("#7a140a")
    hud.write("Ai pierdut!",align="center", font=("Arial", 36, "bold"))
    hud.goto(0,10)
    hud.color("white")
    hud.write(f"Scor final: {scor}", align="center", font=("Arial", 18, "normal"))
    #afisare din nou buton restart
    restart.goto(0,-70)
    restart.showturtle()
    text_btnrestart.goto(0,-80)
    text_btnrestart.write("Joaca din nou!", align="center",font=("Arial",14,"bold"))

#bucla pp tranformata in fct recursiva
def ruleaza_bucla():
    global scor, vieti, viteza_obiecte
    if joc_activ:
        fereastra.update()
        #miscare fructe
        fruct.sety(fruct.ycor() - viteza_obiecte)
        if fruct.distance(cos)<40 and fruct.ycor()<-230:
            scor+=1
            viteza_obiecte+=0.2
            actualiz_afisaj()
            reseteaza_fruct()
        if fruct.ycor()<-280:
            vieti-=1
            actualiz_afisaj()
            if vieti==0:
                opreste()
                return
            else:
                reseteaza_fruct()
        #miscare x
        obiect_x.sety(obiect_x.ycor()-viteza_obiecte)
        text_x.clear()
        text_x.goto(obiect_x.xcor(), obiect_x.ycor()-8)
        text_x.write("X", align="center",font=("Aria;", 12, "bold"))
        if obiect_x.distance(cos)<40 and obiect_x.ycor()<-230:
            opreste()
            return
        if obiect_x.ycor()<-280:
            reseteaza_x()
        #programare urmat actualiz peste 10 milisecunde
        fereastra.ontimer(ruleaza_bucla,10)
#conectare click pe buton cu functia de pornire
restart.onclick(porneste)
#pornire joc automat prima data cand se deschide programul
porneste()
fereastra.mainloop()
        

