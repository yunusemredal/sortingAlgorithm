"""
Merge Sort Algorithm Implementation with Visualization Callback
Complexity:
    - Time: O(n log n) Best / Average / Worst
    - Space: O(n) Auxiliary
"""
import time
from typing import Callable, List, Optional


def mergeSort(
    data: List[int],
    drawData: Callable,
    timeTick: float = 0.05,
    metrics_tracker: Optional[dict] = None
) -> None:
    """Entry point for Merge Sort."""
    if not data or len(data) <= 1:
        return
    _merge_sort_recursive(data, 0, len(data) - 1, drawData, timeTick, metrics_tracker)
    drawData(data, ["green" for _ in range(len(data))])


def _merge_sort_recursive(
    data: List[int],
    left: int,
    right: int,
    drawData: Callable,
    timeTick: float,
    metrics_tracker: Optional[dict] = None
) -> None:
    if left < right:
        mid = (left + right) // 2
        _merge_sort_recursive(data, left, mid, drawData, timeTick, metrics_tracker)
        _merge_sort_recursive(data, mid + 1, right, drawData, timeTick, metrics_tracker)
        _merge(data, left, mid, right, drawData, timeTick, metrics_tracker)


def _merge(
    data: List[int],
    left: int,
    mid: int,
    right: int,
    drawData: Callable,
    timeTick: float,
    metrics_tracker: Optional[dict] = None
) -> None:
    # Highlight current partition being merged
    drawData(data, _get_color_array(len(data), left, mid, right))
    if timeTick > 0:
        time.sleep(timeTick)

    left_part = data[left : mid + 1]
    right_part = data[mid + 1 : right + 1]

    left_idx = 0
    right_idx = 0
    data_idx = left

    # Bug fix: loop must include 'right' (inclusive range: left to right)
    while left_idx < len(left_part) and right_idx < len(right_part):
        if metrics_tracker is not None:
            metrics_tracker["comparisons"] = metrics_tracker.get("comparisons", 0) + 1

        if left_part[left_idx] <= right_part[right_idx]:
            data[data_idx] = left_part[left_idx]
            left_idx += 1
        else:
            data[data_idx] = right_part[right_idx]
            right_idx += 1

        if metrics_tracker is not None:
            metrics_tracker["swaps"] = metrics_tracker.get("swaps", 0) + 1

        data_idx += 1
        drawData(data, _get_color_array(len(data), left, mid, right, active_idx=data_idx - 1))
        if timeTick > 0:
            time.sleep(timeTick)

    while left_idx < len(left_part):
        data[data_idx] = left_part[left_idx]
        left_idx += 1
        data_idx += 1
        if metrics_tracker is not None:
            metrics_tracker["swaps"] = metrics_tracker.get("swaps", 0) + 1
        drawData(data, _get_color_array(len(data), left, mid, right, active_idx=data_idx - 1))
        if timeTick > 0:
            time.sleep(timeTick)

    while right_idx < len(right_part):
        data[data_idx] = right_part[right_idx]
        right_idx += 1
        data_idx += 1
        if metrics_tracker is not None:
            metrics_tracker["swaps"] = metrics_tracker.get("swaps", 0) + 1
        drawData(data, _get_color_array(len(data), left, mid, right, active_idx=data_idx - 1))
        if timeTick > 0:
            time.sleep(timeTick)

    # Subarray sorted indicator
    drawData(
        data,
        ["lightgreen" if left <= idx <= right else "#4a5568" for idx in range(len(data))]
    )
    if timeTick > 0:
        time.sleep(timeTick)


def _get_color_array(
    length: int,
    left: int,
    mid: int,
    right: int,
    active_idx: Optional[int] = None
) -> List[str]:
    """Generates color-coded array for visual tracking during merge operations."""
    colors = []
    for i in range(length):
        if i == active_idx:
            colors.append("#e53e3e")  # Bright red for actively written element
        elif left <= i <= mid:
            colors.append("#ecc94b")  # Yellow for left partition
        elif mid < i <= right:
            colors.append("#ed64a6")  # Pink for right partition
        else:
            colors.append("#4a5568")  # Slate gray for inactive elements
    return colors
