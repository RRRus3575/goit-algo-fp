import turtle
import math

def draw_pythagoras_tree(branch_length, level, angle):
    if level == 0:
        return

    turtle.forward(branch_length)
    
    turtle.right(angle)
    draw_pythagoras_tree(branch_length * math.sqrt(2) / 2, level - 1, angle)
    
    turtle.left(2 * angle)
    draw_pythagoras_tree(branch_length * math.sqrt(2) / 2, level - 1, angle)
    
    turtle.right(angle)
    turtle.backward(branch_length)

def main():
    branch_length = float(input("Введіть довжину гілки: "))
    angle = float(input("Введіть кут повороту: "))
    level = int(input("Введіть рівень рекурсії: "))

    turtle.speed(0) 
    turtle.left(90)  
    turtle.up()
    turtle.backward(200)
    turtle.down()
    
    draw_pythagoras_tree(branch_length, level, angle)
    
    turtle.done()

if __name__ == "__main__":
    main()
