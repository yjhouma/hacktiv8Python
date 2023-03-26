import numpy as np
import scipy.stats
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.animation as animation

# Generate some random data
# data = np.random.normal(loc=10, scale=2, size=100)

# Set up the plot
fig, ax = plt.subplots()
sns.set_style('dark')

# Initialize the list of resampled means
resampled_means = []
sim_num = 1
# Define the function to update the plot for each frame of the animation
def update(frame):
    global sim_num
    # Resample the data
    resampled_data = scipy.stats.uniform.rvs(loc=0,scale=1, size = 100)
    # Calculate the mean of the resampled data
    resampled_mean = np.mean(resampled_data)
    # Add the resampled mean to the list
    resampled_means.append(resampled_mean)
    ax.clear()
    # Update the distribution plot with all the resampled means
    sns.histplot(resampled_means, kde=True, ax=ax, stat='density')
    m = np.mean(resampled_means)
    s = np.std(resampled_means)
    ax.set_title('Simulation Number: {} | Mean of means: {:.2f} | Std Error: {:.2f}'.format(sim_num,m,s))
    sim_num += 1
    

# Create the animation object
anim = animation.FuncAnimation(fig, update, frames=1000, repeat=False,interval=1)

# Show the animation
plt.show()
