"""
Shell Sort Algorithm Implementation with Visualization Callback
Complexity:
    - Time: O(n log n) Best, O(n^(3/2)) or O(n²) Worst (depending on gap sequence)
    - Space: O(1) Auxiliary
"""
import time
from typing import Callable, List, Optional


def shellSort(
    data: List[int],
    drawData: Callable,
    timeTick: float = 0.05,
    metrics_tracker: Optional[dict] = None
) -> None:
    """Shell Sort with dynamic gap sequence visualization."""
    if not data or len(data) <= 1:
        return

    n = len(data)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = data[i]
            j = i

            drawData(data, _get_color_array(n, current_idx=i, compare_idx=j - gap, gap=gap))
            if timeTick > 0:
                time.sleep(timeTick)

            while j >= gap:
                if metrics_tracker is not None:
                    metrics_tracker["comparisons"] = metrics_tracker.get("comparisons", 0) + 1

                if data[j - gap] > temp:
                    data[j] = data[j - gap]
                    if metrics_tracker is not None:
                        metrics_tracker["swaps"] = metrics_tracker.get("swaps", 0) + 1

                    j -= gap
                    drawData(data, _get_color_array(n, current_idx=j, compare_idx=j, gap=gap, is_shifting=True))
                    if timeTick > 0:
                        time.sleep(timeTick)
                else:
                    break

            data[j] = temp
            drawData(data, _get_color_array(n, current_idx=j, compare_idx=i, gap=gap, is_placed=True))
            if timeTick > 0:
                time.sleep(timeTick)

        gap //= 2

    drawData(data, ["green" for _ in range(n)])


def _get_color_array(
    length: int,
    current_idx: int,
    compare_idx: int,
    gap: int,
    is_shifting: bool = False,
    is_placed: bool = False
) -> List[str]:
    colors = []
    for x in range(length):
        if is_placed and x == current_idx:
            colors.append("#38a169")  # Green for placed
        elif is_shifting and x == current_idx:
            colors.append("#e53e3e")  # Red for shift
        elif x == current_idx:
            colors.append("#ecc94b")  # Yellow for active element
        elif x == compare_idx:
            colors.append("#dd6b20")  # Orange for gap comparison
        elif abs(x - current_idx) % max(gap, 1) == 0:
            colors.append("#3182ce")  # Blue for elements in current gap sequence
        else:
            colors.append("#4a5568")  # Slate gray default
    return colors

