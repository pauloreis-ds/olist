import matplotlib.pyplot as plt
import seaborn as sns


def scatterplot(data, x, y, hue, hue_order, x_label, y_label, title='', palette="tab10", x_lim=None, y_lim=None):
    fig = plt.figure()
    plt.box(False)
    sns.scatterplot(data=data, x=x, y=y, hue=hue, hue_order=hue_order, palette=palette)
    plt.legend()
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.xlim(x_lim)
    plt.ylim(y_lim)
    plt.legend(loc='lower center', bbox_to_anchor=(0.5, -.27),
               ncol=3, fancybox=True, shadow=True)
    plt.tick_params(axis='both', which='both', length=0)

    return fig
