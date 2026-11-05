"""
Automated Unit Tests for Sorting Algorithms
Verification & Validation (CMMI VER/VAL)
"""
import random
import pytest
from src.algorithms.bubbleSort import bubbleSort
from src.algorithms.insertionSort import insertionSort
from src.algorithms.selectionSort import selectionSort
from src.algorithms.mergeSort import mergeSort
from src.algorithms.quickSort import quickSort
from src.algorithms.heapSort import heapSort
from src.algorithms.shellSort import shellSort
from src.algorithms.countingSort import countingSort
from algorithmPush import ALGORITHMS_DICT, ALGORITHM_METADATA


def dummy_draw(data, color_array=None, *args, **kwargs):
    """No-op draw callback for headless unit testing."""
    pass


@pytest.mark.parametrize("sort_func", [
    bubbleSort,
    insertionSort,
    selectionSort,
    mergeSort,
    quickSort,
    heapSort,
    shellSort,
])
def test_comparison_sort_correctness(sort_func):
    """Test all comparison sort algorithms against multiple input variations."""
    test_cases = [
        [],                                 # Empty
        [42],                               # Single
        [1, 2, 3, 4, 5],                    # Pre-sorted
        [5, 4, 3, 2, 1],                    # Reversed
        [3, 3, 3, 3, 3],                    # Identical
        [64, 34, 25, 12, 22, 11, 90],       # Standard positive
        [-5, 10, -20, 0, 15, -1, 8],        # Negative & positive
    ]

    for original in test_cases:
        arr = original.copy()
        expected = sorted(original)
        metrics = {"comparisons": 0, "swaps": 0}

        sort_func(arr, dummy_draw, 0, metrics_tracker=metrics)
        assert arr == expected, f"Failed on {original} with {sort_func.__name__}"


def test_counting_sort_correctness():
    """Counting sort operates on non-negative or bounded integers."""
    test_cases = [
        [],
        [10],
        [5, 1, 9, 3, 7, 4],
        [0, 0, 5, 2, 2, 8, 1],
        [100, 50, 75, 25, 10],
    ]
    for original in test_cases:
        arr = original.copy()
        expected = sorted(original)
        countingSort(arr, dummy_draw, 0)
        assert arr == expected


def test_quick_sort_legacy_signature():
    """Verify quick sort backwards compatibility with legacy (data, head, tail, draw, tick)."""
    data = [29, 10, 14, 37, 13]
    expected = sorted(data)
    quickSort(data, 0, len(data) - 1, dummy_draw, 0)
    assert data == expected


def test_metrics_tracking():
    """Ensure algorithms populate comparisons and swaps correctly."""
    data = [5, 1, 4, 2, 8]
    metrics = {"comparisons": 0, "swaps": 0}
    bubbleSort(data, dummy_draw, 0, metrics_tracker=metrics)
    assert data == [1, 2, 4, 5, 8]
    assert metrics["comparisons"] > 0
    assert metrics["swaps"] > 0


def test_random_large_datasets():
    """Verify stability and correctness across random generated datasets."""
    random.seed(42)
    for _ in range(5):
        sample = [random.randint(-100, 100) for _ in range(50)]
        expected = sorted(sample)

        for algo in [bubbleSort, insertionSort, selectionSort, mergeSort, quickSort, heapSort, shellSort]:
            arr = sample.copy()
            algo(arr, dummy_draw, 0)
            assert arr == expected, f"{algo.__name__} failed on random dataset"
