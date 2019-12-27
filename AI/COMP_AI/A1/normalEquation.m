
fprintf('Normal Equation-based linear regression\n')
data = csvread('ex1data1.txt');
X = data(:, 1); y = data(:, 2);
m = length(y); % number of training examples

plotData(X, y);

% ====================== YOUR CODE HERE ======================
% Instructions: 1. Update the matrix X
%               2. Use the normal equation
%
X = [ones(m, 1), data(:,1)];
theta = pinv(X'*X)*X'*y;

fprintf('theta 0 is %.3f theta 1 is%.3f',theta(1),theta(2));
hold on
plot(X(:,2), X*theta);
legend("Training data", "Regression line")	
% ============================================================


hold off % don't overlay any more plots on this figure

