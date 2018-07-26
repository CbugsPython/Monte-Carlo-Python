import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random


def initialize():
    print('This is a visualisation of Monte Carlos method to estimate Pi!')
    num_of_p = int(input('How many points do you want to use\n'))
    refresh_interval_ms = int(input('Graph refresh rate in milliseconds (1000 ms is 1 second, default: 200)\n'))
    ps_per_refresh = int(input('How many points should be added on each refresh?\n'))

    plot(num_of_p, refresh_interval_ms, ps_per_refresh)


def plot(number_of_points, refresh_interval_milliseconds, points_per_refresh):
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
    pi_estimate_steps = []
    monte_carlo_method(number_of_points,
                       outside_x,
                       outside_y,
                       inside_x,
                       inside_y,
                       cur_pi_estimate,
                       pi_estimate_steps)

    ani1 = animation.FuncAnimation(fig1, animate_sim, fargs=(inside_x, inside_y, outside_x, outside_y, ax1),
                                   interval=refresh_interval_milliseconds,
                                   blit=True, frames=points_per_refresh)

    ani2 = animation.FuncAnimation(fig1,
                                   animate_estimate, fargs=(cur_pi_estimate, pi_estimate_steps, ax2),
                                   interval=refresh_interval_milliseconds, blit=True,
                                   frames=points_per_refresh)

    plt.show()


def monte_carlo_method(number_of_points, outside_x, outside_y, inside_x, inside_y, cur_pi_estimate, pi_estimate_steps):
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
    pi_estimate_steps.append(list(range(0, len(cur_pi_estimate))))


def animate_sim(frame, inside_x, inside_y, outside_x, outside_y, ax1):
    if frame+1 < len(inside_y):
        in_x_part = inside_x[0:frame+1]
        in_y_part = inside_y[0:frame+1]
        out_x_part = outside_x[0:frame+1]
        out_y_part = outside_y[0:frame+1]

        ax1.scatter(in_x_part, in_y_part, label='Inside', color='r', marker='.')
        ax1.scatter(out_x_part, out_y_part, label='Outside', color='k', marker='.')
        return ax1


def animate_estimate(frame, cur_pi_estimate, pi_estimate_steps, ax2):
    if frame < len(cur_pi_estimate):
        pi_estimate_part = cur_pi_estimate[0:frame+1]
        pi_step_part = pi_estimate_steps[0:frame+1]

        plt.title("Pi ≈" + str(cur_pi_estimate[frame+1]))
        ax2.plot(pi_step_part, pi_estimate_part, c='k')
        return ax2


if __name__ == '__main__':
    initialize()
