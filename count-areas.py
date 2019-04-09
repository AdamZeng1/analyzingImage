import sys

def binary_to_array(filename):
    """
    convert base 16 binary data to integer and store the integer to a two-dimension array
    :return: two-dimensional array with lots of 255, 200, 0 which represent white pixels,grey pixels,black pixels
    """
    # width and height of the image
    size = 256
    # number of already stored data
    index = 0
    # index of x
    x = 0
    # index of y
    y = 0

    N = [[0] * size for i in range(size)]

    # get the file pointer
    f = open(filename, 'rb')

    try:
        while True:
            # read a character each time
            ch = f.read(1)
            # if reach the end of file, exit the loop
            if not ch: break

            # store the integer data
            N[x][y] = ord(ch)

            index += 1
            # if self.index % 255 == 0, it is time for next line of array
            if index % size == 0:
                # set self.x to 0, start from 0 in next line
                y = 0
                # self.y increment by 1,start in next line
                x += 1
            else:
                y += 1

    finally:
        f.close()

    # return two-dimensional array with lots of 255, 200, 0 which represent white pixels,grey pixels,black pixels
    return N


def dfs(x, y, number, color):
    """
    search from one pixels, finally find all same kind of pixels
    :param x: x of start coordinate
    :param y: y of start coordinate
    :param number: number of colored areas
    :param color: color which is searched
    :return:
    """
    sideLength = 255

    # next possible step
    nextStep = [[0, 1],  # right
                [1, 0],  # down
                [0, -1],  # left
                [-1, 0]]  # up

    # color this pixels to negative
    inputArray[x][y] = number

    # iterate four directions
    for k in range(4):
        # coordinate of next step
        tx = x + nextStep[k][0]
        ty = y + nextStep[k][1]

        # judge if it is out of bound(less than 0 or larger than sideLength
        if tx < 0 or tx > sideLength or ty < 0 or ty > sideLength:
            continue

        # if the color is wanted and this area is not used before
        if inputArray[tx][ty] == color and book[tx][ty] == 0:
            book[tx][ty] = 1
            dfs(tx, ty, number, color)

    return


if __name__ == "__main__":
    filename = sys.argv[1]

    # size of two-dimensional array
    size = int(sys.argv[3].split(',')[0])


    sys.setrecursionlimit(10000000)

    # initial a array of 255 0s
    result = [0] * 256

    # initial two-dimensional array with 0s
    book = [[0] * size for i in range(size)]

    # get two-dimensional array from the binary file 'sample.bin'
    inputArray = binary_to_array(filename)

    # number represents color
    whiteNum = 255
    greyNum = 200
    blackNum = 0

    # number of different colored areas
    numberOfWhite = 0
    numberOfGrey = 0
    numberOfBlack = 0

    # for i in range(size):
    #     for j in range(size):
    #         if inputArray[i][j] > 0:
    #             if inputArray[i][j] == blackNum:
    #                 numberOfBlack -= 1
    #                 book[i][j] = 1
    #                 dfs(i, j, numberOfBlack, blackNum)

    for i in range(size):
        for j in range(size):
            if inputArray[i][j] >= 0:
                # if it is white pixel
                if inputArray[i][j] == whiteNum:
                    numberOfWhite -= 1
                    # set the (i,j) in book
                    book[i][j] = 1
                    dfs(i, j, numberOfWhite, whiteNum)

                # if it is grey pixel
                if inputArray[i][j] == greyNum:
                    numberOfGrey -= 1
                    # set the (i,j) in book
                    book[i][j] = 1
                    dfs(i, j, numberOfGrey, greyNum)

                # if it is white pixel
                if inputArray[i][j] == blackNum:
                    numberOfBlack -= 1
                    # set the (i,j) in book
                    book[i][j] = 1
                    dfs(i, j, numberOfBlack, blackNum)

    result[whiteNum] = -numberOfWhite
    result[greyNum] = -numberOfGrey
    result[blackNum] = -numberOfBlack

    for i in result:
        print(i)
