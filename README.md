# Depth-estimation-model
First run callibration.ipynb file to get the focal lenght and other camera parameters of your device.

Then take 2 stereo images such that you know the distance d between the stereo cameras.

Run Image_Registration.ipynb to combine the left and right stereo images.

At last run the Applying_Stereo_Depth_to_a_Driving_Scenario.ipynb to get the find the depth of objects in the image using depth-disparity concept with combined image.
