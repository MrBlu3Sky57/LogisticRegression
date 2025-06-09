# Logistic Regression
This is a project where I implement different forms of logistic regression (LR) from scratch.

## Table of Contents
- [Plan](#plan)
- [P1](#p1)
- [P2](#p2)
- [P2](#p3)
- [Takeaways](#takeaways)
- [Acknowledgements](#acknowledgements)
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
2    | One Versus Rest LR | DONE
3    | Multinomial LR | DONE

## P1
My first model implemented Binary logistic regression. I decided to define my objective function via Log-Likelihood. Thus, the optimization step was focused on converging towards the maximum of the objective. Due to the structure of the objective function (which is explored in depth in the write up) I applied the Newton-Raphson method to converge to a zero
of the gradient of the objective function and used this for predictions. Before any hyperparameter training and model tuning the model had a 78% accuracy, which is a decent starting point.

## P2
My second model implemented One Versus Rest logistic regression. This is just repeated application of Binary logistic regression so a lot of the details from part 1 carried over. The main changes were for efficiency, as I used the MNIST digit dataset for this part which is quite large and so I had to employ stochastic methods to make the training process feasible. Despite my optimizations the model was still quite slow, but it ended up with a 85% accuracy which is a decent benchmark. I decided not to spend time optimizing the model further as it is basically a cruder version of the model employed in part 3, which I will spend more time working on.

## P3
My third model implemented multinomial logistic regression, and was meant as an extension of part 2. I made changes to how I approached the optimization process for efficiency reasons, however the sheer size of
the MNIST dataset combined with the fact that I was only using Numpy for
my implementation made me run into a wall. My training loop would take an
unreasonable amount of time, so I decided to use two smaller datasets instead. First I used the Iris dataset as a toy dataset to make sure
my model worked correctly then used the pen digits dataset for actual model building. This dataset was still reasonably large but tractable
for my model. I ended up with a 92% accuracy on my model which I was quite
happy with, as sci-kit learn logistic regression performs worse on the same dataset.

## Takeaways
I learned a lot from this project. I did not have too much difficulty with the actual model building process, but I learned a lot of lessons
about optimizing Numpy BLAS calls and reducing the computational cost
of matrix based operations. For this project I was able to manage and build models with a solid performance but I think that I also realized why
most people use PyTorch or TensorFlow instead of pure Numpy. When I begin
to implement more complicated models I think I will make the switch
as the tradeoff between lower level understanding and performance is no
longer worthwhile.

## Acknowledgments

This project was developed independently, but the following resource was extremely helpful for understanding the concepts:
- ESL by Hastie, Tibshirani, Friedman (for SVM background)

All code and math were implemented from scratch using NumPy.

## License
This project is licensed under the [MIT License](LICENSE).
