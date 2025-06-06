# Logistic Regression
This is a project where I implement different forms of logistic regression (LR) from scratch.

## Table of Contents
- [Plan](#plan)
- [P1](#p1)
- [P2](#p2)
- [P2](#p3)
- [Takeaways](#takeaways)
- [License](#license)

## Plan
I separated the project into three parts: Binary Logistic Regression, One versus Rest Logistic Regression and Multinomial Logistic Regression. The first part of
this project uses the Pima Indians Diabetes Database from Kaggle for classifying whether or not a patient has diabetes base on several
diagnostic measurements. The second and third part will use the MNIST dataset for digit classification to predict the value of handwritten
digits. I will supplement the first and third parts with LaTeX writeups of the necessary derivations and optimization algorithm formulations.

Here is a tabular description:

Part | Description | Status
---- | ----------- | ------
1    | Binary LR| DONE
2    | One Versus Rest LR | TODO
3    | Multinomial LR | TODO

## P1
My first model implemented Binary logistic regression. I decided to define my objective function via Log-Likelihood. Thus, the optimization step was focused on converging towards the maximum of the objective. Due to the structure of the objective function (which is explored in depth in the write up) I applied the Newton-Raphson method to converge to a zero
of the gradient of the objective function and used this for predictions. Before any hyperparameter training and model tuning the model had a 78% accuracy, which is a decent starting point.

## P2
My second model implemented One Versus Rest logistic regression. This is just repeated application of Binary logistic regression so a lot of the details from part 1 carried over. The main changes were for efficiency, as I used the MNIST digit dataset for this part which is quite large and so I had to employ stochastic methods to make the training process feasible. Despite my optimizations the model was still quite slow, but it ended up with a 85% accuracy which is a decent benchmark. I decided not to spend time optimizing the model further as it is basically a cruder version of the model employed in part 3, which I will spend more time working on.
