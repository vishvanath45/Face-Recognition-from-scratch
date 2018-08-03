
Problem Statement - Task entails you to develop a simple Web Application, which when given an image, is able to detect a face (show with a boundary box) and give a result saying whether Narendra Modi and/or Arvind Kejriwal are present in the image or not.

TL;Dr- The Web Application is up at http://image-recog.eigencoders.com / http://104.196.154.231 (Accuracy 94.7%):smiley::smiley:

First thought, this looks like a Image Classification Task, Machine Learning approach would do.

So, I broke down the problem into parts -

- Collect Images of classes namely Narendra_modi, Arvind_kejriwal, peoples
- Extract Face from Images of different classes
- Divide Data into three categories Training, Test, Cross validation
- Train the Classifier on Images from each Class on their Training set.
- Test it on Test_Set



The files are accordingly as -
- [Mass_Image_Downloader.ipynb](https://github.com/vishvanath45/Precog_Project/blob/master/face_detection/Mass_Image_Downloader.ipynb) (For Downloading images of given class)
- [Face_detection.ipynd](https://github.com/vishvanath45/Precog_Project/blob/master/face_detection/Face_detection.ipynb) (for recognising faces from downloaded images, cropping, resizing(200x200) pixels, and aligning them)
- [Image_Classification.ipynb](https://github.com/vishvanath45/Precog_Project/blob/master/face_detection/Image_Classification.ipynb) (Training the classifer)


The best output was given by Logistic_Regression_Classifier, Accuracy (94.7%)


I saved the Classifier as .pickle object named [Logistic_regression_fit.pickle](https://github.com/vishvanath45/Precog_Project/blob/master/face_detection/Logistic_regression_fit.pickle)


So now, whenever a new image comes to me, I have to do following processes on it 
- Extract faces, crop, align and create feature numpy array
- load my Object for Logistic regression 
- Run the feature array on classifier, get label and accordingly show output.


Test it now, :100: http://image-recog.eigencoders.com / http://104.196.154.231 :sunglasses:


### _Things which were planned but could not be done :disappointed:._
- Wanted to save the datset of Train, Test and Cross Validation data in MongoDB, but it turns out that maximum size of BSON document size is 16 MB which can be stored in  mongo document. It is visible in in Block [71] of `Image_Classification.ipynb` where it throws an error `DocumentTooLarge: BSON document too large (1484657743 bytes) - the connected server supports BSON document sizes up to 16793598 bytes(16 MB)`:confused:. So I worked around it by saving the datset in .pickle format, which allows me use dataset directly without computating again and again.
- Wanted to upload `dataset_train_final.pickle` on this git repo, but can't due to size restriction on github. I plan to host all `dataset_train_final.pickle`, `dataset_test_final.pickle` and `dataset_cv_final.pickle` on google drive and provide link.


### _Web Deployment Part_
I deployed the app using Flask Library of python on my Google Cloud account.
Link to [Github Repo](https://github.com/vishvanath45/WebApps)


#### _Reference_
I would like to thank several tutorials on machine learning, [Reddit.com/r/MachineLearning](https://reddit.com/r/machinelearning) has awesome learning resources :bow:, also OpenFace for making Face detection Library and developers of Flask for making deployment very easy.


#### _Sample of Face Recogniser_
Link - https://imgur.com/a/u4bgX
![Sample](https://i.imgur.com/NNU8kttr.png) 

For further developement/queries of this work, you can write me to : vnds.20150389[@]btech[.]nitdgp[.]ac[.]in :bowtie:

If you are impressed by this, then you should check out my other works on my personal page [here](https://vishvanath45.github.io)

---
