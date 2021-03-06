<!-- This is the markdown template for the final project of the Building AI course, 
created by Reaktor Innovations and University of Helsinki. 
Copy the template, paste it to your GitHub README and edit! -->

# iris_NN

Final project for the Building AI course

## Summary

Recognising irises by their features using nerual networks. 
Implementation of a classic AI exercise developed in python.


## Background

With this application it is possible to distinguish between the three types of iris Setosa, Versicolour, and Virginica by the features of the flower: sepal length, sepal width, petal length and petal width.

The purpose is purely educational as it is a classic AI exercise but implemented with a neural network.


## How is it used?

Test the capacity of the neural network and put into practice what was learned in the course

<img src="https://upload.wikimedia.org/wikipedia/commons/f/f8/Siberian_Iris_Iris_sibirica_Top_Side_View_Green_2000px.jpg" width="300">

This is how you create code examples:
```
model.add(kr.layers.Dense(16, input_shape=(4,)))
model.add(kr.layers.Activation("sigmoid"))
model.add(kr.layers.Dense(3))
model.add(kr.layers.Activation("softmax"))
```


## Data sources and AI methods

[UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Iris)

* Number of Instances: 150 (50 in each of three classes)

* Number of Attributes: 4 numeric, predictive attributes and the class

* Attribute Information:
   * sepal length in cm
   * sepal width in cm
   * petal length in cm
   * petal width in cm
   * class: 
      * Iris Setosa
      * Iris Versicolour
      * Iris Virginica

* Missing Attribute Values: None

* Summary Statistics:

 Features | Min | Max | Mean | SD | Class Correlation
 --- | --- | --- | --- | --- | ---
 sepal length | 4.3 | 7.9 | 5.84 | 0.83 | 0.7826   
 sepal width | 2.0 | 4.4 | 3.05 | 0.43 | -0.4194
 petal length | 1.0 | 6.9 | 3.76 | 1.76 | 0.9490  (high!)
 petal width | 0.1 | 2.5 | 1.20 | 0.76 | 0.9565  (high!)

* Class Distribution: 33.3% for each of 3 classes.

## Challenges

Is not able to discriminate all varieties of iris.

## What next?

Improve the accuracy of predictions by trying out various hidden level activation functions.
Increasing the number of iris varieties to be discriminated against


## Acknowledgments

* <a href="https://commons.wikimedia.org/wiki/File:Siberian_Iris_Iris_sibirica_Top_Side_View_Green_2000px.jpg">Photo by and (c)2007 Derek Ramsey (Ram-Man)</a>, <a href="http://www.gnu.org/licenses/old-licenses/fdl-1.2.html">GFDL 1.2</a>, via Wikimedia Commons

* dataset https://archive.ics.uci.edu/ml/datasets/Iris
    * Title: Iris Plants Database
    * Updated Sept 21 by C.Blake - Added discrepency information
    
    Sources:
     * Creator: R.A. Fisher
     * Donor: Michael Marshall (MARSHALL%PLU@io.arc.nasa.gov)
     * Date: July, 1988