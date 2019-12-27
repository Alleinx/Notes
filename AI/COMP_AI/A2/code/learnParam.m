function [theta,cost]=learnParam(filename)
%learnParam compute the theta values from the training file, filename, with 
%each data points having two features. You will implementing gradient descent using function fminunc. 

data = load(filename);
X = data(:, [1, 2]); y = data(:, 3);
[m, n] = size(X);
X = [ones(m, 1) X];
initial_theta = zeros(n + 1, 1);


% ====================== YOUR CODE HERE ======================
% Instructions: You may have to define the cost function and gradient first.
%

options = optimset('GradObj', 'on', 'MaxIter', 400); 
[theta, cost] = fminunc(@(t)(costFunction(t, X, y)), initial_theta, options); 


plotDecisionBoundary(theta, X, y);

p = predict(theta,X);

fprintf('Train Accuracy: %f\n', mean(double(p == y)) * 100);


% =========================================================================




end
