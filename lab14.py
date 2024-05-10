import numpy as np

def activation(x):
    return 1 / (1 + np.exp(-x))

def sigma_derivative(x):
    return x * (1 - x)

X = np.array([[0, 0, 1],
              [0, 1, 0],
              [1, 0, 0],
              [1, 1, 1]])

y = np.array([[0],
              [1],
              [1],
              [0]])

np.random.seed(4)

W_1_2 = 2 * np.random.random((3, 4)) - 1
W_2_3 = 2 * np.random.random((4, 5)) - 1
W_3_4 = 2 * np.random.random((5, 6)) - 1
W_4_5 = 2 * np.random.random((6, 1)) - 1

speed = 1.1

for j in range(100000):
    l1 = X
    l2 = activation(np.dot(l1, W_1_2))
    l3 = activation(np.dot(l2, W_2_3))
    l4 = activation(np.dot(l3, W_3_4))
    l5 = activation(np.dot(l4, W_4_5))
    l5_error = y - l5

    if (j % 10000) == 0:
        print("Error:" + str(np.mean(np.abs(l5_error))))

    l5_sigma = l5_error * sigma_derivative(l5)

    l4_error = l5_sigma.dot(W_4_5.T)
    l4_sigma = l4_error * sigma_derivative(l4)

    l3_error = l4_sigma.dot(W_3_4.T)
    l3_sigma = l3_error * sigma_derivative(l3)

    l2_error = l3_sigma.dot(W_2_3.T)
    l2_sigma = l2_error * sigma_derivative(l2)

    W_4_5 += speed * l4.T.dot(l5_sigma)
    W_3_4 += speed * l3.T.dot(l4_sigma)
    W_2_3 += speed * l2.T.dot(l3_sigma)
    W_1_2 += speed * l1.T.dot(l2_sigma)

X_test = np.array([[0, 0, 0],
                   [0, 1, 1],
                   [1, 0, 1],
                   [1, 1, 0],
                   [0.2, 0.2, 0],
                   [0.7, 0.7, 1]])

l1 = X_test
l2 = activation(np.dot(l1, W_1_2))
l3 = activation(np.dot(l2, W_2_3))
l4 = activation(np.dot(l3, W_3_4))
l5 = activation(np.dot(l4, W_4_5))
print(l5)
