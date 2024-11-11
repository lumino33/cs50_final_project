# cs50_final_project
A fun visualization based on Opencv about physical motion

#### Video Demo: https://youtu.be/Wcz9SoOLR00

#### Description:
The system describes the trajectory of an artillery shell and an objective under gravity (without air resistance, friction). The goal is that find the trajectory of the canon shell so that it can break the objective.

The overview system:

![alt text](images/overview.jpg)

The system includes two objects. The first one is a canon shell fired from a canon with initial speed v1, initial angle alpha1, initial coordinates x1_0 and y1_0. The second one is an objective with initial speed v2, initial angle alpha2, initial coordinates x2_0 and y2_0

Consequently, we find the coordinate equations of two objects in terms of time. Then, when the collision happens, the coordinates of two objects are equals.

For implement, we model two objects by OOP. Then we use Numpy libraby for efficient coordinates calculation. Finally, we use OpenCV library to visualize the trajectory of two objects. In case of collision, an effect will happen (see at the demo).

Detailed Equations:

![alt text](images/equations.jpg)

Example:

![alt text](images/example.jpg)

Result: This is the demo with above hyper parameters (The canon shell could break the objective)

![](images/example.gif)

# 2. Dependencies
    1. This project uses Python 3.9

    2. Run 'pip install -r requirements.txt' to install dependencies

# 3. Run
    1. Change the parameters at main.py:
![alt text](images/params.png)

    2. Run 'python main.py'

# 4. Future Idea

In the future, I will incorporate incremental learning to the canon shell, so it can find the objective automatically with any initial conditions.

In addition, I will improve the design of two objectives. 

