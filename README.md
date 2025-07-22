# Computer Vision Projects: Color Detection & Object Counting

<div align="center">
  <img src="https://opencv.org/wp-content/uploads/2020/07/OpenCV_logo_black-2.png" alt="OpenCV Logo" width="200">
  <img src="https://numpy.org/images/logo.svg" alt="NumPy Logo" width="200" style="margin-left: 20px;">
</div>

This repository contains two related computer vision projects using OpenCV and NumPy:

1. **Color Tester**: Identifies and extracts specific color ranges from images/video
2. **Object Counter**: Counts objects based on detected colors in real-time

## Projects Overview

### 1. Color Tester
![Color Detection Demo](demo_color.gif) <!-- Add your gif/png here -->

A tool that:
- Detects colors within specified HSV/RGB ranges
- Creates masks for color isolation
- Works with both images and live video feed
- Adjustable sensitivity for different lighting conditions

### 2. Object Counter
![Object Counting Demo](demo_counter.gif) <!-- Add your gif/png here -->

Features:
- Real-time object counting by color
- Morphological operations for noise reduction
- Contour detection and area filtering
- Visual markers and count display

## Shared Technical Stack

<div align="center">
  <table>
    <tr>
      <th>Component</th>
      <th>Version</th>
      <th>Purpose</th>
    </tr>
    <tr>
      <td>OpenCV</td>
      <td>4.5+</td>
      <td>Image processing and computer vision</td>
    </tr>
    <tr>
      <td>NumPy</td>
      <td>1.19+</td>
      <td>Array operations and math</td>
    </tr>
    <tr>
      <td>Python</td>
      <td>3.7+</td>
      <td>Core programming language</td>
    </tr>
  </table>
</div>

## Installation

```bash
# Clone repository
git clone https://github.com/yourusername/computer-vision-projects.git
cd computer-vision-projects

# Install dependencies
pip install -r requirements.txt
