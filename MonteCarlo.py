import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

number_of_points = 1000
refresh_interval_milliseconds = 10
points_per_refresh = 10


outside_x = []
outside_y = []
inside_x = []
inside_y = []
cur_pi_estimate = []
pi_estimate_steps = []


fig1, (ax1, ax2) = plt.subplots(2, 1, figsize=(7, 8))

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


pi_estimate_steps = range(0, len(cur_pi_estimate))


iteration_step = points_per_refresh
cur_iteration = 0


def animate_sim(interval):
    global cur_iteration
    global iteration_step

    render_from = cur_iteration-iteration_step
    cur_iteration += iteration_step
    if cur_iteration < len(inside_y):
        in_x_part = inside_x[render_from:cur_iteration]
        in_y_part = inside_y[render_from:cur_iteration]
        out_x_part = outside_x[render_from:cur_iteration]
        out_y_part = outside_y[render_from:cur_iteration]

        ax1.scatter(in_x_part, in_y_part, label='Inside', color='r', marker='.')
        ax1.scatter(out_x_part, out_y_part, label='Outside', color='k', marker='.')


pi_cur_iteration = 0


def animate_estimate(interval):
    global pi_cur_iteration
    global iteration_step

    render_from = pi_cur_iteration-iteration_step
    pi_cur_iteration += iteration_step
    if pi_cur_iteration < len(cur_pi_estimate):
        pi_estimate_part = cur_pi_estimate[render_from:cur_iteration]
        pi_step_part = pi_estimate_steps[render_from:cur_iteration]

        plt.title("Pi ≈" + str(cur_pi_estimate[render_from]))
        ax2.plot(pi_step_part, pi_estimate_part, c='k')


plt.subplots_adjust(top=0.96, bottom=0.06, hspace=0.23)
ani1 = animation.FuncAnimation(fig1, animate_sim, interval=refresh_interval_milliseconds)
ani2 = animation.FuncAnimation(fig1, animate_estimate, interval=refresh_interval_milliseconds)
plt.show()
