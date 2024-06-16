import numpy as np
from matplotlib.image import imread
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

image_raw = imread('image.jpeg')
print(f'Початкове зображення: розмір {image_raw.shape}')

image_sum = image_raw.sum(axis=2)
image_bw = image_sum / image_sum.max()
print(image_bw.max())

pca = PCA()
pca.fit(image_bw)
cumulative_variance = np.cumsum(pca.explained_variance_ratio_)

n_components_95 = np.argmax(cumulative_variance >= 0.95) + 1
print(f'Кількість компонент для покриття 95% дисперсії: {n_components_95}')

plt.figure(figsize=(11, 7))
plt.plot(cumulative_variance, marker='o')
plt.axhline(y=0.95, color='r', linestyle='--')
plt.axvline(x=n_components_95, color='r', linestyle='--')
plt.xlabel('Pincipal components')
plt.ylabel('Cumulative Explained variance')
plt.title('Cumulative Explained Variance explained by the components')
plt.grid()
plt.show()


def apply_pca(image, n_components):
    pca = PCA(n_components=n_components)
    transformed = pca.fit_transform(image)
    reconstructed = pca.inverse_transform(transformed)
    return reconstructed


components_list = [5, 15, 25, 75, 150, n_components_95]

fig, axs = plt.subplots(2, 3, figsize=(20, 10))
axs = axs.flatten()


for i, n in enumerate(components_list):
    reconstructed_image = apply_pca(image_bw, n)
    axs[i].imshow(reconstructed_image, cmap='gray')
    axs[i].set_title(f'{n} компонент')

plt.tight_layout(pad=10.0, w_pad=10.0, h_pad=4.0)
plt.subplots_adjust(right=0.95, top=0.95)
plt.show()
