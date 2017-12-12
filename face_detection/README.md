### Precog Task for Summer Internship Application at Precog, IIITD

Problem Statement - Task B entails you to develop a simple Web Application, which when given an image, is able to detect a face (show with a boundary box) and give a result saying whether Narendra Modi and/or Arvind Kejriwal are present in the image or not.

TL;Dr- The Web Application is up at https://image-recog.eigencoders.com (Accuracy 94.7%):smiley::smiley:

First thought, this looks like a Image Classification Task, Machine Learning approach would do.
So, I broke down the problem into parts -

- Collect Images of classes namely Narendra_modi, Arvind_kejeriwal, peoples
- Extract Face from Images of different classes
- Divide Data into three categories Training, Test, Cross validation
- Train the Classifier on Images from each Class on there Training set.
- Test it on Test Set

The files are accordingly as -
- [Mass_Image_Downloader.ipynb](https://github.com/vishvanath45/Precog_Project/blob/master/face_detection/Mass_Image_Downloader.ipynb) (For Downloading images of given class)
- [Face_detection.ipynd](https://github.com/vishvanath45/Precog_Project/blob/master/face_detection/Face_detection.ipynb) (for recognising from dataset, cropping, resizing(200x200) pixels, and aligning them)
- [Image_Classification.ipynb](https://github.com/vishvanath45/Precog_Project/blob/master/face_detection/Image_Classification.ipynb) (Training the classifer)

The best output was given by Logistic_Regression_Classifier, Accuracy (94.7%)

I saved the Classifier as .pickle object named [Logistic_regression_fit.pickle](https://github.com/vishvanath45/Precog_Project/blob/master/face_detection/Logistic_regression_fit.pickle)

So now, whenever a new image comes to me, I have to do following processes on it 
- Extract faces, crop, align and create feature numpy array
- load my Object for Logistic regression 
- Run the feature array on classifier, get label and accordingly show output.

Test it now, :100: https://image-recog.eigencoders.com

### Web Deployment Part

I deployed the app using Flask Library of python on my Google Cloud account.

#### Reference
I would like to thank several tutorials on machine learning application, [r/MachineLearning](https://reddit.com/r/machinelearning) has awesome resources, also OpenFace for making Face detection Library and Several tutorial on deploying web app.
