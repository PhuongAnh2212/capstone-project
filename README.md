# Capstone Project: "_Designing a Photorealistic Simulation Platform for Robust Semantic Segmentation in Autonomous Vehicles"_

## Overview

This repository presents a comprehensive pipeline designed to address the data scarcity challenges in autonomous driving systems. By leveraging synthetic data generation through a simulation platform, the project aims to create realistic traffic scenarios for training semantic segmentation models. The primary objective is to enhance the accuracy and robustness of traffic light detection in various driving conditions.

3 type synchronized images
|||
|-|-|
|Standard color images, as seen while creating the sequence in the editor|<img src="ReadmeContent/ColorImage.gif" alt="Color image" width="250" style="margin:10px"/>|
|Depth images, representing the depth of a pixel using a grayscale value|<img src="ReadmeContent/DepthImage.gif" alt="Depth image" width="250" style="margin:10px"/>|
|Normal images, representing pixel normals using X, Y, and Z color values|<img src="ReadmeContent/NormalImage.gif" alt="Normal image" width="250" style="margin:10px"/>|
|Optical flow images, representing pixel movement between frames using X, Y, and Z color values|<img src="ReadmeContent/OpticalFlowImage.gif" alt="Optical flow image" width="250" style="margin:10px"/>|
|Semantic images, with every object rendered using the user-defined semantic color|<img src="ReadmeContent/SemanticImage.gif" alt="Sematic image" width="250" style="margin:10px"/>|
||Model credits: [Art Equilibrium](https://www.cgtrader.com/3d-models/exterior/street/japanese-street-6278f45d-3e1e-48db-9ca6-cce343baa974)|


## Project Structure

The project is organized into the following key modules:

- **Simulation Platform**: Generates synthetic traffic scenarios using computer vision techniques.
- **Data Preprocessing**: Processes and prepares the synthetic dataset for training.
- **Model Training**: Implements semantic segmentation models to classify traffic-related objects.
- **Evaluation**: Assesses model performance and identifies areas for improvement.

## Further Research Directions

To address the challenges identified, future work will focus on:

- **Enhancing Data Balance**: Implementing advanced data augmentation and synthetic data generation techniques to balance the dataset.
- **Model Optimization**: Exploring alternative semantic segmentation architectures and loss functions to improve performance on minority classes.
- **Real-World Validation**: Testing the developed models in real-world traffic scenarios to evaluate their applicability and robustness.

## Requirements

- Python 3.x
- Jupyter Notebook
- Required Python libraries (to be listed)

## Acknowledgement
* EasySynth (https://github.com/ydrive/EasySynth/tree/main)  
