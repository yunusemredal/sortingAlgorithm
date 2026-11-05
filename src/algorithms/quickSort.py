"""
Quick Sort Algorithm Implementation with Visualization Callback
Complexity:
    - Time: O(n log n) Best / Average, O(n²) Worst
    - Space: O(log n) Auxiliary (Recursive Stack)
"""
import time
from typing import Callable, List, Optional


def quickSort(data: List[int], *args, **kwargs) -> None:
    """
    Entry point for Quick Sort.
    Supports both legacy signature:
        quickSort(data, head, tail, drawData, timeTick)
    and standard unified signature:
        quickSort(data, drawData, timeTick=0.05, metrics_tracker=None)
    """
    if not data or len(data) <= 1:
        return

    # Check argument patterns for backwards compatibility
    if len(args) >= 3 and isinstance(args[0], int) and isinstance(args[1], int):
        head = args[0]
        tail = args[1]
        drawData = args[2]
        timeTick = args[3] if len(args) > 3 else kwargs.get("timeTick", 0.05)
        metrics_tracker = kwargs.get("metrics_tracker", None)
    elif len(args) >= 1 and callable(args[0]):
        head = 0
        tail = len(data) - 1
        drawData = args[0]
        timeTick = args[1] if len(args) > 1 else kwargs.get("timeTick", 0.05)
        metrics_tracker = kwargs.get("metrics_tracker", None)
    else:
        head = 0
        tail = len(data) - 1
        drawData = kwargs.get("drawData")
        timeTick = kwargs.get("timeTick", 0.05)
        metrics_tracker = kwargs.get("metrics_tracker", None)

    if drawData is None:
        raise ValueError("drawData callback must be provided.")

    _quick_sort_recursive(data, head, tail, drawData, timeTick, metrics_tracker)
    drawData(data, ["green" for _ in range(len(data))])


def _quick_sort_recursive(
    data: List[int],
    head: int,
    tail: int,
    drawData: Callable,
    timeTick: float,
    metrics_tracker: Optional[dict] = None
) -> None:
    if head < tail:
        partition_idx = _partition(data, head, tail, drawData, timeTick, metrics_tracker)
        _quick_sort_recursive(data, head, partition_idx - 1, drawData, timeTick, metrics_tracker)
        _quick_sort_recursive(data, partition_idx + 1, tail, drawData, timeTick, metrics_tracker)


def _partition(
    data: List[int],
    head: int,
    tail: int,
    drawData: Callable,
    timeTick: float,
    metrics_tracker: Optional[dict] = None
) -> int:
    border = head
    pivot = data[tail]

    drawData(data, _get_color_array(len(data), head, tail, border, border))
    if timeTick > 0:
        time.sleep(timeTick)

    for j in range(head, tail):
        if metrics_tracker is not None:
            metrics_tracker["comparisons"] = metrics_tracker.get("comparisons", 0) + 1

        if data[j] < pivot:
            drawData(data, _get_color_array(len(data), head, tail, border, j, is_swapping=True))
            if timeTick > 0:
                time.sleep(timeTick)

            data[border], data[j] = data[j], data[border]
            if metrics_tracker is not None:
                metrics_tracker["swaps"] = metrics_tracker.get("swaps", 0) + 1

            border += 1

        drawData(data, _get_color_array(len(data), head, tail, border, j))
        if timeTick > 0:
            time.sleep(timeTick)

    # Swap pivot with element at border
    drawData(data, _get_color_array(len(data), head, tail, border, tail, is_swapping=True))
    if timeTick > 0:
        time.sleep(timeTick)

    data[border], data[tail] = data[tail], data[border]
    if metrics_tracker is not None:
        metrics_tracker["swaps"] = metrics_tracker.get("swaps", 0) + 1

    return border


def _get_color_array(
    data_len: int,
    head: int,
    tail: int,
    border: int,
    curr_idx: int,
    is_swapping: bool = False
) -> List[str]:
    """Generates color mapping for Quick Sort visualization."""
    color_array = []
    for i in range(data_len):
        # Base partition range
        if head <= i <= tail:
            color_array.append("#4a5568")  # Slate gray for current active subsegment
        else:
            color_array.append("#2d3748")  # Dark gray for inactive elements

        if i == tail:
            color_array[i] = "#dd6b20"    # Orange for pivot element
        elif i == border:
            color_array[i] = "#e53e3e"    # Red for border marker
        elif i == curr_idx:
            color_array[i] = "#d69e2e"    # Yellow for current scanning element

        if is_swapping:
            if i == border or i == curr_idx:
                color_array[i] = "#38a169"  # Green for swapping elements

    return color_array
