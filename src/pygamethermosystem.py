import pygame as pg
import numpy as np
from DrawTools.Draw import *
from DrawTools.DrawSystem import *
from Game.Controls import *
from thermosystem import thermoSystem

pg.init()

#in millimeters
Width, Height = 1800, 1000  
Win = pg.display.set_mode((Width, Height))
pg.display.set_caption("Gravitational Field")
GRAY = (200, 200, 200)

def main():
    run = True
    clock = pg.time.Clock()

    system = thermoSystem(2000, 1E-18, [850, 450, 950, 550])

    draw = drawThermo(Win, system)

    ctrl = UIcontroller(system)


    #frame rate and efficiency stuff
    counter = 0
    dt = 1/25
    max_count = 5

    while run:


        #get inputs to influence sim
        ctrlr = ctrl.inputs()
        if ctrlr == 0:
            run = False


        system.evolve(dt)

        if counter % max_count == 0:
            clock.tick(60)
            Win.fill((10, 40, 70))
            draw.draw()
            draw.draw_data()
            pg.display.update()

        counter += 1

    pg.quit()


main()

