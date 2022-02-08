@namespace
class SpriteKind:
    MegaEnemy = SpriteKind.create()
def BossFight():
    scene.set_background_color(2)
    game.show_long_text("You shall face...MEGA KEVIN", DialogLayout.TOP)
    info.start_countdown(5.5)
    MegaKevin()
def addBobas2():
    global projectile
    projectile = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . 7 . . . . . . 
                    . . . . . . . . . 7 . . . . . . 
                    . . . . . . . . . 7 . . . . . . 
                    . . . f f f f f f f f f f . . . 
                    . . . . f . . . . 7 . f . . . . 
                    . . . . f . . . . 7 . f . . . . 
                    . . . . f d d d d d d f . . . . 
                    . . . . f d f d d f d f . . . . 
                    . . . . f d d f d d d f . . . . 
                    . . . . f d f d f d f f . . . . 
                    . . . . f f d d d f d f . . . . 
                    . . . . f d f d f d f f . . . . 
                    . . . . f f f f f f f f . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.projectile)
    projectile.set_position(0, 0)
    projectile.set_stay_in_screen(True)

def on_on_overlap(sprite, otherSprite):
    info.change_score_by(1)
    otherSprite.destroy(effects.bubbles, 200)
    music.pew_pew.play()
sprites.on_overlap(SpriteKind.player, SpriteKind.projectile, on_on_overlap)

def addBobas():
    global mySpeed, projectile
    mySpeed = 50 + info.score() * 2
    projectile = sprites.create_projectile_from_side(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . 7 . . . . . . 
                    . . . . . . . . . 7 . . . . . . 
                    . . . . . . . . . 7 . . . . . . 
                    . . . f f f f f f f f f f . . . 
                    . . . . f . . . . 7 . f . . . . 
                    . . . . f . . . . 7 . f . . . . 
                    . . . . f d d d d d d f . . . . 
                    . . . . f d f d d f d f . . . . 
                    . . . . f d d f d d d f . . . . 
                    . . . . f d f d f d f f . . . . 
                    . . . . f f d d d f d f . . . . 
                    . . . . f d f d f d f f . . . . 
                    . . . . f f f f f f f f . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        mySpeed,
        0)
    projectile.set_position(0, randint(0, scene.screen_height()))
def addKevins():
    global mySpeed, Kevin
    wrapScreen(mySprite3)
    mySpeed = 50 + info.score() * 2
    Kevin = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . f f f f f f f . . . 
                    . . . f f f f f f f f f f . . . 
                    . . . f f f f f f f f f f . . . 
                    . . . d d d d d d d d d d . . . 
                    . . . d d f d d d d f d d . . . 
                    . . . d d d d d d d d d d . . . 
                    . . . . d d d d d d d d . . . . 
                    . . . . . d d d d d d . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.enemy)
    Kevin.set_position(randint(0, scene.screen_width()),
        randint(0, scene.screen_height()))
    Kevin.set_bounce_on_wall(True)
    Kevin.set_velocity(mySpeed, mySpeed)
    Kevin.start_effect(effects.hearts)
def MegaKevin():
    global mySprite2
    mySprite2 = sprites.create(img("""
            . . f f f f f f f f f f f f f f 
                    f f f f f f f f f f f f f f f f 
                    f f f f f f f f f f f f f f f f 
                    f f f f f f f f f f f f f f f f 
                    f f f f f f f f f f f f f f f f 
                    d d d d d d d d d f f f f f f d 
                    d d d d d d d d d d d d d d d d 
                    d d d d d d d d d d d d d d d d 
                    d f f f d d d d d d d d f f f d 
                    d f 2 f d d d d d d d d f 2 f d 
                    d f f f d d d d d d d d f f f d 
                    d d d d d d d d d d d d d d d d 
                    d d d d d d d d d d d d d d d d 
                    d d d d d d d d d d d d d d d d 
                    . d d d d d d d d d d d d d . . 
                    . . d d d d d d d d d d d . . .
        """),
        SpriteKind.MegaEnemy)
    mySprite2.set_position(0, randint(0, scene.screen_height()))
    mySprite2.set_bounce_on_wall(True)
    mySprite2.set_velocity(25 - info.score(), 25 - info.score())
    mySprite2.follow(mySprite3, 50)

def on_on_overlap2(sprite2, otherSprite2):
    game.show_long_text("MEGA KEVIN HAS DEFEATED YOU", DialogLayout.TOP)
    game.over(False)
sprites.on_overlap(SpriteKind.player, SpriteKind.MegaEnemy, on_on_overlap2)

def wrapScreen(mySprite: Sprite):
    if mySprite.x + mySprite.width / 2 < 0:
        mySprite.x = scene.screen_width() + mySprite.width / 2
    if mySprite.x - mySprite.width / 2 > scene.screen_width():
        mySprite.x = 0 - mySprite.width / 2
    if mySprite.y + mySprite.height / 2 < 0:
        mySprite.y = scene.screen_height() + mySprite.height / 2
    if mySprite.y - mySprite.height / 2 > scene.screen_height():
        mySprite.y = 0 - mySprite.height / 2

def on_on_overlap3(sprite3, otherSprite3):
    game.show_long_text("Kevin Nguyen caught u!!", DialogLayout.TOP)
    game.over(False)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap3)

timer = 0
mySprite2: Sprite = None
Kevin: Sprite = None
mySpeed = 0
projectile: Sprite = None
mySprite3: Sprite = None
scene.set_background_color(9)
mySprite3 = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . f f f f f f f . . . . . 
            . . . f f f f f f f f f . . . . 
            . . . f f f f f f f f f . . . . 
            . . . f f f f f d d f f . . . . 
            . . . f d d d d d d d f . . . . 
            . . . f d f d d d f d f . . . . 
            . . . f d d d d d d d f . . . . 
            . . . f d d d d d d d f . . . . 
            . . f f . d d d d d . f f . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.player)
mySprite3.set_stay_in_screen(True)
controller.move_sprite(mySprite3)
game.show_long_text("Eat as much boba as possible and don't let Kevin Nguyen catch you!",
    DialogLayout.TOP)
info.set_score(0)

def on_update_interval():
    global timer
    timer = timer + 1
    if timer == 200:
        info.stop_countdown()
        BossFight()
    elif timer % 5 == 0 and timer < 200:
        addBobas()
        if timer % 80 == 0 and timer < 200:
            addKevins()
    elif timer == 250:
        game.over(True)
game.on_update_interval(100, on_update_interval)
