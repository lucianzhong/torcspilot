import matplotlib.pyplot as plt
import numpy as np

testData = np.genfromtxt('aalborg_trial1.csv', delimiter=',', skip_header=1,
                     skip_footer=0, names=["time","speedX","speedY","speedZ","angle","damage","rpm","trackPos","steering","accel","brake","reward","loss"])

fig, ax1 = plt.subplots()
iterations = np.arange(0, testData.shape[0], 1) 
speedXsin = -abs(np.multiply(testData["speedX"], np.sin(testData["angle"])))
speedXcos = abs(np.multiply(testData["speedX"], np.cos(testData["angle"])))
speedXtrackPos = abs(np.multiply(testData["speedX"], testData["trackPos"]))

# Label graph axes 
ax1.set_xlabel('iteration #')
ax1.set_ylabel('reward value')

# Plot multiple curves (one per training model) 
ax1.plot(iterations, speedXsin, 'b-', label = 'Transversal Velocity')
ax1.plot(iterations, speedXcos, 'r-', label = 'Parallel Velocity')
ax1.plot(iterations, speedXtrackPos, 'g-', label = 'Track Position Velocity')
ax1.plot(iterations, testData['reward'], 'b-', label = "Total Reward")

plt.show() 
