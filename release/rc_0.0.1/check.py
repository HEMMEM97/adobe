from typing import List

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

L = [[1,4] , [5,2] , [5,4]  , [9,4]]
print(straight_line(L))