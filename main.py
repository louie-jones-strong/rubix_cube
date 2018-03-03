import random
import play_sound

def create_cube():
    number_on = False
    #number_on = True
    #
    #     5              top
    #   0 1 2 3     left front    right back
    #     4              bottom
    #
    cube = []
    for loop in range(6):
        side = []
        number = 0
        for loop2 in range(3):
            temp = []
            for loop3 in range(3):
                if number_on:
                    temp += [str(loop)+str(number)]
                else:
                    temp += [loop]
                number +=1
            side += [temp]
        cube += [side]
    return cube

def print_cube(cube):
    lenght = len(str(cube[0][0]))
    print("")
    print(" "*lenght + str(cube[5][0]))
    print(" "*lenght + str(cube[5][1]))
    print(" "*lenght + str(cube[5][2]))

    print(str(cube[0][0])+str(cube[1][0])+str(cube[2][0])+str(cube[3][0]))
    print(str(cube[0][1])+str(cube[1][1])+str(cube[2][1])+str(cube[3][1]))
    print(str(cube[0][2])+str(cube[1][2])+str(cube[2][2])+str(cube[3][2]))

    print(" "*lenght + str(cube[4][0]))
    print(" "*lenght + str(cube[4][1]))
    print(" "*lenght + str(cube[4][2]))
    print("")

    return

def turn_face(cube,times=1):
    new_cube = create_cube()

    new_cube[3] = copy_plane(cube[3])

    new_cube[0] = copy_plane(cube[0])
    new_cube[0][0][2] = cube[4][0][0]
    new_cube[0][1][2] = cube[4][0][1]
    new_cube[0][2][2] = cube[4][0][2]

    new_cube[5] = copy_plane(cube[5])
    new_cube[5][2][0] = cube[0][0][2]
    new_cube[5][2][1] = cube[0][1][2]
    new_cube[5][2][2] = cube[0][2][2]

    new_cube[2] = copy_plane(cube[2])
    new_cube[2][0][0] = cube[5][2][0]
    new_cube[2][1][0] = cube[5][2][1]
    new_cube[2][2][0] = cube[5][2][2]

    new_cube[4] = copy_plane(cube[4])
    new_cube[4][0][0] = cube[2][0][0]
    new_cube[4][0][1] = cube[2][1][0]
    new_cube[4][0][2] = cube[2][2][0]


    new_cube[1] = turn_plane_no_side(cube[1])
    
    if times > 1:
        new_cube = turn_face(new_cube,times=times-1)

    return new_cube

def copy_plane(plane):
    new_plane = [[0,0,0],[0,0,0],[0,0,0]]
    for loop in range(3):
        for loop2 in range(3):
            new_plane[loop][loop2] = plane[loop][loop2]
    return new_plane

def turn_plane_no_side(plane):
    new_plane = [[0,0,0],[0,0,0],[0,0,0]]
    #middle
    new_plane[1][1] = plane[1][1]
        
    #corners
    new_plane[0][0] = plane[2][0]
    new_plane[2][0] = plane[2][2]
    new_plane[0][2] = plane[0][0]
    new_plane[2][2] = plane[0][2]
        
    #edges
    new_plane[0][1] = plane[1][0]
    new_plane[2][1] = plane[1][2]
    new_plane[1][2] = plane[0][1]
    new_plane[1][0] = plane[2][1]
    return new_plane

def turn_cube_horizontal(cube):
    new_cube = create_cube()
    new_cube[0] = cube[3]
    new_cube[1] = cube[0]
    new_cube[2] = cube[1]
    new_cube[3] = cube[2]
    
    cube[4] = turn_plane_no_side(cube[4])
    cube[4] = turn_plane_no_side(cube[4])
    new_cube[4] = turn_plane_no_side(cube[4])

    new_cube[5] = turn_plane_no_side(cube[5])
    return new_cube

def turn_cube_vertical(cube):
    new_cube = create_cube()
    new_cube[1] = cube[4]
    new_cube[5] = cube[1]

    new_cube[4] = copy_plane(cube[3])
    new_cube[4][0] = cube[3][2]
    new_cube[4][2] = cube[3][0]

    new_cube[3] = copy_plane(cube[5])
    new_cube[3][0] = cube[5][2]
    new_cube[3][2] = cube[5][0]
    new_cube[3][1] = cube[5][1]
    
    cube[0] = turn_plane_no_side(cube[0])
    cube[0] = turn_plane_no_side(cube[0])
    new_cube[0] = turn_plane_no_side(cube[0])

    new_cube[2] = turn_plane_no_side(cube[2])
    return new_cube

def turn_cal(cube,face=1,times=1):
    
    times = times%4
    if times == 0:
        return cube

    if face == 0:
        cube = turn_cube_horizontal(cube)
        cube = turn_face(cube,times=times)
        cube = turn_cube_horizontal(cube)
        cube = turn_cube_horizontal(cube)
        cube = turn_cube_horizontal(cube)
    elif face == 1:
        cube = turn_face(cube,times=times)
    elif  face == 2:
        cube = turn_cube_horizontal(cube)
        cube = turn_cube_horizontal(cube)
        cube = turn_cube_horizontal(cube)
        cube = turn_face(cube,times=times)
        cube = turn_cube_horizontal(cube)
    elif face == 3:
        cube = turn_cube_horizontal(cube)
        cube = turn_cube_horizontal(cube)
        cube = turn_face(cube,times=times)
        cube = turn_cube_horizontal(cube)
        cube = turn_cube_horizontal(cube)
    elif face == 4:
        cube = turn_cube_vertical(cube)
        cube = turn_face(cube,times=times)
        cube = turn_cube_vertical(cube)
        cube = turn_cube_vertical(cube)
        cube = turn_cube_vertical(cube)
    elif face == 5:
        cube = turn_cube_vertical(cube)
        cube = turn_cube_vertical(cube)
        cube = turn_cube_vertical(cube)
        cube = turn_face(cube,times=times)
        cube = turn_cube_vertical(cube)

    return cube

def fittness_cal(cube):
    completed = create_cube()
    fittness = 0

    for loop in range(6):
        for loop2 in range(3):
            for loop3 in range(3):
                if cube[loop][loop2][loop3] == completed[loop][loop2][loop3]:
                    fittness += 1
    return fittness/(6*3*3)*100

def random_play(cube,turns):
    for loop in range(turns):
        face = random.randint(0,5)
        times = random.randint(1,3)
        cube = turn_cal(cube,face=face,times=times)

    return cube





cube = create_cube()
play_sound.sound_setup("sounds\\your amazing.ogg")
print_cube(cube)

while True:
    
    turns = int(input("turns to random: "))
    if turns > 0:
        cube = random_play(cube,turns)
        print_cube(cube)
        fittness = fittness_cal(cube)
        print(fittness)
    
    while True:
        face = int(input("face number: "))
        if face > 5 or face < 0:
            print("error bad input for face number!")
            continue
        times = int(input("times: "))
    
        cube = turn_cal(cube,face=face,times=times)
    
    
    
        print_cube(cube)
        fittness = fittness_cal(cube)
        print(fittness)

        if fittness == 100:
            play_sound.play_sound()
            break


