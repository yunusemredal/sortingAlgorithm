"""
Complexity and Performance Graph Visualizer
Provides theoretical Big-O complexity comparison and performance visualization
for sorting algorithms.
"""
import math
import tkinter as tk
from tkinter import ttk
from typing import Optional


def show_complexity_window(current_n: int = 30, selected_algo: str = "Bubble Sort", parent: Optional[tk.Tk] = None) -> None:
    """
    Opens an informative top-level window showing the asymptotic time complexity curves
    O(n), O(n log n), and O(n^2), highlighting the current dataset size (n).
    """
    win = tk.Toplevel(parent) if parent else tk.Tk()
    win.title(f"Algoritma Karmaşıklık Analizi - {selected_algo} (n = {current_n})")
    win.geometry("820x620")
    win.configure(bg="#1a202c")
    win.minsize(700, 500)

    # Header
    header_frame = tk.Frame(win, bg="#2d3748", pady=10)
    header_frame.pack(fill=tk.X)

    title_label = tk.Label(
        header_frame,
        text="Sıralama Algoritmaları Asimptotik Zaman Karmaşıklığı (Big-O)",
        font=("Segoe UI", 14, "bold"),
        fg="#f7fafc",
        bg="#2d3748"
    )
    title_label.pack()

    subtitle_label = tk.Label(
        header_frame,
        text=f"Mevcut Dizi Boyutu: n = {current_n} | Seçili Algoritma: {selected_algo}",
        font=("Segoe UI", 10),
        fg="#cbd5e0",
        bg="#2d3748"
    )
    subtitle_label.pack(pady=2)

    # Canvas for plotting
    canvas_width = 760
    canvas_height = 420
    canvas = tk.Canvas(win, width=canvas_width, height=canvas_height, bg="#171923", highlightthickness=0)
    canvas.pack(pady=15, padx=20, fill=tk.BOTH, expand=True)

    # Legend / Info Footer
    footer = tk.Frame(win, bg="#2d3748", pady=8, padx=15)
    footer.pack(fill=tk.X, side=tk.BOTTOM)

    legend_items = [
        ("O(n) - Doğrusal (En İyi / Saymalı)", "#48bb78"),
        ("O(n log n) - Doğrusal Logaritmik (Merge, Quick, Heap)", "#4299e1"),
        ("O(n²) - Karesel (Bubble, Selection, Insertion)", "#f56565"),
        (f"Mevcut n ({current_n})", "#ecc94b"),
    ]

    for label_text, color in legend_items:
        item_frame = tk.Frame(footer, bg="#2d3748")
        item_frame.pack(side=tk.LEFT, padx=12)
        color_box = tk.Label(item_frame, bg=color, width=2, height=1)
        color_box.pack(side=tk.LEFT, padx=4)
        lbl = tk.Label(item_frame, text=label_text, font=("Segoe UI", 9), fg="#e2e8f0", bg="#2d3748")
        lbl.pack(side=tk.LEFT)

    def draw_chart(event=None):
        canvas.delete("all")
        w = canvas.winfo_width()
        h = canvas.winfo_height()
        if w < 100 or h < 100:
            w, h = canvas_width, canvas_height

        margin_left = 60
        margin_bottom = 50
        margin_top = 30
        margin_right = 30

        plot_w = w - margin_left - margin_right
        plot_h = h - margin_top - margin_bottom

        # Grid lines and Axes
        canvas.create_line(margin_left, margin_top + plot_h, margin_left + plot_w, margin_top + plot_h, fill="#718096", width=2)
        canvas.create_line(margin_left, margin_top, margin_left, margin_top + plot_h, fill="#718096", width=2)

        # X Axis labels (n: 1 to 100)
        max_n = 100
        max_y = 10000  # 100^2

        for tick_n in [10, 25, 50, 75, 100]:
            x_pos = margin_left + (tick_n / max_n) * plot_w
            canvas.create_line(x_pos, margin_top + plot_h, x_pos, margin_top + plot_h + 5, fill="#a0aec0")
            canvas.create_text(x_pos, margin_top + plot_h + 15, text=str(tick_n), fill="#a0aec0", font=("Segoe UI", 8))
            canvas.create_line(x_pos, margin_top, x_pos, margin_top + plot_h, fill="#2d3748", dash=(2, 4))

        canvas.create_text(margin_left + plot_w / 2, margin_top + plot_h + 35, text="Eleman Sayısı (n)", fill="#e2e8f0", font=("Segoe UI", 10, "bold"))

        # Y Axis labels (Operations: 0 to 10000)
        for tick_y in [2000, 4000, 6000, 8000, 10000]:
            y_pos = margin_top + plot_h - (tick_y / max_y) * plot_h
            canvas.create_line(margin_left - 5, y_pos, margin_left, y_pos, fill="#a0aec0")
            canvas.create_text(margin_left - 25, y_pos, text=str(tick_y), fill="#a0aec0", font=("Segoe UI", 8))
            canvas.create_line(margin_left, y_pos, margin_left + plot_w, y_pos, fill="#2d3748", dash=(2, 4))

        canvas.create_text(20, margin_top + plot_h / 2, text="İşlem\nSayısı", fill="#e2e8f0", font=("Segoe UI", 9, "bold"))

        # Plot curves
        steps = 100
        pts_n2 = []
        pts_nlogn = []
        pts_n = []

        for step in range(1, steps + 1):
            n_val = (step / steps) * max_n
            x_pixel = margin_left + (n_val / max_n) * plot_w

            # O(n^2)
            y_n2 = n_val ** 2
            y_pix_n2 = margin_top + plot_h - (y_n2 / max_y) * plot_h
            pts_n2.extend([x_pixel, max(margin_top, y_pix_n2)])

            # O(n log n) - scaled for visibility (multiply factor ~15 for relative curve visibility)
            y_nlogn = n_val * math.log2(max(n_val, 1)) * 15
            y_pix_nlogn = margin_top + plot_h - (y_nlogn / max_y) * plot_h
            pts_nlogn.extend([x_pixel, max(margin_top, y_pix_nlogn)])

            # O(n) - scaled (factor ~25)
            y_linear = n_val * 25
            y_pix_n = margin_top + plot_h - (y_linear / max_y) * plot_h
            pts_n.extend([x_pixel, max(margin_top, y_pix_n)])

        canvas.create_line(pts_n2, fill="#f56565", width=3, smooth=True)
        canvas.create_line(pts_nlogn, fill="#4299e1", width=3, smooth=True)
        canvas.create_line(pts_n, fill="#48bb78", width=3, smooth=True)

        # Plot current n vertical line
        cur_x = margin_left + (min(current_n, max_n) / max_n) * plot_w
        canvas.create_line(cur_x, margin_top, cur_x, margin_top + plot_h, fill="#ecc94b", width=2, dash=(4, 3))
        canvas.create_text(cur_x, margin_top - 12, text=f"n={current_n}", fill="#ecc94b", font=("Segoe UI", 9, "bold"))

    canvas.bind("<Configure>", draw_chart)
    win.after(100, draw_chart)


def drawRootGraph(current_n: int = 30, selected_algo: str = "Bubble Sort", parent: Optional[tk.Tk] = None) -> None:
    """
    Backwards compatibility alias for show_complexity_window.
    Does NOT block or run automatically on import.
    """
    show_complexity_window(current_n=current_n, selected_algo=selected_algo, parent=parent)
