function [J, grad] = costFunction(theta, X, y) 

m = length(y);

h = sigmoid(X*theta);

J = -( y'*log(h)+(1-y)'*log(1-h) ) / m; %cost function.

grad =X'*(h-y)/m; 
