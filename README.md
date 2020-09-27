# CellCounter
This script counts the number of cells in an image.
To do this, the script first loads the image and converts the image to grayscale. 
The grayscale image is then thresholded. Any pixel with a value less than 49 is converted to black and any pixel with a value greater than 49 is replaced with a white pixel. A watershed algorithm is applied to the thresholded image. This algorithm aids in separating out overlapping cells. A mask was applied to each resulting cell, a contour was drawn around the mask to visualize cells, and cells were counted.

The thresholded, contoured image is then saved and displayed with the number of cells in the top left corner.

This script works with JPG and TIF images.

Tif files were preprocessed in Fiji.
Raw tif was a single channel, 16 bit file.
Raw tif file was loaded into Fiji, Brightness/Contrast was Auto adjusted and applied, a Blue LUT was applied (Image>Color>Channel Tools>More>Blue), and then converted to RGB and saved.

No preprocessing was necessary on JPG files.

Improvements that need to be made:
A size filter to filter out noise. 
A better way to separate out overlapping cells
A method to process multiple images without having to manually input file path of individual images
A method to preprocess TIF files in the script without having to use Fiji

Sample images of cells are included 

## JPG Input:
![alt text](https://github.com/kathleenisrad/CellCounter/blob/master/jpginput.jpg?raw=true)

## JPG Output:
![alt text](https://github.com/kathleenisrad/CellCounter/blob/master/jpgoutput.jpg?raw=true)

## TIF Output:
![alt text](https://github.com/kathleenisrad/CellCounter/blob/master/output_tif.jpg?raw=true) 
