clc, clearvars, close all
t = linspace(0, 30, 1000);
%% Load system parameters
%Motor: DCX35L  36V (Page 106) 
r = 243;        %GPX 32@4 stages @350g page 360
lcma = 0.15;    
lcmd = 0.3;
md = 5;
ma = 1;
Ja = 0.0225;
b = 0.4169;
Jm = 0;                 %Motor inertia (initial trial)
Jt = Jm*r^2 + (Ja + ma*lcma^2) + md*lcmd^2;
g = 9.81;
L = 0.26/1e3;           %H - Page 106 catalog
R = 0.716;              %Ohms - Page 106 catalog
kt = 42.9/1e3;          %Nm/A - Page 106 catalog
kb = 1/(223*2*pi/60);   %V/(rad/sec)
ia_max = 10;            %A Max current from power supply
ia_con = 3.07;          %A Max continuous current [line 6]
stallCurrent = 50.3;    %A Line 8 datasheet
V_max = 36;             %V Max. voltage from power supply
% Kinematic trajectories (at the load side)
syms ts
q = pi/2*sin(ts*pi/3)^2;    %The homework may use q = pi/2*sin(ts*pi/3);
qd = diff(q,ts);
qdd = diff(qd,ts);
qddd = diff(qdd,ts);
ts = t;
q = subs(q);
qd = subs(qd);
qdd = subs(qdd);
qddd = subs(qddd);
% Motor kinematic trajectories (at the motor shaft)
qm = q*r;
qmd = qd*r;
qmdd = qdd*r;

% Motor torque
taum = (Jt*qdd + b*qd + (ma*lcma+md*lcmd)*g*sin(q))/r;
taumd = (Jt*qddd + b*qdd + (ma*lcma+md*lcmd)*g*cos(q).*qd)/r;
% Plot 1.c - (Plot actuation requirements)
figure, plot(qmd, taum), grid on, hold on, title('Q1c - SI units')
xlabel('Motor velocity [rad/sec]'), ylabel('Motor torque [Nm]')
figure, plot(qmd/(2*pi)*60, taum*1000), grid on, hold on
title('Q1c - Maxon units (to have perspective)')
xlabel('Motor velocity [rpm]'), ylabel('Motor torque [mNm]')
% Plot 2 - (Plot feasible range of motor)
figure, hold on, grid on, xlabel('Speed [rad/s]'), ylabel('Torque [Nm]')
title('Q2 - Feasible range of the motor')
% FEASIBLE RANGE WITH A POWER SUPPLY THAT CAN PROVIDE 50.3 AMPS
line([0, V_max/kb],[kt*stallCurrent, 0]) %First quadrant
line([0, -V_max/kb],[kt*stallCurrent, 0])
line([0, V_max/kb],[-kt*stallCurrent, 0])
line([0, -V_max/kb],[-kt*stallCurrent, 0])
line([V_max/kb, -V_max/kb],[kt*ia_max, kt*ia_max], 'Color','red')
line([V_max/kb, -V_max/kb],[-kt*ia_max, -kt*ia_max], 'Color','red')
line([V_max/kb, -V_max/kb],[kt*ia_con, kt*ia_con], 'Color','green')
line([V_max/kb, -V_max/kb],[-kt*ia_con, -kt*ia_con], 'Color','green')
plot(qmd, taum, 'r--o', 'DisplayName', 'Requirement')
ylim([-kt*ia_con*1.1, kt*ia_con*1.1])
% Plot 3
figure, hold on, xlabel('Time [s]'), ylabel('Voltage [V]'), grid on
title('Q3 - Different motor voltages')
plot(t, L*taumd/kt), plot(t, kb*qmd), plot(t, taum/kt*R)
legend('Inductor', 'Back-EMF', 'Resistor')
% Question 4
fprintf("\n#####\nQuestion 2.4\n")
fprintf("Winding losses:\t\t\t\t\t\t\t\t%3.4f [J]\n", trapz(t, (taum/kt).^2*R))
fprintf("Mechanical energy delivered to the load:\t%3.4f [J]\n", trapz(t, taum.*qmd))
