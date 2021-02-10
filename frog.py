import ursina
from ursina import *
import random

app = Ursina()
window.color = color.rgb(38,37,38)
speed = 0.05
rot_speed = 0.06
floats = [0.01, 0.02, 0.051, 0.04,0.2, 0.32]
floatss = [2,1.4,1.45,1.5,1.8,2.5,2.8,3,3.2,2.32]
frog = 'frog-game-main/frog!.png'
player = Entity(model = 'sphere', scale = (0.35,0.35,0.35), position = (0,-2), texture = frog, collider = 'box')
rains = []
hazards = []
count = 0
hp = 50
text = Text(text="frog game! -by adal :)", color = color.turquoise, origin = (0,-18), background = True)
window.borderless = False
window.fps_counter.enabled = False
window.exit_button.visible = False

for i in range(450):
    rain = Entity(model = 'circle', scale = (0.25,0.5,0.25), color = color.cyan, collider = 'box')
    rain.x = random.uniform(-7,7)
    rain.y = random.uniform(2,50)
    rains.append(rain)
for i in range(150):
    hazard = Entity(model = 'circle', scale = (0.25,0.5,0.25), color = color.red, collider = 'box')
    hazard.x = random.uniform(-7,7)
    hazard.y = random.uniform(2,50)
    hazards.append(hazard)
def update():
    global count
    global hp
    print_on_screen(str(count), scale = 1, position = (-.85,0.45),duration = 1/25)
    print_on_screen('hp ' + str(hp), scale = 1, position = (-.85,0.35),duration = 1/25)
    hit_detect = player.intersects()
    if hit_detect.hit:
        if hit_detect.entity in rains:
            hit_detect.entity.scale = (0,0,0)
            rains.remove(hit_detect.entity)
            count += 1
        if hit_detect.entity in hazards:
            hp -= 1
    if hp <= 0:
        application.pause()
        end_msg('u lose, ur score was '+ str(count))
    movement()
    if player.x > 6.8:
        player.x = 6.8
    if player.x < -6.8:
        player.x = -6.8
    if player.y > 3.6:
        player.y = 3.6
    if player.y < -3.6:
        player.y = -3.6
    if held_keys['space']:
        player.scale = (1,1,1)
    else:
        player.scale = (0.35,0.35,0.35)
    for rain in rains:
        if rain.y < -5 :
            rains.remove(rain)
    if len(rains) <= 0:
        if hp == 50:
            application.pause()
            end_msg('perfect run! your score was '+ str(count))
        else:
            application.pause()
            end_msg('nice! your score was ' +str(count) + " and you had " + str(hp) + " hp left")
def end_msg(msg):
    lose_text = Text(text = msg, color = color.pink, origin = (0,0), background = True)
def movement():
    if held_keys['w']:
        player.y += speed
        player.rotation_x += rot_speed *100
    if held_keys['s']:
        player.y -= speed
        player.rotation_x += rot_speed *100
    if held_keys['a']:
        player.x -= speed
        player.rotation_y -= rot_speed  * 100
    if held_keys['d']:
        player.x += speed
        player.rotation_y += rot_speed *100
    for rain in rains:
        rain.y -= random.choice(floatss) * time.dt
    for hazard in hazards:
        hazard.y -= random.choice(floatss) * time.dt
app.run()
