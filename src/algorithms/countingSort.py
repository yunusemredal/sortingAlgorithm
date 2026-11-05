"""
Counting Sort Algorithm Implementation with Visualization Callback
Complexity:
    - Time: O(n + k) where k is the range of input
    - Space: O(n + k) Auxiliary
"""
import time
from typing import Callable, List, Optional


def countingSort(
    data: List[int],
    drawData: Callable,
    timeTick: float = 0.05,
    metrics_tracker: Optional[dict] = None
) -> None:
    """Counting sort with distribution and placement visualization."""
    if not data or len(data) <= 1:
        return

    n = len(data)
    min_val = min(data)
    max_val = max(data)
    k = max_val - min_val + 1

    # Safety check: if range is excessively huge, avoid excessive memory allocation
    if k > 10000:
        return

    count = [0] * k
    output = [0] * n

    # Step 1: Count frequencies
    for i in range(n):
        count[data[i] - min_val] += 1
        if metrics_tracker is not None:
            metrics_tracker["comparisons"] = metrics_tracker.get("comparisons", 0) + 1
        drawData(data, ["#ecc94b" if x == i else "#4a5568" for x in range(n)])
        if timeTick > 0:
            time.sleep(timeTick)

    # Step 2: Accumulate counts
    for i in range(1, k):
        count[i] += count[i - 1]

    # Step 3: Build output array
    for i in range(n - 1, -1, -1):
        val = data[i]
        pos = count[val - min_val] - 1
        output[pos] = val
        count[val - min_val] -= 1
        if metrics_tracker is not None:
            metrics_tracker["swaps"] = metrics_tracker.get("swaps", 0) + 1

    # Step 4: Copy back to data with visual animation
    for i in range(n):
        data[i] = output[i]
        drawData(data, ["#38a169" if x <= i else "#4a5568" for x in range(n)])
        if timeTick > 0:
            time.sleep(timeTick)

    drawData(data, ["green" for _ in range(n)])

