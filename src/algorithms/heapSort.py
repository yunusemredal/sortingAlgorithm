"""
Heap Sort Algorithm Implementation with Visualization Callback
Complexity:
    - Time: O(n log n) Best / Average / Worst
    - Space: O(1) Auxiliary
"""
import time
from typing import Callable, List, Optional


def heapSort(
    data: List[int],
    drawData: Callable,
    timeTick: float = 0.05,
    metrics_tracker: Optional[dict] = None
) -> None:
    """Heap Sort with binary heap visualization."""
    if not data or len(data) <= 1:
        return

    n = len(data)

    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        _heapify(data, n, i, drawData, timeTick, metrics_tracker)

    # Extract elements one by one from heap
    for i in range(n - 1, 0, -1):
        # Move current root to end
        data[i], data[0] = data[0], data[i]
        if metrics_tracker is not None:
            metrics_tracker["swaps"] = metrics_tracker.get("swaps", 0) + 1

        drawData(data, _get_color_array(n, heap_size=i, root=0, largest=i, is_swapping=True))
        if timeTick > 0:
            time.sleep(timeTick)

        # Call max heapify on reduced heap
        _heapify(data, i, 0, drawData, timeTick, metrics_tracker)

    drawData(data, ["green" for _ in range(n)])


def _heapify(
    data: List[int],
    n: int,
    i: int,
    drawData: Callable,
    timeTick: float,
    metrics_tracker: Optional[dict] = None
) -> None:
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n:
        if metrics_tracker is not None:
            metrics_tracker["comparisons"] = metrics_tracker.get("comparisons", 0) + 1
        if data[left] > data[largest]:
            largest = left

    if right < n:
        if metrics_tracker is not None:
            metrics_tracker["comparisons"] = metrics_tracker.get("comparisons", 0) + 1
        if data[right] > data[largest]:
            largest = right

    if largest != i:
        drawData(data, _get_color_array(len(data), heap_size=n, root=i, largest=largest, is_swapping=True))
        if timeTick > 0:
            time.sleep(timeTick)

        data[i], data[largest] = data[largest], data[i]
        if metrics_tracker is not None:
            metrics_tracker["swaps"] = metrics_tracker.get("swaps", 0) + 1

        _heapify(data, n, largest, drawData, timeTick, metrics_tracker)
    else:
        drawData(data, _get_color_array(len(data), heap_size=n, root=i, largest=largest))
        if timeTick > 0:
            time.sleep(timeTick)


def _get_color_array(
    length: int,
    heap_size: int,
    root: int,
    largest: int,
    is_swapping: bool = False
) -> List[str]:
    colors = []
    for x in range(length):
        if x >= heap_size:
            colors.append("#38a169")  # Green for sorted tail
        elif is_swapping and (x == root or x == largest):
            colors.append("#e53e3e")  # Red for swap
        elif x == root:
            colors.append("#dd6b20")  # Orange for subtree root
        elif x == largest:
            colors.append("#ecc94b")  # Yellow for largest candidate
        else:
            colors.append("#4a5568")  # Slate gray for heap elements
    return colors

