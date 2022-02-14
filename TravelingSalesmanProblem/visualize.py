import matplotlib.pyplot as plt


def visualize_segment(segment, style="bo-"):
    plt.plot([c.real for c in segment], [c.imag for c in segment],
             style,
             clip_on=False)
    plt.axis('off')


def visualize_tour(tour, style="bo-"):
    if len(tour) > 1000: plt.figure(figsize=(15, 10))

    start = tour[0:1]
    visualize_segment(tour + start)
    visualize_segment(start, "rD")
    plt.show()