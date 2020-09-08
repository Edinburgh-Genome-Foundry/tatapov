import itertools
import tatapov
import tatapov.utils


def test_basics():
    data = tatapov.annealing_data["25C"]["01h"]
    subset = tatapov.data_subset(data, ["ACGA", "AAAT", "AGAG"], add_reverse=True)
    ax, _ = tatapov.plot_data(subset, figwidth=5)


def test_is_palyndromic():
    assert tatapov.utils.is_palyndromic("AAAA") is False
    assert tatapov.utils.is_palyndromic("AATT") is True


def test_list_overhangs():
    all_overhangs = ["".join(o) for o in itertools.product(*(4 * ["ACGT"]))]
    assert tatapov.utils.list_overhangs(
        standard_overhangs_only=True, non_palyndromic=True
    ) == [
        "AAAA",
        "AAAC",
        "AAAG",
        "AAAT",
        "AACA",
        "AACC",
        "AACG",
        "AACT",
        "AAGA",
        "AAGC",
        "AAGG",
        "AAGT",
        "AATA",
        "AATC",
        "AATG",
        "ACAA",
        "ACAC",
        "ACAG",
        "ACAT",
        "ACCA",
        "ACCC",
        "ACCG",
        "ACCT",
        "ACGA",
        "ACGC",
        "ACGG",
        "ACTA",
        "ACTC",
        "ACTG",
        "AGAA",
        "AGAC",
        "AGAG",
        "AGAT",
        "AGCA",
        "AGCC",
        "AGCG",
        "AGGA",
        "AGGC",
        "AGGG",
        "AGTA",
        "AGTC",
        "AGTG",
        "ATAA",
        "ATAC",
        "ATAG",
        "ATCA",
        "ATCC",
        "ATCG",
        "ATGA",
        "ATGC",
        "ATGG",
        "ATTA",
        "ATTC",
        "ATTG",
        "CAAA",
        "CAAC",
        "CAAG",
        "CACA",
        "CACC",
        "CACG",
        "CAGA",
        "CAGC",
        "CAGG",
        "CATA",
        "CATC",
        "CCAA",
        "CCAC",
        "CCAG",
        "CCCA",
        "CCCC",
        "CCCG",
        "CCGA",
        "CCGC",
        "CCTA",
        "CCTC",
        "CGAA",
        "CGAC",
        "CGAG",
        "CGCA",
        "CGCC",
        "CGGA",
        "CGGC",
        "CGTA",
        "CGTC",
        "CTAA",
        "CTAC",
        "CTCA",
        "CTCC",
        "CTGA",
        "CTGC",
        "CTTA",
        "CTTC",
        "GAAA",
        "GAAC",
        "GACA",
        "GACC",
        "GAGA",
        "GAGC",
        "GATA",
        "GCAA",
        "GCAC",
        "GCCA",
        "GCCC",
        "GCGA",
        "GCTA",
        "GGAA",
        "GGAC",
        "GGCA",
        "GGGA",
        "GGTA",
        "GTAA",
        "GTCA",
        "GTGA",
        "GTTA",
        "TAAA",
        "TACA",
        "TAGA",
        "TCAA",
        "TCCA",
        "TGAA",
    ]


def test_relative_self_annealings():
    assert (
        len(
            tatapov.utils.relative_self_annealings(
                tatapov.annealing_data["37C"]["01h"]
            ).keys()
        )
        == 240
    )


def test_cross_annealing():
    assert (
        tatapov.utils.cross_annealing(
            tatapov.annealing_data["37C"]["01h"], overhangs=["AAGG", "GGCC", "CCTT"]
        )
        == 0.0
    )


def test_cross_annealings():
    assert (
        len(tatapov.utils.cross_annealings(tatapov.annealing_data["37C"]["01h"]).keys())
        == 57360
    )


def test_standardize_overhang():
    assert tatapov.utils.standardize_overhang("AACG") == "AACG"
    assert tatapov.utils.standardize_overhang("TTCG") == "CGAA"


def test_standardize_overhang_pair():
    assert tatapov.utils.standardize_overhang_pair(["AACG", "TTCG"]) == ("AACG", "CGAA")
