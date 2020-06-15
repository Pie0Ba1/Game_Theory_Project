import numpy as np
import matplotlib.pyplot as plt
import nash_to_brouwer as ntb

def plot_vector_filed(func):
    N, delta = 30, 0.01
    plt.figure(figsize = (10, 10))
    plt.title(ntb.name_game)

    #prepare grid
    xarr = np.linspace(delta, 1-delta, N)
    yarr = np.linspace(delta, 1-delta, N)
    X, Y = np.meshgrid(xarr, yarr)
    Xflat, Yflat = np.concatenate(X), np.concatenate(Y)
    D = np.empty((len(Xflat), 2))
    r = np.empty(2)
    colorarr = []#np.empty(len(Xflat), dtype = str)

    #calculate displacements and convert to colors
    for i in range(len(Xflat)):
        r[0], r[1] = Xflat[i], Yflat[i]
        D[i] = func(r) - r  #displacement of R after the mapping
        D[i] /= np.sqrt(np.sum(np.square(D[i])))
        angle = np.arctan2(D[i, 1], D[i, 0])*2/np.pi
        if angle >= 0 and angle< 1:
            colorarr.append('gold')
        elif angle < 0 and angle > - 1.5:
            colorarr.append('red')
        else:
            colorarr.append('blue')

    plt.quiver(Xflat, Yflat, D[:, 0], D[:, 1], color = colorarr)

    #plot triangles
    lwmy = 0.5 #width of grid lines
    for i in range(N):
        plt.plot([xarr[i], xarr[i]], [yarr[0], yarr[-1]], lw = lwmy, color = 'grey') #vertical lines
        plt.plot([xarr[0], xarr[-1]], [yarr[i], yarr[i]], lw = lwmy, color = 'grey') #horizontal lines
        plt.plot([xarr[0], xarr[i]], [yarr[i], yarr[0]], lw = lwmy, color = 'grey') #diagonal down lines
        plt.plot([xarr[i], xarr[-1]], [yarr[-1], yarr[i]], lw = lwmy, color = 'grey') #diagonal down lines

    plt.scatter(ntb.Nash_equilibria[:, 0], ntb.Nash_equilibria[:, 1], s = 80, color = 'black')

    plt.savefig('brouwer_to_end_of_the_line' + ntb.name_game)
    plt.show()


plot_vector_filed(ntb.f)



