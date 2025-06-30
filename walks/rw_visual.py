import matplotlib.pyplot as plt
from walks.random_walks import RandomWalks



def run():
    plt.style.use('classic')
    rw = RandomWalks(50_000)
    rw.fill_walk()
    fig, ax = plt.subplots(figsize = (10,6), dpi=128)#figsize = (15,9) fi
    point_numbers = range(len(rw.y_values))
    # ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=1)
    ax.plot(rw.x_values, rw.y_values, c='green', linewidth=3)
    ax.set_aspect('equal')
    
    #star and end
    ax.scatter(rw.x_values[0], rw.y_values[0], c='green', s=20)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', s=20)

    #remove axis
    ax.get_yaxis().set_visible(False)
    ax.get_xaxis().set_visible(False)
    
    plt.show()
    

while True:
    
    string = input('type no to stop: ')
    if string == 'no':
        break
    run()
    