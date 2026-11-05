"""
Algorithm Registry and Metadata Specification
Maps algorithm keys to execution functions and theoretical complexity models.
"""
import sys
from pathlib import Path

# Add project root to sys.path to enable flexible importing
project_root = Path(__file__).resolve().parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from src.algorithms.bubbleSort import bubbleSort
from src.algorithms.selectionSort import selectionSort
from src.algorithms.quickSort import quickSort
from src.algorithms.mergeSort import mergeSort
from src.algorithms.insertionSort import insertionSort
from src.algorithms.heapSort import heapSort
from src.algorithms.shellSort import shellSort
from src.algorithms.countingSort import countingSort

# Primary lookup dictionary for display UI and CLI invocation
algorithmsDict = {
    'Bubble Sort': bubbleSort,
    'Insertion Sort': insertionSort,
    'Selection Sort': selectionSort,
    'Merge Sort': mergeSort,
    'Quick Sort': quickSort,
    'Heap Sort': heapSort,
    'Shell Sort': shellSort,
    'Counting Sort': countingSort,
    # Short names alias support
    'bubble': bubbleSort,
    'insertion': insertionSort,
    'selection': selectionSort,
    'merge': mergeSort,
    'quick': quickSort,
    'heap': heapSort,
    'shell': shellSort,
    'counting': countingSort,
}

ALGORITHMS_DICT = algorithmsDict

# Detailed algorithm metadata for UI cards & complexity reports
ALGORITHM_METADATA = {
    'Bubble Sort': {
        'func': bubbleSort,
        'best_time': 'O(n)',
        'avg_time': 'O(n²)',
        'worst_time': 'O(n²)',
        'space': 'O(1)',
        'stable': True,
        'description': 'Komşu elemanları karşılaştırarak sırasız olanları yer değiştirir. Erken bitiş optimizasyonu içerir.'
    },
    'Insertion Sort': {
        'func': insertionSort,
        'best_time': 'O(n)',
        'avg_time': 'O(n²)',
        'worst_time': 'O(n²)',
        'space': 'O(1)',
        'stable': True,
        'description': 'Diziyi sıralı ve sırasız iki parçaya ayırıp, her elemanı sıralı kısımdaki doğru yerine yerleştirir.'
    },
    'Selection Sort': {
        'func': selectionSort,
        'best_time': 'O(n²)',
        'avg_time': 'O(n²)',
        'worst_time': 'O(n²)',
        'space': 'O(1)',
        'stable': False,
        'description': 'Sıralanmamış kısımdaki en küçük elemanı bulup sıralı kısmın sonuna yerleştirir.'
    },
    'Merge Sort': {
        'func': mergeSort,
        'best_time': 'O(n log n)',
        'avg_time': 'O(n log n)',
        'worst_time': 'O(n log n)',
        'space': 'O(n)',
        'stable': True,
        'description': 'Böl ve yönet (Divide & Conquer) yaklaşımı ile diziyi ikiye böler, sıralar ve birleştirir.'
    },
    'Quick Sort': {
        'func': quickSort,
        'best_time': 'O(n log n)',
        'avg_time': 'O(n log n)',
        'worst_time': 'O(n²)',
        'space': 'O(log n)',
        'stable': False,
        'description': 'Pivot eleman seçip diziyi pivottan küçük ve büyük olarak ikiye böler ve özyinelemeli sıralar.'
    },
    'Heap Sort': {
        'func': heapSort,
        'best_time': 'O(n log n)',
        'avg_time': 'O(n log n)',
        'worst_time': 'O(n log n)',
        'space': 'O(1)',
        'stable': False,
        'description': 'İkili tepe (binary max-heap) veri yapısı kurarak en büyük elemanı kökten çıkarıp sona koyar.'
    },
    'Shell Sort': {
        'func': shellSort,
        'best_time': 'O(n log n)',
        'avg_time': 'O(n^(3/2))',
        'worst_time': 'O(n²)',
        'space': 'O(1)',
        'stable': False,
        'description': 'Belirli aralıklarla (gap) elemanları karşılaştırıp aralığı daraltan gelişmiş eklemeli sıralama.'
    },
    'Counting Sort': {
        'func': countingSort,
        'best_time': 'O(n + k)',
        'avg_time': 'O(n + k)',
        'worst_time': 'O(n + k)',
        'space': 'O(n + k)',
        'stable': True,
        'description': 'Karşılaştırmasız algoritma. Eleman frekanslarını sayarak doğrudan indislerine yerleştirir.'
    },
}
