# Smooth a signal that has noise using an optimized fit that minimizes jerk

1. Install CVX (Matlab)
2. Install and activate Gurobi and Mosek

```Matlab
%% Smoothing of signal to minimize jerk
% Edgar and Mohsen - Nov. 2022
clc, clearvars, close all

time    = linspace(0, 2, 1000).'; 
sig     = sin(2*pi*time);                               %Signal
noi     = sig + (rand(1, length(sig)).'-0.5)*0.1;       %Noisy signal   

% Smooth the signal (calculate alpha (second parameter) by trial and error)
[smo, D] = smoothCVX(noi, 3e2);

% Plot and compare
figure, sgtitle('Signal smoothing'), subplot(3,1,1)
hold on, grid on, xlabel('Time'), ylabel('Position')
plot(time, sig)
plot(time, noi, '--')
plot(time, smo, '--o')
legend('Original signal', 'Noisy signal', 'Smoothed signal')
subplot(3,1,2)
hold on, grid on, xlabel('Time'), ylabel('Velocity')
plot(time, D*sig)
plot(time, D*noi, '--')
plot(time, D*smo, '--o')
subplot(3,1,3)
hold on, grid on, xlabel('Time'), ylabel('Acceleration')
plot(time, D*D*sig)
plot(time, D*D*noi, '--')
plot(time, D*D*smo, '--o')

function [fil, D] = smoothCVX(sig, alp)
% Find a set of points that are close to sig but minimize jerk

%-Create derivative operator Matrix (Center difference)
n = length(sig);
e = ones(n,1);
D = spdiags([-e 0*e e], -1:1, n, n);
D(1,:) = D(2,:);
D(end,:) = D(end-1,:);

%-Optimize
cvx_begin quiet
    variable x(n)
    
    minimize( norm(sig - x, 2) + alp*norm(D*D*D*x, 2))
cvx_end

%-Return meaningful solution
if (strcmp(cvx_status, 'Solved'))
    fil = x;
else
    warning('Solution is not accurate or defective')
end

end
```