import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import nash_to_brouwer as ntb

fig, ax = plt.subplots()
plt.title(ntb.name_game)
plt.xlabel(r'$\alpha$')
plt.ylabel(r'$\beta$')

# #plot Nash equilibria
plt.scatter(ntb.Nash_equilibria[:, 0], ntb.Nash_equilibria[:, 1], s = 80, color = 'red')

plt.xlim(0, 1)
plt.ylim(0, 1)

num_lines = 20
value = np.linspace(0, 1, num_lines)
ones = np.ones(50)
running = np.linspace(0, 1, 50)

#for interactive ploting
C, D = [], []
for i in range(num_lines):
    C.append(0)
    D.append(0)
    C[i], = plt.plot([], [], color = 'orange')
    D[i], = plt.plot([], [], color = 'orange')


def update(alpha):
    for i in range(num_lines):
        # vertical lines
        X, Y = ntb.plot_line(0, value[i])
        C[i].set_data(alpha*X + (1-alpha)*ones*value[i], alpha*Y + (1-alpha)*running)

        #horizontal lines
        X, Y = ntb.plot_line(1, value[i])
        D[i].set_data(alpha*X + (1-alpha)*running, alpha*Y + (1-alpha)*ones*value[i])



total_time = 5*1000
num_frames = int(30*total_time/1000)
ani = FuncAnimation(fig, update, frames=np.linspace(0, 1, num_frames), interval = total_time/num_frames, blit=False)
ani.save('moovie_'+ntb.name_game+'.gif', writer='imagemagick', fps= 30)

