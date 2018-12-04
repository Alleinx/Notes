fprintf('Plotting Data ...\n')
data = load('ex1data1.txt');
t = data(:, 1 : 11); y = data(:, 12);
m = length(y); % number of training examples

mu = mean(t);
sigma = std(t);
temp = t;
temp = temp - mu;

for i = 1:m
    for z = 1:11
        temp(i,z)=temp(i,z)/sigma(z);
    end
end

t = temp;
% Plot Data
% Note: You have to complete the code in plotData.m

fprintf('Running Gradient Descent ...\n')



X = [ones(m, 1), t]; % Add a column of ones to x
theta = zeros(12, 1); % initialize fitting parameters
for i = 1:12
    theta(i) = randn;
end
% Some gradient descent settings
iterations = 3000;
alpha = 0.01;
% ====================== YOUR CODE HERE ======================
% Instructions: 1. using gradient descent to compute the parameter
%               theta and the cost. 2. plotting the regression line.
%

[theta,J]=gradientDescent(X,y,theta,alpha,iterations);


