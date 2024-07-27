from typing import List
import numpy as np

def slope(point1: List[float], point2: List[float]) -> float:
    [x1, y1] = point1
    [x2, y2] = point2
    if x2 == x1:
        return 10e100
    return (y2 - y1) / (x2 - x1)

def average(current_average: float, n: int, new_num: float) -> float:
    total_sum = n * current_average
    new_average = (total_sum + new_num) / (n + 1)
    return new_average

def accuracy(num: float, avg: float) -> float:
    if avg == 0:
        return 0  # Return 0 to indicate no accuracy if the average slope is zero
    diff = abs(avg - num)
    accuracy = 1 - (diff / (abs(num) + abs(avg)))
    return accuracy

def straight_line(XY: List[List[float]]) -> float:
    if len(XY) == 2:
        return 100.0
    
    fixed_point = XY[0]
    
    for i in range(1, len(XY)):
        point = XY[i]
        current_slope = slope(fixed_point, point)
        if i == 1:
            average_slope = current_slope
            continue
        average_slope = average(average_slope, i - 1, current_slope)
        if i == 2:
            average_accuracy = accuracy(current_slope, average_slope)
            continue
        print(fixed_point , point)
        current_accuracy = accuracy(current_slope, average_slope)
        average_accuracy = average(average_accuracy, i - 2, current_accuracy)
    
    return average_accuracy * 100


def fit_circle(points):
    x = np.array([p[0] for p in points])
    y = np.array([p[1] for p in points])
    
    # Formulate matrices
    A = np.c_[x, y, np.ones(len(points))]
    b = x**2 + y**2
    
    # Solve the system of linear equations
    c, d, e = np.linalg.lstsq(A, b, rcond=None)[0]
    
    # Calculate circle parameters
    h = c / 2
    k = d / 2
    r = np.sqrt(e + h**2 + k**2)
    
    return [h, k, r]

def percentage_points_on_circle(points, h, k, r, tolerance=1e-6):
    # Count the number of points close to the circle
    count = 0
    for (x, y) in points:
        if np.isclose((x - h)**2 + (y - k)**2, r**2, atol=tolerance):
            count += 1
    # Calculate the percentage
    percentage = (count / len(points)) * 100
    return percentage


def circle(XY : List[List[float]]) -> float:
    totalLength = len(XY)
    P1 = 0
    P2 = int(totalLength * (1/3))
    P3 = int(totalLength * (2/3))

    while(P3 < totalLength):
        [h, k, r] = fit_circle([XY[P1], XY[P2], XY[P3]])

        if P1 == 0:
            average_h = h
            average_k = k
            average_r = r
            P1 += 1
            P2 += 1
            P3 += 1
            continue
        average_h = average(average_h , P1 , h)
        average_k = average(average_k , P1 , k)
        average_r = average(average_r , P1 , r)

        if P1 == 1:
            average_acurracy_h = accuracy(average_h,h)
            average_acurracy_k = accuracy(average_k,k)
            average_acurracy_r = accuracy(average_r,r)
            P1 += 1
            P2 += 1
            P3 += 1
            continue

        current_acurracy_h = accuracy(h,average_h)
        current_acurracy_k = accuracy(h,average_k)
        current_acurracy_r = accuracy(h,average_r)

        average_acurracy_h = average(average_acurracy_h, P1 - 1, current_acurracy_h)
        average_acurracy_k = average(average_acurracy_k, P1 - 1, current_acurracy_k)
        average_acurracy_r = average(average_acurracy_r, P1 - 1, current_acurracy_r)

        P1 += 1
        P2 += 1
        P3 += 1


    return (average_acurracy_h + average_acurracy_k + average_acurracy_r)/3



# Example points
points = [(-4,0), (4,0), (0,4)  , (0,-4)]
print(circle(points))

# # Fit circle to points
# h, k, r = fit_circle(points)

# # Calculate the percentage of points close to the circle
# percentage = percentage_points_on_circle(points, h, k, r)
# print("Percentage of points close to the circle:", percentage)