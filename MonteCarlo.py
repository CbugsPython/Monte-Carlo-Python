import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random


def initialize():
    print('This is a visualisation of Monte Carlos method to estimate Pi!')
    num_of_p = int(input('How many points do you want to use\n'))
    refresh_interval_ms = int(input('Graph refresh rate in milliseconds (1000 ms is 1 second, default: 200)\n'))

    plot(num_of_p, refresh_interval_ms)


def plot(number_of_points, refresh_interval_milliseconds):
    fig1, (ax1, ax2) = plt.subplots(2, 1, figsize=(7, 8))
    plt.subplots_adjust(top=0.96, bottom=0.06, hspace=0.23)
    circle = plt.Circle((0, 0), radius=1, edgecolor='b', facecolor='None')
    ax1.set_title('Monte Carlo Pi simulation')
    ax1.set_xlabel('x')
    ax1.set_ylabel('y')
    ax1.add_artist(circle)
    ax1.plot()

    ax2.set_title('Pi estimate')
    ax2.set_xlabel('Iterations')
    ax2.set_ylabel('Pi')
    ax2.plot()

    outside_x = []
    outside_y = []
    inside_x = []
    inside_y = []
    cur_pi_estimate = []

    monte_carlo_method(number_of_points,
                       outside_x,
                       outside_y,
                       inside_x,
                       inside_y,
                       cur_pi_estimate)
    pi_estimate_steps = range(0, len(cur_pi_estimate))

    ani1 = animation.FuncAnimation(fig1, animate_sim_inside, fargs=(inside_x, inside_y, ax1),
                                   interval=refresh_interval_milliseconds, frames=number_of_points)

    ani2 = animation.FuncAnimation(fig1,
                                   animate_pi_estimate, fargs=(cur_pi_estimate, pi_estimate_steps, ax2),
                                   interval=refresh_interval_milliseconds,
                                   frames=number_of_points, blit=True)

    ani3 = animation.FuncAnimation(fig1, animate_sim_outside, fargs=(outside_x, outside_y, ax1),
                                   interval=refresh_interval_milliseconds, frames=number_of_points)

    plt.show()


def monte_carlo_method(number_of_points, outside_x, outside_y, inside_x, inside_y, cur_pi_estimate):
    for i in range(0, number_of_points):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        if (x ** 2 + y ** 2) <= 1.0:
            inside_x.append(x)
            inside_y.append(y)
        else:
            outside_x.append(x)
            outside_y.append(y)
        cur_pi_estimate.append((len(inside_y)/(len(inside_y)+len(outside_y)))*4)


def animate_sim_inside(frame, inside_x, inside_y, ax1):
    if frame < len(inside_y):
        scatter = ax1.scatter(inside_x[frame], inside_y[frame], color='r', marker='.')
    else:
        scatter = ax1.scatter(inside_x[len(inside_x)-1], inside_y[len(inside_y)-1], color='r', marker='.')
    return scatter


def animate_sim_outside(frame, outside_x, outside_y, ax1):
    if frame < len(outside_y):
        scatter = ax1.scatter(outside_x[frame], outside_y[frame], color='k', marker='.')
    else:
        scatter = ax1.scatter(outside_x[len(outside_x)-1], outside_y[len(outside_y)-1], color='k', marker='.')
    return scatter


def animate_pi_estimate(frame, cur_pi_estimate, pi_estimate_steps, ax2):
    #plt.title("Pi ≈" + str(cur_pi_estimate[frame]))
    graph = ax2.plot(pi_estimate_steps[0:frame], cur_pi_estimate[0:frame], c='k')
    return graph


if __name__ == '__main__':
    initialize()
