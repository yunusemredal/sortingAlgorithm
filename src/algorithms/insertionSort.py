"""
Insertion Sort Algorithm Implementation with Visualization Callback
Complexity:
    - Time: O(n) Best, O(n²) Average / Worst
    - Space: O(1) Auxiliary
"""
import time
from typing import Callable, List, Optional


def insertionSort(
    data: List[int],
    drawData: Callable,
    timeTick: float = 0.05,
    metrics_tracker: Optional[dict] = None
) -> None:
    """
    Insertion Sort with step-by-step visual feedback.
    """
    if not data or len(data) <= 1:
        return

    n = len(data)
    for i in range(1, n):
        key = data[i]
        j = i - 1

        # Highlight key element to be inserted
        drawData(data, _get_color_array(n, current_idx=i, key_idx=i))
        if timeTick > 0:
            time.sleep(timeTick)

        while j >= 0:
            if metrics_tracker is not None:
                metrics_tracker["comparisons"] = metrics_tracker.get("comparisons", 0) + 1

            if data[j] > key:
                data[j + 1] = data[j]
                if metrics_tracker is not None:
                    metrics_tracker["swaps"] = metrics_tracker.get("swaps", 0) + 1

                j -= 1
                drawData(data, _get_color_array(n, current_idx=j + 1, key_idx=i, is_shifting=True))
                if timeTick > 0:
                    time.sleep(timeTick)
            else:
                break

        data[j + 1] = key
        drawData(data, _get_color_array(n, current_idx=j + 1, key_idx=i, is_placed=True))
        if timeTick > 0:
            time.sleep(timeTick)

    drawData(data, ["green" for _ in range(n)])


def _get_color_array(
    length: int,
    current_idx: int,
    key_idx: int,
    is_shifting: bool = False,
    is_placed: bool = False
) -> List[str]:
    colors = []
    for x in range(length):
        if is_placed and x == current_idx:
            colors.append("#38a169")  # Green for settled key placement
        elif x == current_idx:
            colors.append("#e53e3e" if is_shifting else "#ecc94b")  # Red for shift, Yellow for comparison
        elif x == key_idx:
            colors.append("#dd6b20")  # Orange for the original key slot
        elif x < key_idx:
            colors.append("#3182ce")  # Blue for sorted prefix
        else:
            colors.append("#4a5568")  # Slate gray for unprocessed elements
    return colors
