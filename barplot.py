def barplot(name,value):
    import numpy as np

    import matplotlib.pyplot as plt
    from matplotlib.path import Path
    from matplotlib.spines import Spine
    from matplotlib.projections.polar import PolarAxes
    from matplotlib.projections import register_projection

    x_pos = np.array(list(value))
    y_pos = np.arange(len(name))
    performance = 100 + np.zeros((len(value),),dtype = np.int)
    p1 = plt.barh(y_pos, performance, align='center', alpha=0.4)
    p2 = plt.barh(y_pos, value)
    plt.yticks(y_pos,name)
    plt.xlabel('Percentage')
    plt.title('barchart')
    for a,b in zip(x_pos,y_pos):
        plt.text(a+2, b, '%.0f' % a, ha='center', va= 'center')

    plt.show()


barplot(['aaron','bob'],[24,50])
