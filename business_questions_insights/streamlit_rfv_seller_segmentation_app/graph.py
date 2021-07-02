import matplotlib.pyplot as plt


def scatter(x, y, c, s, l, x_label, y_label, title=''):
    fig, ax = plt.subplots()
    plt.box(False)
    ax.scatter(x=x, y=y, c=c, s=s)
    ax.legend()
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.tick_params(axis='both', which='both', length=0)

    return fig