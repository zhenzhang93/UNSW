import operator
import copy
import math
from functools import reduce


# the program may have mutiplied judge
# which may slow down the runtime
# should write a single funciton to judge whether a single point inside


def available_coloured_pieces(file):
    contents = file.read()
    # print(contents)
    contents = contents.replace("/>", "")
    contents = contents.replace("\n", "")
    contents = contents.replace("</svg>", "")
    a = contents.split("<path ")[1:]
    # print(a)
    # a is every sentence
    dic = {}
    # store the color and its points
    for i in a:
        points = []
        i = i.strip()
        number = i.split(" ")
        for j in number:
            if j.isdigit():
                points.append(j)
        dic[number[-1]] = points
    # print(dic)
    for i in dic:
        res = []
        for index in range(len(dic[i])):
            if index % 2 == 1:
                res.append([int(dic[i][index - 1]), int(dic[i][index])])
        dic[i] = res
    # print(dic)

    return dic


def clockwise(a, b):
    difference = a[0] * b[1] - a[1] * b[0]
    # reverse clockwise
    if (difference > 0):
        return 1
    # clockwise
    if (difference < 0):
        return -1
    # same point
    else:
        return False


# judge all points are in the same side of one line
def onside(line, point):
    x1 = line[0]
    x2 = line[2]
    y1 = line[1]
    y2 = line[3]
    x = point[0]
    y = point[1]
    # if (x1 * y2 - x2 * y1 == 0):

    # return False
    # y-y1/x-x1=y2-y1/x2-x1
    result = x * (y2 - y1) + y * (x1 - x2) - x1 * y2 + x2 * y1
    # print(result)
    if result == 0:
        # point on the line
        return False
    if result > 0:
        return 1
    else:
        return -1


# the points set has two same point
def has_samepoint(points):
    for i in range(len(points) - 1):
        for k in range(i + 1, len(points)):
            if operator.eq(points[i], points[k]):
                return False
    return True


# poins is a list,store single points
def single_valid(points):
    # have same point
    if not has_samepoint(points):
        return False
    finalres = []
    for i in range(len(points) - 1):
        # print(points[i] + [1])
        j = i + 1
        # print(points[j] + [2])
        templine = points[i] + points[j]
        tempres = []
        # print(templine)
        for k in range(len(points)):
            if (not points[k].__eq__(points[i])) and (not points[k].__eq__(points[j])):
                # print(points[k] + [3])
                res = onside(templine, points[k])
                if res == False:
                    return False
                else:
                    tempres.append(res)
        # print(tempres)
        if (len(set(tempres)) == 1):
            finalres.append(True)
        else:
            return False

    if (len(set(finalres)) == 1):
        return True
    else:
        return False


# res =all(onside(templine, points[k]) for k in range(len(points)) if (not k.__eq__(i)) or (not k.__eq__(j)))


# coloured_pieces is a dic
def are_valid(coloured_pieces):
    return all(single_valid(coloured_pieces[key]) for key in coloured_pieces)


# coloured_pieces = available_coloured_pieces(file)


# print(are_valid(coloured_pieces))

def all_edge(points):
    res = []
    for i in range(len(points) - 1):
        x1 = points[i][0]
        y1 = points[i][1]
        x2 = points[i + 1][0]
        y2 = points[i + 1][1]
        res.append(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2))
    x1 = points[-1][0]
    y1 = points[-1][1]
    x2 = points[0][0]
    y2 = points[0][1]
    res.append(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2))
    return res


def edge_same(points1, points2):
    res1 = all_edge(points1)
    res2 = all_edge(points2)
    return has_same_point(res1, res2)


def to_origin(points):
    newpoints = copy.deepcopy(points)
    x = newpoints[0][0]
    y = newpoints[0][1]
    # print(x, y)
    for i in range(len(newpoints)):
        newpoints[i][0], newpoints[i][1] = \
            points[i][0] - x, points[i][1] - y

    return newpoints


# every points become the origin
def become_origin(points):
    # all possible situations
    res = []
    for point in points:
        newpoints = copy.deepcopy(points)
        # print(point)
        x = point[0]
        y = point[1]
        for i in range(len(newpoints)):
            # print(x, y)
            newpoints[i][0], newpoints[i][1] = points[i][0] - x, points[i][1] - y
        res.append(copy.deepcopy(newpoints))

    return res


def has_same_point(points1, points2):
    length = 0
    for i in points1:
        if (i in points2):
            length += 1
    return length == len(points1)


# following functions can rotate all direction
def reverse_points(points):
    newpoints = copy.deepcopy(points)
    for i in range(len(newpoints)):
        newpoints[i][0], newpoints[i][1] = points[i][1], points[i][0]
    return newpoints


def reverseorigin_points(points):
    newpoints = copy.deepcopy(points)
    for i in range(len(newpoints)):
        newpoints[i][0], newpoints[i][1] = -1 * points[i][0], -1 * points[i][0]
    return newpoints


def turn180_x(points):
    newpoints = copy.deepcopy(points)
    for i in range(len(newpoints)):
        newpoints[i][0], newpoints[i][1] = -1 * points[i][0], points[i][1]
    return newpoints


def turn180_y(points):
    newpoints = copy.deepcopy(points)
    for i in range(len(newpoints)):
        newpoints[i][0], newpoints[i][1] = points[i][0], -1 * points[i][1]
    return newpoints


# rotate first
# if mathch,means true
# then move

def singgle_same(points1, points2):
    if (len(points1) != len(points2)):
        return False
    if (operator.eq(points1, points2)):
        return True
    else:
        # pos = to_origin(points1)
        p1_possible = become_origin(points1)
        p2_possible = become_origin(points2)
        for pos in p1_possible:
            for points in p2_possible:
                if (operator.eq(pos, points)) or has_same_point(pos, points):
                    return True
            rotx = turn180_x(points2)
            all_possiblex = become_origin(rotx)
            for points in all_possiblex:
                # print(points)
                if (operator.eq(pos, points)) or has_same_point(pos, points):
                    return True
            roty = turn180_y(points2)
            all_possibley = become_origin(roty)
            for points in all_possibley:
                # print(points)
                if (operator.eq(pos, points)) or has_same_point(pos, points):
                    return True

            rotxy = turn180_y(rotx)
            all_possiblexy = become_origin(rotxy)
            for points in all_possiblexy:
                # print(points)
                if (operator.eq(pos, points)) or has_same_point(pos, points):
                    return True

            rotyx = turn180_y(roty)
            all_possibleyx = become_origin(rotyx)
            for points in all_possibleyx:
                # print(points)
                if (operator.eq(pos, points)) or has_same_point(pos, points):
                    return True
            symetry = reverse_points(points2)
            all_possible_symetry = become_origin(symetry)
            for points in all_possible_symetry:
                if (operator.eq(pos, points)) or has_same_point(pos, points):
                    return True
            symetry_x = turn180_x(symetry)
            all_possible_symetry_x = become_origin(symetry_x)
            for points in all_possible_symetry_x:
                if (operator.eq(pos, points)) or has_same_point(pos, points):
                    return True
            symetry_y = turn180_y(symetry)
            all_possible_symetry_y = become_origin(symetry_y)
            for points in all_possible_symetry_y:
                if (operator.eq(pos, points)) or has_same_point(pos, points):
                    return True
            symetry_xy = turn180_y(symetry_x)
            all_possible_symetry_xy = become_origin(symetry_xy)
            for points in all_possible_symetry_xy:
                if (operator.eq(pos, points)) or has_same_point(pos, points):
                    return True
            symetry_yx = turn180_x(symetry_y)
            all_possible_symetry_yx = become_origin(symetry_yx)
            for points in all_possible_symetry_yx:
                if (operator.eq(pos, points)) or has_same_point(pos, points):
                    return True

            origin = reverseorigin_points(points2)
            all_possible_origin = become_origin(origin)
            for points in all_possible_origin:
                if (operator.eq(pos, points)) or has_same_point(pos, points):
                    return True
            origin_x = turn180_x(origin)
            all_possible_origin_x = become_origin(origin_x)
            for points in all_possible_origin_x:
                if (operator.eq(pos, points)) or has_same_point(pos, points):
                    return True
            origin_y = turn180_y(origin)
            all_possible_origin_y = become_origin(origin_y)
            for points in all_possible_origin_y:
                if (operator.eq(pos, points)) or has_same_point(pos, points):
                    return True
        return False


def are_identical_sets_of_coloured_pieces(coloured_pieces_1, coloured_pieces_2):
    if len(coloured_pieces_1) != len(coloured_pieces_2):
        return False
    if not are_valid(coloured_pieces_1) or not are_valid(coloured_pieces_2):
        return False
    length=len(coloured_pieces_1)

    num = 0
    for key1 in coloured_pieces_1:
        for key2 in coloured_pieces_2:
            if (key1 == key2):
                num +=1
                if (not singgle_same(coloured_pieces_1[key1], coloured_pieces_2[key2])):
                    return False
    if(num !=length):
        return False
    return True


# s=1/2*[(x1*y2-x2*y1)+(x2*y3-x3*y2)+...... +(Xk*Yk+1-Xk+1*Yk)+...+(Xn*y1-x1*Yn) ]
def calculate_area(points):
    area = 0
    for i in range(len(points) - 1):
        area += 0.5 * (points[i][0] * points[i + 1][1] - points[i + 1][0] * points[i][1])

    area += 0.5 * (points[-1][0] * points[0][1] - points[-1][1] * points[0][0])
    return abs(area)


def cal_one_shape(shape):
    area_shape = 0
    for key in shape:
        area_shape += calculate_area(shape[key])
    return area_shape


def same_area(trangram, shape):
    area_shape = 0
    for key in shape:
        area_shape += calculate_area(shape[key])
    trangram_shape = 0
    for key in trangram:
        trangram_shape += calculate_area(trangram[key])
    # print(area_shape,trangram_shape)
    return area_shape == trangram_shape


# whether the points is in the shape(points is the point of a piece,like triangle)
# points like [[30, 20], [110, 20], [30, 120]]
# trangram is the shape, like [[30, 20], [110, 20], [110, 120], [30, 120]]
# return True if in the shape
def in_trangram(trangram, points):
    temp = []
    for key in trangram:
        x_min = reduce(min, [i[0] for i in trangram[key]])
        x_max = reduce(max, [i[0] for i in trangram[key]])
        y_min = reduce(min, [i[1] for i in trangram[key]])
        y_max = reduce(max, [i[1] for i in trangram[key]])
        temp.append(x_min)
        temp.append(x_max)
        temp.append(y_min)
        temp.append(y_max)
    # print(temp)
    # all points of a polygon in this trangram.
    for point in points:
        # print(point)
        if point[0] < temp[0] or point[1] < temp[2] or \
                point[0] > temp[1] or point[1] > temp[3]:
            return False

    for key in trangram:
        length = len(trangram[key])
        if (length < 3):
            return False
        value = trangram[key]
        for point in points:
            num = 0
            y = point[1]
            flag = True
            for i in range(len(trangram[key])):
                # print(y,point[0])
                # point is the vertex
                if (value[i % length][0] == point[0] and value[i % length][1] == y):
                    flag = False
                    break

                # if on point under a vertical line
                if (point[0] == value[i % length][0] and point[0] == value[(i + 1) % length][0]
                        and (point[1] < min(value[i % length][1], value[(i + 1) % length][1]) or
                             point[1] > max(value[i % length][1], value[(i + 1) % length][1]))):
                    continue
                if (value[(i + 1) % length][1] - value[i % length][1] == 0):
                    if (y == value[i % length][1] and point[0] >= min(value[i % length][0], value[(i + 1) % length][0])
                            and point[0] <= max(value[i % length][0], value[(i + 1) % length][0])):
                        flag = False
                        break
                    else:
                        continue
                # y2-y1  /  x2-x1=y-y1  /  x-x1,on the line
                if (value[(i + 1) % length][0] - value[i % length][0]) * (y - value[i % length][1]) == \
                        (value[(i + 1) % length][1] - value[i % length][1]) * (point[0] - value[i % length][0]):
                    flag = False
                    break

                x = (y - value[i % length][1]) * (value[(i + 1) % length][0] - value[i % length][0]) / \
                    (value[(i + 1) % length][1] - value[i % length][1]) + value[i % length][0]
                # print(x, point[0])
                # inside or on the line
                if (x <= max(value[(i + 1) % length][0], value[(i) % length][0]) and
                        y <= max(value[(i + 1) % length][1], value[(i) % length][1]) and
                        y > min(value[(i + 1) % length][1], value[(i) % length][1])):
                    if (x > point[0]):
                        num += 1
            # %2 =0 means outside
            if (flag):
                # print(num)
                if (num % 2 == 0):
                    return False
                # outside,but still have one intersection point
    return True


def in_trangram_without_key(trangram, points):
    temp = []
    x_min = reduce(min, [i[0] for i in trangram])
    x_max = reduce(max, [i[0] for i in trangram])
    y_min = reduce(min, [i[1] for i in trangram])
    y_max = reduce(max, [i[1] for i in trangram])
    temp.append(x_min)
    temp.append(x_max)
    temp.append(y_min)
    temp.append(y_max)
    for point in points:
        if point[0] < temp[0] or point[1] < temp[2] or \
                point[0] > temp[1] or point[1] > temp[3]:
            return False

        length = len(trangram)
        value = trangram
        for point in points:
            num = 0
            y = point[1]
            flag = True
            for i in range(len(trangram)):
                # print(y,point[0])
                # point is the vertex
                if (value[i % length][0] == point[0] and value[i % length][1] == y):
                    flag = False
                    break

                # if on point under a vertical line
                if (point[0] == value[i % length][0] and point[0] == value[(i + 1) % length][0]
                        and (point[1] < min(value[i % length][1], value[(i + 1) % length][1]) or
                             point[1] > max(value[i % length][1], value[(i + 1) % length][1]))):
                    continue
                    # parallel to x
                if (value[(i + 1) % length][1] - value[i % length][1] == 0):
                    if (y == value[i % length][1] and point[0] >= min(value[i % length][0], value[(i + 1) % length][0])
                            and point[0] <= max(value[i % length][0], value[(i + 1) % length][0])):
                        flag = False
                        break
                    else:
                        continue

                # y2-y1  /  x2-x1=y-y1  /  x-x1,on the line
                if (value[(i + 1) % length][0] - value[i % length][0]) * (y - value[i % length][1]) == \
                        (value[(i + 1) % length][1] - value[i % length][1]) * (point[0] - value[i % length][0]):
                    flag = False
                    break
                """
                # parallel to x
                if (value[(i + 1) % length][1] - value[i % length][1] == 0):
                    continue
                    
                """
                x = (y - value[i % length][1]) * (value[(i + 1) % length][0] - value[i % length][0]) / \
                    (value[(i + 1) % length][1] - value[i % length][1]) + value[i % length][0]
                # print(x, point[0])
                # inside or on the line
                if (x <= max(value[(i + 1) % length][0], value[(i) % length][0]) and
                        y <= max(value[(i + 1) % length][1], value[(i) % length][1]) and
                        y > min(value[(i + 1) % length][1], value[(i) % length][1])):
                    if (x > point[0]):
                        num += 1
            # %2 =0 means outside
            if (flag):
                # print(num)
                if (num % 2 == 0):
                    return False
                # outside,but still have one intersection point
    return True


# trangram, like[[30, 60], [30, 20], [70, 20]]
# and [[50, 120], [50, 80], [70, 60], [90, 80], [90, 120]]

# this is to deal with the case the person give
# the shape_f.xml
# return False if it do not match,means have problem
def all_point_match_shape(trangram, shape):
    vertex_trangram = []
    vertex_shape = []
    for key in trangram:
        for i in trangram[key]:
            vertex_trangram.append(i)

    for key in shape:
        for i in shape[key]:
            vertex_shape.append(i)
    for item in vertex_shape:
        flag = True
        for i in range(len(vertex_trangram)):
            if (item == vertex_trangram[i]):
                flag = False
                break
        if (flag == True):
            return False
    return True


# some points on the pologon ,but its edge is outside
# this method is to avoid this case.
# judge one point of this edge is inside the pologon
# return false if it outside
def is_edge_outside(shape, points):
    value = []
    for key in shape:
        value = shape[key]
    length = len(value)
    # print(length)
    for i in range(length):
        line1 = [value[i % length], value[(i + 1) % length]]
        if (line_cross(line1, points)):
            return False

    x1 = points[0][0]
    x2 = points[1][0]
    y1 = points[0][1]
    y2 = points[1][1]
    midx = min(x1, x2) + abs((x2 - x1)) / 2
    midy = min(y1, y2) + abs((y2 - y1)) / 2

    # y-y1/x-x1=y2-y1/x2-x1
    newpoint = [midx, midy]
    # print(newpoint)
    # newpoint not in the shape,judge the middle point in the shape
    new1 = [newpoint, points[0]]
    new2 = [newpoint, points[1]]
    # print(new1)
    # print(points)
    if (not in_trangram(shape, new1)):
        # print(new1)
        return False
    if (not in_trangram(shape, new2)):
        return False

    return True


# using similar way to judge point inside a polygon
# return True if overlap(has line cross)
# another function consider polygon in another
# if points on the line, it is overlap


# need add something more, becasue line cross in not the only situation.
def is_overlap(piece1, piece2):
    length1 = len(piece1)
    length2 = len(piece2)
    for i in range(length1):
        line1 = [piece1[i % length1], piece1[(i + 1) % length1]]
        # print(line1)
        for j in range(length2):
            line2 = [piece2[j % length2], piece2[(j + 1) % length2]]
            # print(line2)
            if (line_cross(line1, line2)):
                return True

    # they are parallel but overlap
    """
     ___________
    |____|__|___|
    like this 
    """
    for j in range(length2):
        line2 = [piece2[j % length2], piece2[(j + 1) % length2]]
        if (in_trangram_without_key(piece1, line2)):
            # means overlap
            point1 = line2[0]
            point2 = line2[1]
            oneline = 0
            difline = 0
            for i in range(length1):
                # two points on the one line
                line1 = [piece1[i % length1], piece1[(i + 1) % length1]]
                if (point_on_the_line(line1, point1) and point_on_the_line(line1, point2)):
                    oneline += 1
                if (point_on_the_line(line1, point1) and not point_on_the_line(line1, point2)):
                    difline += 1
                if (not point_on_the_line(line1, point1) and point_on_the_line(line1, point2)):
                    difline += 1
            if (difline != 0 and oneline == 0):
                return True
    return False


# y2-y1  /  x2-x1=y-y1  /  x-x1,on the line
# return True if on the line

def point_on_the_line(line, point):
    y = point[1]
    x = point[0]
    if (line[1][0] - line[0][0]) * (y - line[0][1]) == \
            (line[1][1] - line[0][1]) * (x - line[0][0]):
        return True

    return False


# return True, if pieces in another poloygon
# return Flase, if do not have inside
def polygon_inanother(trangram):
    for key in trangram:
        newdic = {}
        newdic[key] = trangram[key]
        # print(newdic)
        for j in trangram:
            if (key == j):
                continue
            if in_trangram(newdic, trangram[j]):
                # print(newdic, trangram[j])
                return True
    return False


# two points,become a line
# there are only for ponits
# four points, two is a pair
def cross(points1, points2):
    return points1[0] * points2[1] - points1[1] * points2[0]


# return True, if they cross
def line_cross(points1, points2):
    acy = points2[0][1] - points1[0][1]
    acx = points2[0][0] - points1[0][0]
    ady = points2[1][1] - points1[0][1]
    adx = points2[1][0] - points1[0][0]

    bcy = points2[0][1] - points1[1][1]
    bcx = points2[0][0] - points1[1][0]
    bdx = points2[1][0] - points1[1][0]
    bdy = points2[1][1] - points1[1][1]

    cax = points1[0][0] - points2[0][0]
    cay = points1[0][1] - points2[0][1]
    cbx = points1[1][0] - points2[0][0]
    cby = points1[1][1] - points2[0][1]

    dax = points1[0][0] - points2[1][0]
    day = points1[0][1] - points2[1][1]
    dbx = points1[1][0] - points2[1][0]
    dby = points1[1][1] - points2[1][1]
    # print(cross([acx, acy], [adx, ady]) * cross([bcx, bcy], [bdx, bdy]))
    # do no consider the point is on the line
    return cross([acx, acy], [adx, ady]) * cross([bcx, bcy], [bdx, bdy]) < 0 \
           and cross([cax, cay], [cbx, cby]) * cross([dax, day], [dbx, dby]) < 0




# return True if do not have overlap
# return Flase if have overlap
def trangram_overlap(trangram):
    for key in trangram:
        for key1 in trangram:
            if key != key1:
                # has overlap
                if (is_overlap(trangram[key], trangram[key1])):
                    #print(trangram[key], trangram[key1])
                    return False
    return True


def is_solution(trangram, shape):
    if (len(shape) > 1):
        #print("3")
        return False
    if (not same_area(trangram, shape)):
        #print("4")
        return False
    if (not are_valid(trangram)):
        #print("5")
        return False
    # whether point in the trangram
    for key in trangram:
        # print(trangram[key])
        if (not in_trangram(shape, trangram[key])):
            #print("6")
            return False
    if (not trangram_overlap(trangram)):
        #print("1")
        return False
    if (polygon_inanother(trangram)):
        #print("2")
        return False
    if (not all_point_match_shape(trangram, shape)):
        #print("9")
        return False

    for key in trangram:
        length = len(trangram[key])
        for i in range(len(trangram[key])):
            newpoint = [trangram[key][i % length], trangram[key][(i + 1) % length]]
            if (not is_edge_outside(shape, newpoint)):
                # print(shape, newpoint)
                return False

    return True


