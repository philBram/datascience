##################################################################################################################
# 
#   learning rate visualization
#
#   Author: Philip Bramwell
#   Date: 26 December
# 
#   goal: 
#         * Visualize the learning rate
#   
#   Documentation: 
#         https://matplotlib.org/stable/tutorials/toolkits/mplot3d.html
#         https://matplotlib.org/stable/api/animation_api.html
#
##################################################################################################################

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

def draw_learning_rate(weights_slope, weights_intercept, weights_cost=None, plot_type='2d', ax=None):
    
    '''
    Draws the learning rate onto a 2d or 3d matplotlib axes by passing the x-, y-, and if the animation should 
    be in 3d, z-values

    Parameters
    ----------
    weights_slope : list of float or int
        will be plotted on the x-axes of the matplotlib axes
    weights_intercept : list of float or int
        will be plotted on the y-axes of the matplotlib axes
    weights_cost : list, default None
        will be plotted on the z-axes of the matplotlib axes, if plot_type='2d' this parameter should be None
    plot_type : str, default '2d'
        determines the matplotlib axes projection, acceptable values '2d', '3d'
    ax : matplotlib axes, default None
        matplotlib axes on whitch the learning rate visualisation should be plotted,
        if None creates a new matplotlib axes and plots the learning rate visualisation onto the created axes
        
    Returns
    -------
    None
    '''
    
    # plots onto a 3d matplotlib axes    
    if plot_type == '3d':

        # creates new matplotlib axes with 3d projection if ax=None        
        if ax == None:
            fig = plt.figure(figsize=(10, 8), dpi=100)
            fig.suptitle('learning rate 3D', fontsize=20)

            ax = fig.add_subplot(projection='3d')

            ax.set_xlabel('slope')
            ax.set_ylabel('intercept')
            ax.set_zlabel('cost')

        # draws a line between x-, y- z-coordinate point so that they are connected 
        for i in range(len(weights_cost) - 1):
            ax.plot([weights_slope[i], weights_slope[i + 1]], [weights_intercept[i], weights_intercept[i + 1]], zs=[weights_cost[i], weights_cost[i + 1]], c='b')
            
        # draw a point for each x-, y- z-coordinate point
        ax.scatter(weights_slope, weights_intercept, weights_cost, c='r', s=30)
    
    # plots onto a 3d matplotlib axes    
    elif plot_type == '2d':
        
        # creates new matplotlib axes with 2d projection if ax=None
        if ax == None:
            fig = plt.figure(figsize=(10, 8), dpi=100)
            fig.suptitle('learning rate 2D', fontsize=20)

            ax = fig.add_subplot()
            
            ax.set_xlabel('slope')
            ax.set_ylabel('intercept')
            
        # draw a point for each x-, y-coordinate point
        ax.plot(weights_slope, weights_intercept, c='b', marker='o', markerfacecolor='r')
        
        
def draw_animated_learning_rate(weights_slope, weights_intercept, weights_cost=None, plot_type='2d', ax=None, fig=None):
    
    '''
    Draws the learning rate as an matplotlib animation onto a 2d or 3d matplotlib axes by passing the x-, y-, and if the 
    animation should be in 3d, z-values

    Parameters
    ----------
    weights_slope : list of float or int
        will be plotted on the x-axes of the matplotlib axes
    weights_intercept : list of float or int
        will be plotted on the y-axes of the matplotlib axes
    weights_cost : list, default None
        will be plotted on the z-axes of the matplotlib axes, if plot_type='2d' this parameter should be None
    plot_type : str, default '2d'
        determines the matplotlib axes projection, acceptable values '2d', '3d'
    ax : matplotlib axes, default None
        matplotlib axes on whitch the learning rate visualisation should be plotted,
        if ax=None creates a new matplotlib axes and plots the learning rate visualisation onto the created axes
    fig : matplotlib figure, default None
        matplotlib figure needed for the animation if the learning rate visualisation should be plotted on a already
        existing matplotlib axes
        if fig:None creates a new matplotlib figure needed for the animation
        
    Returns
    -------
    matplotlib animation
        returns a matplotlib animation object which can further be used to save the animation.
    '''

    def animate_3D(i, data, line):
        line.set_data(data[0: 2, :i]) 
        line.set_3d_properties(data[2][:i]) 

        return line,
    
    def animate_2D(i, data, line):
        line.set_data(data[0: 2, :i]) 

        return line,
    
    # plots onto a 3d matplotlib axes   
    if plot_type == '3d':

        # creates new matplotlib axes with 3d projection if ax=None 
        if ax == None:
            fig = plt.figure(figsize=(10, 8), dpi=100)
            fig.suptitle('learning rate 3D animated', fontsize=20)

            ax = fig.add_subplot(projection='3d')

            ax.set_xlabel('slope')
            ax.set_ylabel('intercept')
            ax.set_zlabel('cost')
    
        # animates 3d learning rate course 
        line, = ax.plot(weights_slope, weights_intercept, weights_cost, c='b', lw=3)
        data = np.array([weights_slope, weights_intercept, weights_cost])
        anim_3D = FuncAnimation(fig, animate_3D, frames=len(weights_cost) * 3, fargs=(data, line), interval=50)
                
        # draw a point for each x-, y- z-coordinate point
        ax.scatter(weights_slope, weights_intercept, weights_cost, alpha=0.05, c='r', s=30)
        
        return anim_3D
    
    # plots onto a 3d matplotlib axes 
    elif plot_type == '2d':
        
        # creates new matplotlib axes with 2d projection if ax=None
        if ax == None:
            fig = plt.figure(figsize=(10, 8), dpi=100)
            fig.suptitle('learning rate 2D animated', fontsize=20)

            ax = fig.add_subplot()
            
            ax.set_xlabel('slope')
            ax.set_ylabel('intercept')
            
        # animates 2d learning rate course 
        line, = ax.plot(weights_slope, weights_intercept, c='b', lw=3)
        data = np.array([weights_slope, weights_intercept])
        anim_2D = FuncAnimation(fig, animate_2D, frames=len(weights_intercept) * 3, fargs=(data, line), interval=50)
        
        # draw a point for each x-, y-coordinate point
        ax.scatter(weights_slope, weights_intercept, alpha=0.05, c='r', s=30)
        
        return anim_2D