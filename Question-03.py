import turtle

def draw_branch(t, branch_length, angle_left, angle_right, depth, reduction_factor, initial_depth):
    if depth > 0:
        if depth == initial_depth:
            #Setting the root color to brown  
            t.pencolor("brown") 
            #Setting the root thickness starting as 10
            t.pensize(10)  
        else:
            #Setting all other branches to green
            t.pencolor("green")  
            #Reducing the thickness after each branches
            t.pensize(max(1, depth))  
        
        t.forward(branch_length)
        
        #Right subtree
        t.right(angle_right)
        draw_branch(t, branch_length * reduction_factor, angle_left, angle_right, depth - 1, reduction_factor, initial_depth)
        
        #Left subtree
        t.left(angle_right + angle_left)
        draw_branch(t, branch_length * reduction_factor, angle_left, angle_right, depth - 1, reduction_factor, initial_depth)
        
        #Returnig to original state
        t.right(angle_left)
        t.backward(branch_length)
    else:
        #Drawing leafs at the end of each branch
        #Setting the leaf color to green
        t.pencolor("green")  
        t.begin_fill()
        #putting leaf size as 10
        t.circle(10)  
        t.end_fill()


def main():

    
    t = turtle.Turtle()
    t.speed(0)


    #Taking the inputs from the keyboard as mentioned in the question
    angle_left = float(input("Enter the left branch angle (e.g., 20): "))
    angle_right = float(input("Enter the right branch angle (e.g., 25): "))
    starting_length = float(input("Enter the starting branch length (e.g., 100): "))
    depth = int(input("Enter the recursion depth (e.g., 5): "))
    reduction_factor = float(input("Enter the branch length reduction factor (e.g., 0.7): "))

    #Initializing the turtles
    t.penup()
    t.goto(0, -150)  
    t.pendown()
    t.left(90)  

    #Drawing the tree by passing the user values to the draw_brunch funtion
    draw_branch(t, starting_length, angle_left, angle_right, depth, reduction_factor, depth)

    #Closing the drawing
    t.hideturtle()


if __name__ == "__main__":
    main()
