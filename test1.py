
def add_vectors(A, B):
    return [A[0]+B[0], A[1]+B[1], A[2]+B[2]]


def plot1():
    import numpy as np
    import matplotlib
    import matplotlib.pyplot as plt

    # Data to be represented
    Y = np.linspace(0,1,12)
    X = np.ones(Y.size)
    W = [0.25,0.50,0.75,1,2,3,4,5,6,7,8]
    
    # Actual plotting
    fig = plt.figure(figsize=(8,6), dpi=72, facecolor='white')
    axes = plt.subplot(111)
    for i,w in enumerate(W):
        axes.plot( (1+i)*X, Y, linewidth=w, color='blue')
    
    axes.set_xlim(0,len(W)+1)
    axes.set_yticks([])
    axes.set_xticks(np.arange(1,len(W)+1))
    axes.set_xticklabels(['%.2f' % w for w in W])
    
    plt.show()



def plot2():
    import numpy as np
    import matplotlib
    import matplotlib.pyplot as plt
    # Data to be represented
    X = np.linspace(-np.pi,+np.pi,256)
    Y = np.sin(X)
    
    # Actual plotting
    fig = plt.figure(figsize=(8,6), dpi=72,facecolor="white")
    axes = plt.subplot(111)
    axes.plot(X,Y, color = 'blue', linewidth=2, linestyle="-")
    axes.set_xlim(X.min(),X.max())
    axes.set_ylim(1.01*Y.min(),1.01*Y.max())
    
    axes.spines['right'].set_color('none')
    axes.spines['top'].set_color('none')
    axes.xaxis.set_ticks_position('bottom')
    axes.spines['bottom'].set_position(('data',0))
    axes.yaxis.set_ticks_position('left')
    axes.spines['left'].set_position(('data',0))
    
    plt.show()
