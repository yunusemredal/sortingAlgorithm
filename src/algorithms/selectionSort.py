"""
Selection Sort Algorithm Implementation with Visualization Callback
Complexity:
    - Time: O(n²) Best / Average / Worst
    - Space: O(1) Auxiliary
"""
import time
from typing import Callable, List, Optional


def selectionSort(
    data: List[int],
    drawData: Callable,
    timeTick: float = 0.05,
    metrics_tracker: Optional[dict] = None
) -> None:
    """
    Selection Sort with dynamic visualization for scanned elements and minimum candidate.
    """
    if not data or len(data) <= 1:
        return

    n = len(data)
    for i in range(n):
        min_idx = i

        for j in range(i + 1, n):
            if metrics_tracker is not None:
                metrics_tracker["comparisons"] = metrics_tracker.get("comparisons", 0) + 1

            # Visualize scanning element j and current candidate min_idx
            drawData(data, _get_color_array(n, sorted_until=i, current_target=i, current_min=min_idx, scanning_idx=j))
            if timeTick > 0:
                time.sleep(timeTick)

            if data[j] < data[min_idx]:
                min_idx = j
                drawData(data, _get_color_array(n, sorted_until=i, current_target=i, current_min=min_idx, scanning_idx=j))
                if timeTick > 0:
                    time.sleep(timeTick)

        if min_idx != i:
            data[i], data[min_idx] = data[min_idx], data[i]
            if metrics_tracker is not None:
                metrics_tracker["swaps"] = metrics_tracker.get("swaps", 0) + 1

            drawData(data, _get_color_array(n, sorted_until=i, current_target=i, current_min=min_idx, is_swapping=True))
            if timeTick > 0:
                time.sleep(timeTick)

    drawData(data, ["green" for _ in range(n)])


def _get_color_array(
    length: int,
    sorted_until: int,
    current_target: int,
    current_min: int,
    scanning_idx: Optional[int] = None,
    is_swapping: bool = False
) -> List[str]:
    colors = []
    for x in range(length):
        if x < sorted_until:
            colors.append("#38a169")  # Green for finalized prefix
        elif is_swapping and (x == current_target or x == current_min):
            colors.append("#e53e3e")  # Red for swap
        elif x == current_min:
            colors.append("#9f7aea")  # Purple for current minimum candidate
        elif x == scanning_idx:
            colors.append("#ecc94b")  # Yellow for active scan probe
        elif x == current_target:
            colors.append("#dd6b20")  # Orange for target slot to fill
        else:
            colors.append("#4a5568")  # Slate gray for unprocessed elements
    return colors
