import tatapov

def test_basics():
    data = tatapov.annealing_data["25C"]["01h"]
    subset = tatapov.data_subset(data, ["ACGA", "AAAT", "AGAG"],
                                 add_reverse=True)
    ax, _ = tatapov.plot_data(subset, figwidth=5)