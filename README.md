# AutoCertify - Bulk Certificate Generator
AutoCertify is a simple certificate generator tool built using Tkinter, OpenCV, and openpyxl in Python.By letting users choose the location of an example certificate image and the Excel file with names, this program streamlines the process of creating certificates. Next, at user-specified locations, the application superimposes the names onto the certificate.</br>
## Features
* ### Excel Integration:
 * Uses Excel file to import name to be written on the Certificate.
* ### Customizable Positioning:
 * Specify the X and Y coordinates on the certificate where the names should be placed.
* ### User-Friendly Interface: 
 * Utilizes Tkinter for a simple and intuitive graphical user interface.
* ### Guide Option: 
 * Provides a guide for users on how to select the position on the certificate.

## Usage
* ### Excel File:
 * Click the "Browse" button to select the Excel file containing the list of names.
* ### Certificate Image:
 * Click the "Browse" button to select the sample certificate image.
* ### Positioning: 
 * Enter the X and Y coordinates for the name placement on the certificate.
* ### Generate Certificates: 
 * Click the "Generate" button to generate certificates with names placed at the specified positions.
* ### Guide Option: 
 * Click the "Guide" link to view instructions on selecting the position on the certificate. 

## Installation
To run the application, ensure you have the required dependencies installed:</br>
* _pip install opencv-python_</br>
* _pip install openpyxl_</br>

## ScreenShot
![ScreenShot1](https://github.com/muhammad-haziqul-khair/AutoCertify/blob/main/s1.png)

## Important Notes
* Ensure that the paths provided for the Excel file and the sample certificate image are valid.</br>
* The generated certificates will be saved in the "certificate" folder within the user's Downloads directory.</br>
