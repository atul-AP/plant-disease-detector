# plant-disease-detector

# Plant Disease Detector

It is a web-enabled Plant Disease Detector built with a machine learning backend to classify images of plant leaves as healthy or diseased. It is created using Python and Streamlit and has a simple interface to upload images, view classification output, and download CSV files of prediction. The software has interface support both in English and Hindi with basic analytics to give a snapshot of health status of samples uploaded.

# Introduction

Accurate and timely identification of plant diseases is critical for modern agriculture. This application simplifies disease detection by allowing users to upload one or more images of plant leaves, and receive predictions powered by a trained machine learning model. The interface is visually polished, multilingual, and easy to use, even for non-technical users.

# Features

- Batch prediction with upload of several images
- Image classification as healthy or diseased ones
- Each prediction's confidence level
- Downloadable CSV file of prediction results
- Summary report with healthy versus diseased image counts
- Language support: English and Hindi
- Proprietary UI with customizable styles and non-mandatory branding

# Technologies Used
Techno

-- Category--               --Technology--
- Programming :              	Python 3.x
- Web Framework	 :             Streamlit
- Machine Learning	 :         Formally trained model (via predict_image)
- Image Processing	:          Pillow (PIL)
- Data Processing	 :           Pandas, NumPy
- Styling	 :                   Integration of custom CSS

# How It Works

- The language is selected and a single or a set of leaf images is uploaded using the sidebar.
- Individual images are processed and forwarded to a model within a function predict_image.
- Predictions and confidences are shown next to the image. * A cumulative panel reveals the amount of healthy and diseased leaves.
- You can export results into a CSV file.

# Use Cases

- Farm field inspection and disease control
- Textbook material for students and researchers

- Pre-diagnostically, support was given to --- ## Future Directions * Integration of real-time dashboards with daily disease data * More advanced deep models (e.g., CNNs) Real-time camera capture and device optimization * Treatment recommendations depending on predictive disease specificity







