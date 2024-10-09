# K-Means Image Compression

**K-Means Image Compression** is a Python tool that compresses images by clustering their pixels using the K-Means algorithm. The project allows users to reduce image size by adjusting the number of clusters, striking a balance between compression ratio and image quality.

## Features

- **K-Means Clustering**: Compresses images by grouping similar pixels into clusters.
- **Adjustable Cluster Size**: Users can choose the number of clusters to control the level of compression.
- **Visualization**: The compressed image is displayed at different cluster sizes for comparison.

## Getting Started

### Prerequisites

This project requires the following libraries:

- scikit-learn
- numpy
- matplotlib

Since this repository doesn't include a virtual environment, users need to create one and install the dependencies themselves.

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/nhminle/kmeans-image-compressor.git
    ```

2. Navigate to the project directory:
    ```bash
    cd kmeans-image-compressor
    ```

3. Create and activate a virtual environment:
    ```bash
    python -m venv myenv
    source myenv/bin/activate
    ```

4. Install the required dependencies:
    ```bash
    pip install scikit-learn numpy matplotlib
    ```

### Usage

1. Place your image in the project directory and name it `cityview.png`.
   
2. Run the script:
    ```bash
    python image_compressor.py
    ```

3. The script will display compressed versions of the image at different cluster sizes (e.g., 2, 5, 10, 50, 200, 500, 1000, 2000 clusters).

### Example
original image:
![original image](cityview.png)
compressed image:
![compressed image](reconstructed_image_k_2000.png)
