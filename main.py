import cv2 
import time
import numpy as np
  
from entities import ArtilleryShell, Objective
from config import TIMESTEP

if __name__ == "__main__":
    # Get input from user
    # artillery_shell_v0 = float(input("Vận tốc ban đầu của viên đạn:"))
    # artillery_shell_angle = float(input("Góc ban đầu của viên đạn:"))
    # artillery_shell_initial_x = float(input("Tọa độ ban đầu theo phương x của viên đạn:"))
    # artillery_shell_initial_y = float(input("Tọa độ ban đầu theo phương y của viên đạn:"))
    # artillery_shell_radius = float(input("Bán kính của viên đạn:"))

    # objective_v0 = float(input("Vận tốc ban đầu của mục tiêu:"))
    # objective_angle = float(input("Góc ban đầu của mục tiêu:"))
    # objective_initial_x = float(input("Tọa độ ban đầu theo phương x của mục tiêu:"))
    # objective_initial_y = float(input("Tọa độ ban đầu theo phương y của mục tiêu:"))
    # objective_radius = float(input("Bán kính của mục tiêu:"))


    artillery_shell_v0 = 100
    artillery_shell_angle = 45
    artillery_shell_initial_x = 0
    artillery_shell_initial_y = 0
    artillery_shell_radius = 2

    objective_v0 = 0
    objective_angle = 0
    objective_initial_x = 487
    objective_initial_y = 254
    objective_radius = 10

    # Initialize objects
    current_time, step = 0 , 0
    artillery_shell = ArtilleryShell(weight = 1, 
                                     v0 = artillery_shell_v0, 
                                     angle = artillery_shell_angle, 
                                     initial_x = artillery_shell_initial_x, 
                                     initial_y = artillery_shell_initial_y, 
                                     is_movable = True,
                                     radius = artillery_shell_radius)
    objective = Objective(weight = 1, 
                            v0 = objective_v0, 
                            angle = objective_angle, 
                            initial_x = objective_initial_x, 
                            initial_y = objective_initial_y, 
                            is_movable = False,
                            radius = objective_radius)

    heightImage, widthImage = 500, 1000
    cv2.namedWindow("Display", cv2.WINDOW_AUTOSIZE) 

    height_explosion_image, width_explosion_image = 50, 50
    explosion_image = cv2.imread("images/explosion_icon.png")
    explosion_image = cv2.resize(explosion_image, (height_explosion_image, width_explosion_image), interpolation = cv2.INTER_AREA)
    
    height_canon_image, width_canon_image = 50, 50
    canon_image = cv2.imread("images/canon_icon.png", -1)
    canon_image = cv2.resize(canon_image, (height_canon_image, width_canon_image), interpolation = cv2.INTER_AREA)


    is_collided = False
    while cv2.getWindowProperty('Display', 0) >= 0:        
        background = np.ones((heightImage,widthImage,3), np.uint8)*255.0
        # draw canon
        background[heightImage - height_canon_image:, :width_canon_image, :] = canon_image[:,:,:3] #heightImage - height_canon_image

        # draw artillery_shell
        if not is_collided and (artillery_shell.x >= width_canon_image or artillery_shell.y >= height_canon_image):
            cv2.circle(background, [int(artillery_shell.x), heightImage - int(artillery_shell.y)], int(artillery_shell.radius), (0, 0, 0), 1)
        for i in range(len(artillery_shell.trace) - 1):
            if not is_collided and (artillery_shell.trace[i][0] >= width_canon_image or artillery_shell.trace[i][1] >= height_canon_image):
                cv2.line(background, 
                        (artillery_shell.trace[i][0], heightImage - artillery_shell.trace[i][1]), 
                        (artillery_shell.trace[i + 1][0], heightImage - artillery_shell.trace[i + 1][1]), 
                        (0, 0, 255), 
                        1)

        #draw objective
        if not is_collided:
            cv2.circle(background, [int(objective.x), heightImage - int(objective.y)], int(objective.radius), (0, 0, 0), 5)
            for i in range(len(objective.trace) - 1):
                cv2.line(background, 
                        (objective.trace[i][0], heightImage - objective.trace[i][1]), 
                        (objective.trace[i + 1][0], heightImage - objective.trace[i + 1][1]), 
                        (0,0,255), 
                        1)
        
        # check collision
        if is_collided:
            background[int(objective.y) - height_explosion_image//2: int(objective.y) + height_explosion_image//2, 
                       int(objective.x) - width_explosion_image//2: int(objective.x) + width_explosion_image//2, :] = explosion_image[:,:,:3]

        # show distance between object
        font = cv2.FONT_HERSHEY_SIMPLEX
        fontScale = 0.5
        color = (0, 0, 255)
        thickness = 1
        image = cv2.putText(background, 
                            f"Distance: {artillery_shell.get_distance(objective)}", 
                            (0, 20), 
                            font, fontScale, color, thickness, cv2.LINE_AA)
        
        image = cv2.putText(background, 
                            f"Artillery Shell: {artillery_shell.x}, {artillery_shell.y}", 
                            (0, 40), 
                            font, fontScale, color, thickness, cv2.LINE_AA)

        image = cv2.putText(background, 
                            f"Objective: {objective.x}, {objective.y}", 
                            (0, 60), 
                            font, fontScale, color, thickness, cv2.LINE_AA)

        image = cv2.putText(background, 
                            f"Collision: {artillery_shell.is_collided(objective)}", 
                            (0, 80), 
                            font, fontScale, color, thickness, cv2.LINE_AA)

        # visualize 
        cv2.imshow('Display', background/255.0)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
        if is_collided:
            time.sleep(2)
            break
        
        #update objects
        step += 1
        
        new_artillery_shell_x, new_artillery_shell_y = artillery_shell.get_position_at_t(current_time + step * TIMESTEP)
        artillery_shell.move(new_artillery_shell_x, new_artillery_shell_y)

        new_objective_x, new_objective_y = artillery_shell.get_position_at_t(current_time + step * TIMESTEP)
        artillery_shell.move(new_objective_x, new_objective_y)
        
        if not is_collided:
            is_collided = artillery_shell.is_collided(objective)

        # time.sleep(TIMESTEP)
    
    cv2.destroyAllWindows()
    