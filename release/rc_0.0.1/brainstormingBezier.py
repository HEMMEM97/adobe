import numpy as np
import matplotlib.pyplot as plt

def bezierPoint(P1 : np.ndarray, P2 : np.ndarray, t : float) -> np.ndarray:
    XB = P1[0] + t * (P2[0] - P1[0])
    YB = P1[1] + t * (P2[1] - P1[1])

    return np.array([XB,YB])

def quadraticBezierPoint(P0: np.ndarray, P1: np.ndarray, P2: np.ndarray, t : float) -> np.ndarray:
    B = (1-t)**2 * P0 + 2 * (1-t) * t * P1 + t**2 * P2
    return B

def cubicBezierPoint(P0: np.ndarray, P1: np.ndarray, P2: np.ndarray, P3: np.ndarray, t: float) -> np.ndarray:
    B = (1-t)**3 * P0 + 3 * (1-t)**2 * t * P1 + 3 * (1-t) * t**2 * P2 + t**3 * P3
    return B


XYP0 = np.array([0,-4])
XYP1 = np.array([4,0])
XYP2 = np.array([0,4])
XYP3 = np.array([5,7])

x_values = []
y_values = []

for i in range(1000):

    t = i / 999

    # XYB = bezierPoint(bezierPoint(XYP0, XYP1, 0.1 * i), bezierPoint(XYP1, XYP2, 0.1 * i), 0.1 * i)  
    # XYB = quadraticBezierPoint(XYP0, XYP1, XYP3, t) 
    # XYB1 = quadraticBezierPoint(XYP1, XYP2, XYP3, 0.01 * i)

    XYB = bezierPoint(XYP0, XYP3, t ) 

    # XYB = cubicBezierPoint(XYP0, XYP1, XYP2, XYP3, t)



    x_values.append(XYB[0])
    y_values.append(XYB[1])
    print(XYB)


plt.plot(x_values, y_values, 'b-o')
# plt.scatter(XYP1[0], XYP1[1], color = 'black')
# plt.scatter(XYP2[0], XYP2[1], color = 'black')

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Bezier Points')
plt.grid(True)
plt.show()