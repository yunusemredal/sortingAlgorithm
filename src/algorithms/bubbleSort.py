"""
Bubble Sort Algorithm Implementation with Visualization Callback
Complexity:
    - Time: O(n) Best (early exit), O(n²) Average / Worst
    - Space: O(1) Auxiliary
"""
import time
from typing import Callable, List, Optional


def bubbleSort(
    data: List[int],
    drawData: Callable,
    timeTick: float = 0.05,
    metrics_tracker: Optional[dict] = None
) -> None:
    """
    Optimized Bubble Sort with early termination and visual state coloring.
    """
    if not data or len(data) <= 1:
        return

    n = len(data)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if metrics_tracker is not None:
                metrics_tracker["comparisons"] = metrics_tracker.get("comparisons", 0) + 1

            # Highlight compared elements
            drawData(data, _get_color_array(n, j, j + 1, n - i))
            if timeTick > 0:
                time.sleep(timeTick)

            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped = True
                if metrics_tracker is not None:
                    metrics_tracker["swaps"] = metrics_tracker.get("swaps", 0) + 1

                # Highlight swapped elements
                drawData(data, _get_color_array(n, j, j + 1, n - i, is_swapping=True))
                if timeTick > 0:
                    time.sleep(timeTick)

        # If no two elements were swapped by inner loop, array is sorted
        if not swapped:
            break

    drawData(data, ["green" for _ in range(n)])


def _get_color_array(
    length: int,
    idx1: int,
    idx2: int,
    sorted_boundary: int,
    is_swapping: bool = False
) -> List[str]:
    colors = []
    for x in range(length):
        if x >= sorted_boundary:
            colors.append("#38a169")  # Green for settled elements
        elif x == idx1 or x == idx2:
            colors.append("#e53e3e" if is_swapping else "#ecc94b")  # Red for swap, Yellow for comparison
        else:
            colors.append("#4a5568")  # Slate gray default
    return colors
