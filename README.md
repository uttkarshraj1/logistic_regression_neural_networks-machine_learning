# Logistic Regression and Neural Networks 

**Logistic Regression**

1) From the root directory of the assignment’s code, navigate to the folder “assgn_1_part_2/1_logistic_regression”.

2) With logistic regression the values we want to predict are now discrete classes, not continuous variables.
3) 
4) In other words, logistic regression is for classification tasks. In the binary classification problem we have classes 0 and 1, e.g.
classifying email as spam or not spam based on words used in the email. 

**Task 1:** Include in your report the relevant lines of code and the result of the using plot_sigmoid.py.

1) The dataset we use is an exam score dataset with a 2-dimensional input space (for easy visualization) and a binary classification of whether the student was admitted or not.

2) The data can be found in:”ex4x.dat” and “ex4y.dat”. 
3) The data has been loaded into the variables X and y. Additionally, the bias variable 1 has been added to each data point.

4) Run plot_data.py to plot the data. Note that the data have been normalized, to enable the data to be more easily
optimized.

**Task 2.** Plot the normalized data to see what it looks like. Plot also the data, without normalization.

1) Enclose the plots in your report.

**Cost function and gradient for logistic regression**

**Task 3.** Modify the calculate_hypothesis.py function so that for a given dataset, theta and training example it returns
the hypothesis.

1) For example, for the dataset X=[[1,10,20],[1,20,30]] and for Theta = [0.5,0.6,0.7], the call to the function calculate_hypothesis(X,theta,0) will return: sigmoid(1 * 0.5 + 10 * 0.6 + 20 * 0.7)

2) The function should be able to handle datasets of any size. Enclose in your report the relevant lines of code.

**Task4** To calculate a logarithm you can use np.log(x). Now run the file assgn1_ex1.py.

1) Tune the learning rate, if necessary.

2) What is the final cost found by the gradient descent algorithm? In your report include the modified code and the cost
plot.


 **Draw the decision boundary**
 
Task 5. Plot the decision boundary. This corresponds to the line where , which is the boundary line’s
equation.

1) To plot the line of the boundary, you’ll need two points of (x1,x2). 

2) Given a known value for x1, you can find the value of x2. 

3) Rearrange the equation in terms of x2 to do that.

4) Use the minimum and maximum values of x1 as the known values, so that the boundary line that you’ll plot, will span across the whole axis of x1. 

5) For these values of x1, compute the values of x2.

6) Use the relevant plot_boundary function in assgn1_ex1.py and include the graph in your report

**Neural Network**

1) We will now perform backpropagation on a feedforward network to solve the XOR problem.

2) The network will have 2 input neurons, 2 hidden neurons and one output neuron.

3) There is also a bias on the hidden and output layer, e.g. with the following architecture:

4) Your first task is to modify the function sigmoid.py to use the sigmoid function that was implemented in the previous
part, I.e. the logistic regression’s code.

=> The program works in the following way:

5) he arrays containing the input patterns (X) and the desired outputs (y) are created. 

6) These are passed to the train() function, that can be found in the file train_scripts.py. 

7) The train() function also takes as input arguments the number of hidden units desired (set to 2 for XOR), the number of iterations we should run the algorithm for, and the learning
rate.

8) In train() the neural network is created, and the main loop of the algorithm is executed. It works in the following way:

=> For each iteration:

=> For each sample:

 - forward_pass()
 
 - backward_pass()
 
9) For each input pattern, we activate the network by feeding the input signal through the neurons.

10) After this is completed, we compare the network’s output (i.e. the predictions), to the desired output (groundtruth labels), and
update the weights using gradient descent
