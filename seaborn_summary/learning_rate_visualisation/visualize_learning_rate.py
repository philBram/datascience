import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

def draw_learning_rate(weights_slope, weights_intercept, weights_cost=None, plot_type='2d', ax=None, size=30):
    
    if plot_type == '3d':

        if ax == None:
            fig = plt.figure(figsize=(10, 8), dpi=100)
            fig.suptitle('learning rate 3D', fontsize=20)

            ax = fig.add_subplot(projection='3d')

            ax.set_xlabel('slope')
            ax.set_ylabel('intercept')
            ax.set_zlabel('cost')

        for i in range(len(weights_cost) - 1):
            ax.plot([weights_slope[i], weights_slope[i + 1]], [weights_intercept[i], weights_intercept[i + 1]], zs=[weights_cost[i], weights_cost[i + 1]], c='b')
            
        ax.scatter(weights_slope, weights_intercept, weights_cost, c='r', s=size)
    
    elif plot_type == '2d':
        
        if ax == None:
            fig = plt.figure(figsize=(10, 8), dpi=100)
            fig.suptitle('learning rate 2D', fontsize=20)

            ax = fig.add_subplot()
            
            ax.set_xlabel('slope')
            ax.set_ylabel('intercept')
            
        ax.plot(weights_slope, weights_intercept, c='b', marker='o', markerfacecolor='r')
        
        
def draw_animated_learning_rate(weights_slope, weights_intercept, weights_cost=None, plot_type='2d', ax=None, fig=None):
    

    def animate_3D(i, data, line):
        line.set_data(data[0: 2, :i]) 
        line.set_3d_properties(data[2][:i]) 

        return line,
    
    def animate_2D(i, data, line):
        line.set_data(data[0: 2, :i]) 

        return line,
    
    if plot_type == '3d':

        if ax == None:
            fig = plt.figure(figsize=(10, 8), dpi=100)
            fig.suptitle('learning rate 3D animated', fontsize=20)

            ax = fig.add_subplot(projection='3d')

            ax.set_xlabel('slope')
            ax.set_ylabel('intercept')
            ax.set_zlabel('cost')
    
        line, = ax.plot(weights_slope, weights_intercept, weights_cost, c='b', lw=3)
        data = np.array([weights_slope, weights_intercept, weights_cost])
        anim_3D = FuncAnimation(fig, animate_3D, frames=len(weights_cost) * 3, fargs=(data, line), interval=50)
        
        return anim_3D
    
    elif plot_type == '2d':
        
        if ax == None:
            fig = plt.figure(figsize=(10, 8), dpi=100)
            fig.suptitle('learning rate 2D animated', fontsize=20)

            ax = fig.add_subplot()
            
            ax.set_xlabel('slope')
            ax.set_ylabel('intercept')
            
        line, = ax.plot(weights_slope, weights_intercept, c='b', lw=3)
        data = np.array([weights_slope, weights_intercept])
        anim_2D = FuncAnimation(fig, animate_2D, frames=len(weights_intercept) * 3, fargs=(data, line), interval=50)
        anim_2D.frame_seq = anim_2D.new_frame_seq() 
        anim_2D.event_source.start()
        
        return anim_2D