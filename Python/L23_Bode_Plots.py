import control as ct

# sys = ct.tf([1], [1, 4]) #Transfer function 1/(s + 4)
# response = ct.frequency_response(sys)
# ct.bode_plot(response, initial_phase = 0)

sys1 = ct.tf([1], [1, 2, 1], name='sys1')
sys2 = ct.tf([1, 0.2], [1, 1, 3, 1, 1], name='sys2')
response = ct.frequency_response([sys1, sys2], omega = [0.1, 1., 10.])

ct.bode_plot(response, initial_phase=0)