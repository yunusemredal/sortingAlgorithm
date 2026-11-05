"""
Interactive Sorting Algorithm Visualizer GUI
Engineered according to CMMI Technical Solution (TS) and Verification (VER) standards.
Provides real-time non-blocking animation, thread-safe controls, and dynamic performance metrics.
"""
import random
import sys
import threading
import time
from pathlib import Path
import tkinter as tk
from tkinter import messagebox, ttk
from typing import List, Optional

# Ensure project root in sys.path
PROJECT_ROOT = Path(__file__).resolve().parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from algorithmPush import ALGORITHMS_DICT, ALGORITHM_METADATA
from src.graf.grafics import show_complexity_window


class StopAlgorithmException(Exception):
    """Exception raised inside visualization callback to cleanly abort algorithm execution."""
    pass


class SortingVisualizerApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Sıralama Algoritmaları Görselleştiricisi")
        self.root.geometry("1180x820")
        self.root.minsize(980, 680)
        self.root.configure(bg="#1a202c")

        # Execution State
        self.data: List[int] = []
        self.is_running: bool = False
        self.is_paused: bool = False
        self.stop_requested: bool = False
        self.worker_thread: Optional[threading.Thread] = None

        # Metrics Tracker
        self.metrics = {"comparisons": 0, "swaps": 0}
        self.start_time: float = 0.0
        self.elapsed_time: float = 0.0

        # Build UI
        self._setup_styles()
        self._build_header_and_controls()
        self._build_dashboard()
        self._build_canvas()
        self._build_status_bar()

        # Initial data generation
        self.generate_dataset()

        # Window close handler
        self.root.protocol("WM_DELETE_WINDOW", self._on_close)

    def _setup_styles(self):
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TCombobox", fieldbackground="#2d3748", background="#4a5568", foreground="#ffffff")
        style.configure("Horizontal.TScale", background="#1a202c")

    def _build_header_and_controls(self):
        control_frame = tk.Frame(self.root, bg="#2d3748", padx=16, pady=12, relief=tk.RAISED, bd=1)
        control_frame.pack(fill=tk.X, padx=12, pady=(10, 6))

        # Row 1: Algorithm selection and Primary action buttons
        row1 = tk.Frame(control_frame, bg="#2d3748")
        row1.pack(fill=tk.X, pady=(0, 8))

        lbl_algo = tk.Label(row1, text="Algoritma:", font=("Segoe UI", 11, "bold"), fg="#e2e8f0", bg="#2d3748")
        lbl_algo.pack(side=tk.LEFT, padx=(0, 6))

        self.algo_var = tk.StringVar(value="Bubble Sort")
        self.algo_menu = ttk.Combobox(
            row1,
            textvariable=self.algo_var,
            values=list(ALGORITHM_METADATA.keys()),
            state="readonly",
            width=16,
            font=("Segoe UI", 10, "bold")
        )
        self.algo_menu.pack(side=tk.LEFT, padx=(0, 16))
        self.algo_menu.bind("<<ComboboxSelected>>", self._on_algorithm_change)

        lbl_type = tk.Label(row1, text="Dizi Tipi:", font=("Segoe UI", 10), fg="#e2e8f0", bg="#2d3748")
        lbl_type.pack(side=tk.LEFT, padx=(0, 4))

        self.distribution_var = tk.StringVar(value="Rastgele")
        self.distribution_menu = ttk.Combobox(
            row1,
            textvariable=self.distribution_var,
            values=["Rastgele", "Neredeyse Sıralı", "Ters Sıralı", "Tekrarlı Değerler"],
            state="readonly",
            width=15,
            font=("Segoe UI", 9)
        )
        self.distribution_menu.pack(side=tk.LEFT, padx=(0, 16))

        # Buttons
        self.btn_generate = tk.Button(
            row1,
            text="🎲 Yeni Dizi",
            command=self.generate_dataset,
            bg="#3182ce",
            fg="white",
            activebackground="#2b6cb0",
            activeforeground="white",
            font=("Segoe UI", 10, "bold"),
            relief=tk.FLAT,
            padx=12,
            pady=4,
            cursor="hand2"
        )
        self.btn_generate.pack(side=tk.LEFT, padx=4)

        self.btn_start = tk.Button(
            row1,
            text="▶ Başlat",
            command=self.start_algorithm,
            bg="#38a169",
            fg="white",
            activebackground="#2f855a",
            activeforeground="white",
            font=("Segoe UI", 10, "bold"),
            relief=tk.FLAT,
            padx=16,
            pady=4,
            cursor="hand2"
        )
        self.btn_start.pack(side=tk.LEFT, padx=4)

        self.btn_pause = tk.Button(
            row1,
            text="⏸ Duraklat",
            command=self.toggle_pause,
            bg="#d69e2e",
            fg="white",
            activebackground="#b7791f",
            activeforeground="white",
            font=("Segoe UI", 10, "bold"),
            relief=tk.FLAT,
            padx=12,
            pady=4,
            state=tk.DISABLED,
            cursor="hand2"
        )
        self.btn_pause.pack(side=tk.LEFT, padx=4)

        self.btn_stop = tk.Button(
            row1,
            text="⏹ Sıfırla",
            command=self.stop_algorithm,
            bg="#e53e3e",
            fg="white",
            activebackground="#c53030",
            activeforeground="white",
            font=("Segoe UI", 10, "bold"),
            relief=tk.FLAT,
            padx=12,
            pady=4,
            state=tk.DISABLED,
            cursor="hand2"
        )
        self.btn_stop.pack(side=tk.LEFT, padx=4)

        self.btn_graph = tk.Button(
            row1,
            text="📊 Karmaşıklık Grafiği",
            command=self.open_complexity_graph,
            bg="#805ad5",
            fg="white",
            activebackground="#6b46c1",
            activeforeground="white",
            font=("Segoe UI", 10, "bold"),
            relief=tk.FLAT,
            padx=12,
            pady=4,
            cursor="hand2"
        )
        self.btn_graph.pack(side=tk.RIGHT, padx=4)

        # Row 2: Sliders for Size, Min/Max value, and Speed
        row2 = tk.Frame(control_frame, bg="#2d3748")
        row2.pack(fill=tk.X)

        # Size slider
        tk.Label(row2, text="Boyut (n):", font=("Segoe UI", 9, "bold"), fg="#cbd5e0", bg="#2d3748").pack(side=tk.LEFT, padx=(0, 4))
        self.size_scale = tk.Scale(
            row2, from_=5, to=100, orient=tk.HORIZONTAL, bg="#2d3748", fg="#e2e8f0",
            highlightthickness=0, troughcolor="#4a5568", activebackground="#63b3ed",
            length=130, font=("Segoe UI", 8), command=lambda _: self._on_size_change()
        )
        self.size_scale.set(30)
        self.size_scale.pack(side=tk.LEFT, padx=(0, 16))

        # Min Value
        tk.Label(row2, text="Min:", font=("Segoe UI", 9, "bold"), fg="#cbd5e0", bg="#2d3748").pack(side=tk.LEFT, padx=(0, 4))
        self.min_scale = tk.Scale(
            row2, from_=1, to=50, orient=tk.HORIZONTAL, bg="#2d3748", fg="#e2e8f0",
            highlightthickness=0, troughcolor="#4a5568", activebackground="#63b3ed",
            length=100, font=("Segoe UI", 8), command=lambda _: self.generate_dataset()
        )
        self.min_scale.set(5)
        self.min_scale.pack(side=tk.LEFT, padx=(0, 16))

        # Max Value
        tk.Label(row2, text="Max:", font=("Segoe UI", 9, "bold"), fg="#cbd5e0", bg="#2d3748").pack(side=tk.LEFT, padx=(0, 4))
        self.max_scale = tk.Scale(
            row2, from_=20, to=300, orient=tk.HORIZONTAL, bg="#2d3748", fg="#e2e8f0",
            highlightthickness=0, troughcolor="#4a5568", activebackground="#63b3ed",
            length=110, font=("Segoe UI", 8), command=lambda _: self.generate_dataset()
        )
        self.max_scale.set(150)
        self.max_scale.pack(side=tk.LEFT, padx=(0, 16))

        # Speed slider (Delay in ms)
        tk.Label(row2, text="Gecikme (sn):", font=("Segoe UI", 9, "bold"), fg="#cbd5e0", bg="#2d3748").pack(side=tk.LEFT, padx=(0, 4))
        self.speed_scale = tk.Scale(
            row2, from_=0.001, to=0.3, resolution=0.005, orient=tk.HORIZONTAL,
            bg="#2d3748", fg="#e2e8f0", highlightthickness=0, troughcolor="#4a5568",
            activebackground="#63b3ed", length=140, font=("Segoe UI", 8)
        )
        self.speed_scale.set(0.04)
        self.speed_scale.pack(side=tk.LEFT, padx=(0, 10))

    def _build_dashboard(self):
        dash_frame = tk.Frame(self.root, bg="#171923", padx=16, pady=8)
        dash_frame.pack(fill=tk.X, padx=12, pady=(0, 6))

        # Metrics cards
        self.lbl_comparisons = tk.Label(
            dash_frame, text="Karşılaştırma: 0", font=("Segoe UI", 10, "bold"),
            fg="#ecc94b", bg="#232733", padx=10, pady=4, relief=tk.GROOVE
        )
        self.lbl_comparisons.pack(side=tk.LEFT, padx=6)

        self.lbl_swaps = tk.Label(
            dash_frame, text="Yer Değiştirme / Yazma: 0", font=("Segoe UI", 10, "bold"),
            fg="#fc8181", bg="#232733", padx=10, pady=4, relief=tk.GROOVE
        )
        self.lbl_swaps.pack(side=tk.LEFT, padx=6)

        self.lbl_timer = tk.Label(
            dash_frame, text="Süre: 0.00 sn", font=("Segoe UI", 10, "bold"),
            fg="#63b3ed", bg="#232733", padx=10, pady=4, relief=tk.GROOVE
        )
        self.lbl_timer.pack(side=tk.LEFT, padx=6)

        # Complexity badges
        self.lbl_complexity = tk.Label(
            dash_frame,
            text="Zaman: En İyi: O(n) | Ort: O(n²) | Kötü: O(n²)  |  Bellek: O(1)",
            font=("Segoe UI", 9),
            fg="#a0aec0",
            bg="#171923"
        )
        self.lbl_complexity.pack(side=tk.RIGHT, padx=6)
        self._update_complexity_label()

    def _build_canvas(self):
        canvas_container = tk.Frame(self.root, bg="#1a202c")
        canvas_container.pack(fill=tk.BOTH, expand=True, padx=12, pady=(0, 6))

        self.canvas = tk.Canvas(
            canvas_container,
            bg="#11141c",
            highlightthickness=1,
            highlightbackground="#2d3748"
        )
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.canvas.bind("<Configure>", lambda e: self.draw_data(self.data))

    def _build_status_bar(self):
        status_frame = tk.Frame(self.root, bg="#2d3748", padx=12, pady=4)
        status_frame.pack(fill=tk.X, side=tk.BOTTOM)

        self.lbl_status = tk.Label(
            status_frame, text="Durum: Hazır", font=("Segoe UI", 9, "bold"),
            fg="#48bb78", bg="#2d3748"
        )
        self.lbl_status.pack(side=tk.LEFT)

        self.lbl_info = tk.Label(
            status_frame,
            text="Etkileşimli Görselleştirme ve Performans Analizi",
            font=("Segoe UI", 8),
            fg="#718096",
            bg="#2d3748"
        )
        self.lbl_info.pack(side=tk.RIGHT)

    def _on_algorithm_change(self, event=None):
        self._update_complexity_label()

    def _update_complexity_label(self):
        meta = ALGORITHM_METADATA.get(self.algo_var.get(), {})
        if meta:
            best = meta.get("best_time", "-")
            avg = meta.get("avg_time", "-")
            worst = meta.get("worst_time", "-")
            space = meta.get("space", "-")
            self.lbl_complexity.config(
                text=f"Zaman: En İyi: {best} | Ort: {avg} | Kötü: {worst}  |  Bellek: {space}"
            )

    def _on_size_change(self):
        if not self.is_running:
            self.generate_dataset()

    def generate_dataset(self):
        """Generates array based on selected size, ranges, and distribution."""
        if self.is_running:
            return

        size = int(self.size_scale.get())
        min_v = int(self.min_scale.get())
        max_v = int(self.max_scale.get())

        if min_v > max_v:
            min_v, max_v = max_v, min_v
            self.min_scale.set(min_v)
            self.max_scale.set(max_v)

        dist = self.distribution_var.get()
        if dist == "Neredeyse Sıralı":
            arr = list(range(min_v, min_v + size))
            swaps_count = max(1, size // 10)
            for _ in range(swaps_count):
                i1, i2 = random.randint(0, size - 1), random.randint(0, size - 1)
                arr[i1], arr[i2] = arr[i2], arr[i1]
            self.data = arr
        elif dist == "Ters Sıralı":
            step = max(1, (max_v - min_v) // max(1, size))
            self.data = list(range(min_v + size * step, min_v, -step))[:size]
        elif dist == "Tekrarlı Değerler":
            pool = [random.randint(min_v, min_v + 6) for _ in range(4)]
            self.data = [random.choice(pool) for _ in range(size)]
        else:  # Rastgele
            self.data = [random.randint(min_v, max_v) for _ in range(size)]

        self.metrics = {"comparisons": 0, "swaps": 0}
        self.elapsed_time = 0.0
        self._update_metrics_display()
        self.lbl_status.config(text="Durum: Yeni dizi oluşturuldu", fg="#48bb78")
        self.draw_data(self.data)

    def draw_data(self, data: List[int], color_array: Optional[List[str]] = None, **kwargs):
        """
        Thread-safe canvas rendering callback.
        Handles dynamic coordinate scaling, label drawing, pause holding, and cancellation checks.
        """
        if self.stop_requested:
            raise StopAlgorithmException("Kullanıcı tarafından durduruldu.")

        # Pause loop
        while self.is_paused:
            if self.stop_requested:
                raise StopAlgorithmException("Kullanıcı tarafından durduruldu.")
            time.sleep(0.05)

        self.canvas.delete("all")
        if not data:
            return

        c_width = self.canvas.winfo_width()
        c_height = self.canvas.winfo_height()
        if c_width <= 50 or c_height <= 50:
            c_width, c_height = 800, 450

        n = len(data)
        margin_x = 16
        margin_y_bottom = 20
        margin_y_top = 35

        usable_width = c_width - (2 * margin_x)
        usable_height = c_height - margin_y_top - margin_y_bottom

        bar_width = usable_width / n
        spacing = 2 if bar_width >= 8 else (1 if bar_width >= 4 else 0)

        min_val = min(data)
        max_val = max(data)
        val_range = max_val - min_val if max_val != min_val else 1

        if color_array is None or len(color_array) != n:
            color_array = ["#4299e1" for _ in range(n)]

        for i, val in enumerate(data):
            x0 = margin_x + i * bar_width + spacing
            x1 = margin_x + (i + 1) * bar_width
            if x1 <= x0:
                x1 = x0 + 1

            # Safe height normalization
            normalized_height = ((val - min_val) / val_range) * (usable_height - 15) + 10
            y0 = c_height - margin_y_bottom - normalized_height
            y1 = c_height - margin_y_bottom

            self.canvas.create_rectangle(
                x0, y0, x1, y1,
                fill=color_array[i],
                outline="#2d3748" if bar_width > 12 else "",
                width=1
            )

            # Draw value numbers above bars only if bar is wide enough
            if bar_width >= 24:
                font_size = 9 if bar_width >= 35 else 8
                self.canvas.create_text(
                    (x0 + x1) / 2,
                    y0 - 8,
                    text=str(val),
                    font=("Segoe UI", font_size, "bold"),
                    fill="#e2e8f0"
                )

        # Update metrics in UI
        if self.is_running:
            self.elapsed_time = time.time() - self.start_time
        self._update_metrics_display()

        self.root.update_idletasks()

    def _update_metrics_display(self):
        self.lbl_comparisons.config(text=f"Karşılaştırma: {self.metrics.get('comparisons', 0):,}")
        self.lbl_swaps.config(text=f"Yer Değiştirme / Yazma: {self.metrics.get('swaps', 0):,}")
        self.lbl_timer.config(text=f"Süre: {self.elapsed_time:.2f} sn")

    def start_algorithm(self):
        """Starts algorithm sorting on a background thread."""
        if self.is_running:
            return

        algo_name = self.algo_var.get()
        algo_func = ALGORITHMS_DICT.get(algo_name)
        if not algo_func:
            messagebox.showerror("Hata", f"Seçilen algoritma bulunamadı: {algo_name}")
            return

        if not self.data:
            self.generate_dataset()

        self.is_running = True
        self.is_paused = False
        self.stop_requested = False
        self.metrics = {"comparisons": 0, "swaps": 0}
        self.start_time = time.time()

        # Update UI control states
        self.btn_start.config(state=tk.DISABLED)
        self.btn_generate.config(state=tk.DISABLED)
        self.btn_pause.config(state=tk.NORMAL, text="⏸ Duraklat")
        self.btn_stop.config(state=tk.NORMAL)
        self.algo_menu.config(state=tk.DISABLED)
        self.distribution_menu.config(state=tk.DISABLED)
        self.lbl_status.config(text=f"Durum: {algo_name} çalışıyor...", fg="#ecc94b")

        def run_thread():
            try:
                speed = float(self.speed_scale.get())
                algo_func(self.data, self.draw_data, speed, metrics_tracker=self.metrics)
                if not self.stop_requested:
                    self.lbl_status.config(text=f"Durum: {algo_name} tamamlandı! ✓", fg="#48bb78")
            except StopAlgorithmException:
                self.lbl_status.config(text="Durum: İşlem durduruldu ve sıfırlandı.", fg="#f56565")
            except Exception as e:
                self.lbl_status.config(text=f"Hata: {str(e)}", fg="#f56565")
            finally:
                self.is_running = False
                self.is_paused = False
                self.stop_requested = False
                self.btn_start.config(state=tk.NORMAL)
                self.btn_generate.config(state=tk.NORMAL)
                self.btn_pause.config(state=tk.DISABLED, text="⏸ Duraklat")
                self.btn_stop.config(state=tk.DISABLED)
                self.algo_menu.config(state="readonly")
                self.distribution_menu.config(state="readonly")
                self._update_metrics_display()

        self.worker_thread = threading.Thread(target=run_thread, daemon=True)
        self.worker_thread.start()

    def toggle_pause(self):
        if not self.is_running:
            return
        self.is_paused = not self.is_paused
        if self.is_paused:
            self.btn_pause.config(text="▶ Devam Et", bg="#3182ce")
            self.lbl_status.config(text="Durum: Duraklatıldı", fg="#ecc94b")
        else:
            self.btn_pause.config(text="⏸ Duraklat", bg="#d69e2e")
            self.lbl_status.config(text="Durum: Çalışmaya devam ediyor...", fg="#ecc94b")

    def stop_algorithm(self):
        if self.is_running:
            self.stop_requested = True
            self.is_paused = False
            self.lbl_status.config(text="Durum: Durduruluyor...", fg="#f56565")
            self.root.after(100, self.generate_dataset)

    def open_complexity_graph(self):
        show_complexity_window(
            current_n=len(self.data),
            selected_algo=self.algo_var.get(),
            parent=self.root
        )

    def _on_close(self):
        self.stop_requested = True
        self.is_paused = False
        self.root.destroy()


# Standalone entry point & backwards-compatible functions
_app_instance: Optional[SortingVisualizerApp] = None


def drowData(data, colorArray):
    """Backwards compatibility function for older code references."""
    if _app_instance:
        _app_instance.draw_data(data, colorArray)


def startAlgorithm():
    """Backwards compatibility function for older code references."""
    if _app_instance:
        _app_instance.start_algorithm()


def Generate():
    """Backwards compatibility function for older code references."""
    if _app_instance:
        _app_instance.generate_dataset()


def main():
    global _app_instance
    root = tk.Tk()
    _app_instance = SortingVisualizerApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
