import numpy as np


def eigenvalues_and_eigenvectors(matrix):
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    for i in range(len(eigenvalues)):
        av = np.dot(matrix, eigenvectors[:, i])
        lv = eigenvalues[i] * eigenvectors[:, i]
        if np.allclose(av, lv):
            print(
                f"Власне значення {eigenvalues[i]} та власний вектор {eigenvectors[:, i]} задовольняють A⋅v = λ⋅v")
        else:
            print(
                f"Власне значення {eigenvalues[i]} та власний вектор {eigenvectors[:, i]} НЕ задовольняють A⋅v = λ⋅v")
    return eigenvalues, eigenvectors


matrix = np.array([[4, -2, 4],
                   [1, 1, 4],
                   [2, 1, 4]])
eigenvalues, eigenvectors = eigenvalues_and_eigenvectors(matrix)
print("Власні значення:", eigenvalues)
print("Власні вектори:", eigenvectors)
