from enum import StrEnum

class Faces(StrEnum):
    Front = "Front"
    Back = "Back"
    Left = "Left"
    Right = "Right"
    Top = "Top"
    Bottom = "Bottom"

class RubiksCube:
    def __init__(self):
        self.cube = dict()
        self.__constructRubiksCube()
    
    # Private function to construct a face of the cube with a colour
    def __constructFace(self, colour):
        face = []
        cell_num = 1 # Tracks cell number
        for row in range(3):
            # New array for each row of face
            face.insert(row, [])
            for col in range(3):
                face[row].insert(col, colour + str(cell_num))
                cell_num += 1
        return face

    # Private function to construct each face of the cube
    def __constructRubiksCube(self):
        self.cube[Faces.Front] = self.__constructFace("G")
        self.cube[Faces.Back] = self.__constructFace("B")
        self.cube[Faces.Left] = self.__constructFace("O")
        self.cube[Faces.Right] = self.__constructFace("R")
        self.cube[Faces.Top] = self.__constructFace("W")
        self.cube[Faces.Bottom] = self.__constructFace("Y")
    
    # Private function to print a face of the cube
    def __printFace(self, face, face_values):
        print(face + ":")
        for row in face_values:
            print(row)
        print()

    # Print all faces of the cube with labels, e.g. Front: ...
    def printCube(self):
        for face, face_values in self.cube.items():
            self.__printFace(face, face_values)
    
    # Pretty print an exploded view of the cube
    def explodedPrint(self):
        indent = "\t\t " # Indent for top/bottom faces
        # Prints top face
        topSection = self.cube[Faces.Top]
        for row in topSection:
            print(indent, row)
        # Prints left, front, right and back faces
        middleSection = []
        middleSection.append(self.cube[Faces.Left])
        middleSection.append(self.cube[Faces.Front])
        middleSection.append(self.cube[Faces.Right])
        middleSection.append(self.cube[Faces.Back])
        for i in range(3):
            for face in middleSection:
                print(face[i], end="")
            print()
        # Prints bottom face
        bottomSection = self.cube[Faces.Bottom]
        for row in bottomSection:
            print(indent, row)
    
    # Private function to rotate only the current face clockwise
    # Excludes rotation of adjacent faces
    def __rotateFaceClockwise(self, face):
        curr_face = self.cube[face]
        # 1. Rotate corners cubes
        temp_cell = curr_face[0][0]
        curr_face[0][0] = curr_face[2][0]
        curr_face[2][0] = curr_face[2][2]
        curr_face[2][2] = curr_face[0][2]
        curr_face[0][2] = temp_cell

        # 2. Rotate edge cubes
        temp_cell = curr_face[0][1]
        curr_face[0][1] = curr_face[1][0]
        curr_face[1][0] = curr_face[2][1]
        curr_face[2][1] = curr_face[1][2]
        curr_face[1][2] = temp_cell

    # Private function to rotate only the current face anticlockwise
    # Excludes rotation of adjacent faces
    def __rotateFaceAntiClockwise(self, face):
        curr_face = self.cube[face]
        # 1. Rotate corners cubes
        temp_cell = curr_face[0][0]
        curr_face[0][0] = curr_face[0][2]
        curr_face[0][2] = curr_face[2][2]
        curr_face[2][2] = curr_face[2][0]
        curr_face[2][0] = temp_cell

        # 2. Rotate edge cubes
        temp_cell = curr_face[0][1]
        curr_face[0][1] = curr_face[1][2]
        curr_face[1][2] = curr_face[2][1]
        curr_face[2][1] = curr_face[1][0]
        curr_face[1][0] = temp_cell


    # Which faces correspond to which other faces:
        # Front/Back face -> Top, Right, Left, Bottom faces
        # Left/Right face -> Front, Back, Top, Bottom faces
        # Top/Bottom face -> Left, Right, Front, Back faces

    # Rotating front face and adjacent faces
    def rotateFrontClockwise(self):
        self.__rotateFaceClockwise(Faces.Front)
        temp_cells = [self.cube[Faces.Top][2][i] for i in range(3)]
        for i in range(3):
            self.cube[Faces.Top][2][i] = self.cube[Faces.Left][2 - i][2]
            self.cube[Faces.Left][2 - i][2] = self.cube[Faces.Bottom][0][2 - i]
            self.cube[Faces.Bottom][0][2 - i] = self.cube[Faces.Right][i][0]
            self.cube[Faces.Right][i][0] = temp_cells[i]

    def rotateFrontAntiClockwise(self):
        self.__rotateFaceAntiClockwise(Faces.Front)
        temp_cells = [self.cube[Faces.Top][2][i] for i in range(3)]
        for i in range(3):
            self.cube[Faces.Top][2][i] = self.cube[Faces.Right][i][0]
            self.cube[Faces.Right][i][0] = self.cube[Faces.Bottom][0][2 - i]
            self.cube[Faces.Bottom][0][2 - i] = self.cube[Faces.Left][2 - i][2]
            self.cube[Faces.Left][2 - i][2] = temp_cells[i]

    # Rotating back face and adjacent faces
    def rotateBackClockwise(self):
        self.__rotateFaceClockwise(Faces.Back)
        temp_cells = [self.cube[Faces.Top][0][i] for i in range(3)]
        for i in range(3):
            self.cube[Faces.Top][0][i] = self.cube[Faces.Right][i][2]
            self.cube[Faces.Right][i][2] = self.cube[Faces.Bottom][2][2 - i]
            self.cube[Faces.Bottom][2][2 - i] = self.cube[Faces.Left][2- i][0]
            self.cube[Faces.Left][2 - i][0] = temp_cells[i]

    def rotateBackAntiClockwise(self):
        self.__rotateFaceAntiClockwise(Faces.Back)
        temp_cells = [self.cube[Faces.Top][0][i] for i in range(3)]
        for i in range(3):
            self.cube[Faces.Top][0][i] = self.cube[Faces.Left][2 - i][0]
            self.cube[Faces.Left][2 - i][0] = self.cube[Faces.Bottom][2][2 - i]
            self.cube[Faces.Bottom][2][2 - i] = self.cube[Faces.Right][i][2]
            self.cube[Faces.Right][i][2] = temp_cells[i]

    # Rotating left face and adjacent faces
    def rotateLeftClockwise(self):
        self.__rotateFaceClockwise(Faces.Left)
        temp_cells = [self.cube[Faces.Top][i][0] for i in range(3)]
        for i in range(3):
            self.cube[Faces.Top][i][0] = self.cube[Faces.Back][2 - i][2]
            self.cube[Faces.Back][2 - i][2] = self.cube[Faces.Bottom][i][0]
            self.cube[Faces.Bottom][i][0] = self.cube[Faces.Front][i][0]
            self.cube[Faces.Front][i][0] = temp_cells[i]
    
    def rotateLeftAntiClockwise(self):
        self.__rotateFaceAntiClockwise(Faces.Left)
        temp_cells = [self.cube[Faces.Top][i][0] for i in range(3)]
        for i in range(3):
            self.cube[Faces.Top][i][0] = self.cube[Faces.Front][i][0]
            self.cube[Faces.Front][i][0] = self.cube[Faces.Bottom][i][0]
            self.cube[Faces.Bottom][i][0] = self.cube[Faces.Back][2 - i][2]
            self.cube[Faces.Back][2 - i][2] = temp_cells[i]

    # Rotating right face and adjacent faces
    def rotateRightClockwise(self):
        self.__rotateFaceClockwise(Faces.Right)
        temp_cells = [self.cube[Faces.Top][i][2] for i in range(3)]
        for i in range(3):
            self.cube[Faces.Top][i][2] = self.cube[Faces.Front][i][2]
            self.cube[Faces.Front][i][2] = self.cube[Faces.Bottom][i][2]
            self.cube[Faces.Bottom][i][2] = self.cube[Faces.Back][2 - i][0]
            self.cube[Faces.Back][2 - i][0] = temp_cells[i]

    def rotateRightAntiClockwise(self):
        self.__rotateFaceAntiClockwise(Faces.Right)
        temp_cells = [self.cube[Faces.Top][i][2] for i in range(3)]
        for i in range(3):
            self.cube[Faces.Top][i][2] = self.cube[Faces.Back][2 - i][0]
            self.cube[Faces.Back][2 - i][0] = self.cube[Faces.Bottom][i][2]
            self.cube[Faces.Bottom][i][2] = self.cube[Faces.Front][i][2]
            self.cube[Faces.Front][i][2] = temp_cells[i]

    # Rotating top face and adjacent faces
    def rotateTopClockwise(self):
        self.__rotateFaceClockwise(Faces.Top)
        temp = self.cube[Faces.Front][0]
        self.cube[Faces.Front][0] = self.cube[Faces.Right][0]
        self.cube[Faces.Right][0] = self.cube[Faces.Back][0]
        self.cube[Faces.Back][0] = self.cube[Faces.Left][0]
        self.cube[Faces.Left][0] = temp

    def rotateTopAntiClockwise(self):
        self.__rotateFaceAntiClockwise(Faces.Top)
        temp = self.cube[Faces.Front][0]
        self.cube[Faces.Front][0] = self.cube[Faces.Left][0]
        self.cube[Faces.Left][0] = self.cube[Faces.Back][0]
        self.cube[Faces.Back][0] = self.cube[Faces.Right][0]
        self.cube[Faces.Right][0] = temp

    # Rotating bottom face and adjacent faces
    def rotateBottomClockwise(self):
        self.__rotateFaceClockwise(Faces.Bottom)
        temp = self.cube[Faces.Front][2]
        self.cube[Faces.Front][2] = self.cube[Faces.Left][2]
        self.cube[Faces.Left][2] = self.cube[Faces.Back][2]
        self.cube[Faces.Back][2] = self.cube[Faces.Right][2]
        self.cube[Faces.Right][2] = temp

    def rotateBottomAntiClockwise(self):
        self.__rotateFaceAntiClockwise(Faces.Bottom)
        temp = self.cube[Faces.Front][2]
        self.cube[Faces.Front][2] = self.cube[Faces.Right][2]
        self.cube[Faces.Right][2] = self.cube[Faces.Back][2]
        self.cube[Faces.Back][2] = self.cube[Faces.Left][2]
        self.cube[Faces.Left][2] = temp

if __name__ == "__main__":
    '''
    Possible rotations available:
    - cube.rotateFrontClockwise()
    - cube.rotateFrontAntiClockwise()
    - cube.rotateBackClockwise()
    - cube.rotateBackAntiClockwise()
    - cube.rotateLeftClockwise()
    - cube.rotateLeftAntiClockwise()
    - cube.rotateRightClockwise()
    - cube.rotateRightAntiClockwise()
    - cube.rotateTopClockwise()
    - cube.rotateTopAntiClockwise()
    - cube.rotateBottomClockwise()
    - cube.rotateBottomAntiClockwise()

    Possible print functions:
    # Prints an exploded view of the function
    - explodedPrint()
    # Prints each face separately with labels
    - printCube()
    '''

    cube = RubiksCube()
    # Modify the BELOW code to change the Rubik's Cube

    cube.rotateFrontClockwise()
    cube.rotateRightAntiClockwise()
    cube.rotateTopClockwise()
    cube.rotateBackAntiClockwise()
    cube.rotateLeftClockwise()
    cube.rotateBottomAntiClockwise()

    # Modify the ABOVE code to change the Rubik's Cube

    cube.explodedPrint()