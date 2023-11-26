# The script of the game goes in this file.

default your_health = 100
default cloyster_health = 100
#define buttons counter
default nw_count = 0
default ne_count = 0
default sw_count = 0
default se_count = 0
#default position generation of bursts
default col = 0.8
default row = 0.8
default end = False
#define images
init:
    image punchNW = Image("images/punch_nw.png", optimize_bounds=True, oversample=2)
    image punchNE = Image("images/punch_ne.png", optimize_bounds=True, oversample=2)
    image punchSW = Image("images/punch_sw.png", optimize_bounds=True, oversample=2)
    image punchSE = Image("images/punch_se.png", optimize_bounds=True, oversample=2)
#define winner legend screen
screen winner():
    textbutton "You Win":
        align (0.5,0.5)
        text_color "#3f3"
        action Function(renpy.return_statement)
#define loser legend screen
screen loser():
        textbutton "You Died":
            align (0.5,0.5)
            text_color "#f33"
            action Function(renpy.return_statement)
#python block that run at start of the game
init python:

    def set_health(param):

#set variables to global
        global punch_count
        global your_health
        global cloyster_health
        global end

        global nw_count
        global ne_count
        global sw_count
        global se_count

        if not end:

#buttons identified with cardinal directions
            if param == "nw": nw_count+=1
            if param == "ne": ne_count+=1
            if param == "sw": sw_count+=1
            if param == "se": se_count+=1

#if enemy life under zero clean screen and show legend
            if cloyster_health <= 0:
                renpy.hide_screen("stats")
                renpy.hide_screen("grilla")
                renpy.hide("cloyster")
                renpy.show_screen("winner")
                end = True
#if player life under zero clean screen and show legend
            elif your_health <= 0:
                renpy.hide_screen("stats")
                renpy.hide_screen("grilla")
                renpy.hide("cloyster")
                renpy.show_screen("loser")
                end = True
#if some of the buttons is clicked more than 3 times enemy can parry
            else:
                if nw_count >= 3:
                    your_health -= 50
                    nw_count = 0
                if ne_count >= 3:
                    your_health -= 50
                    ne_count = 0
                if sw_count >= 3:
                    your_health -= 50
                    sw_count = 0
                if se_count >= 3:
                    your_health -= 50
                    se_count = 0
#otherwise is attacked
                else:
                    cloyster_health -= 20

#define player health and enemy health screen
screen stats():
    frame:
        align (0.01,0.1)
        background "#f95"
        grid 2 2:
            
            text "you :" color "#fff"
            text "[your_health]" color "#f88"
            
            text "cloyster :" color "#fff"
            text "[cloyster_health]" color "#f88"


#define buttons grid
screen grilla():
    grid 2 2:
        align (0.5,0.5)
        spacing 150

        imagebutton idle "punchSE" action Function(set_health, "se")
        
        imagebutton idle "punchSW" action Function(set_health, "sw")
        
        imagebutton idle "punchNE" action Function(set_health, "ne")
        
        imagebutton idle "punchNW" action Function(set_health, "nw")

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    
    #scene bg

    show cloyster at truecenter

    # These display lines of dialogue.
    
    "Select burst to punch."

    "if you select three times the same side gives the enemy a chance of parry!"

#show game screens
    show screen stats

    call screen grilla


