import psutil
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def get_memory_usage():
    memory_info = psutil.virtual_memory()
    return memory_info.percent

def update(frame):
    cpu_usage = get_cpu_usage()
    memory_usage = get_memory_usage()
    cpu_text.set_text(f"CPU Kullanımı: {cpu_usage}%")
    memory_text.set_text(f"Bellek Kullanımı: {memory_usage}%")
    cpu_bar[0].set_height(cpu_usage)
    memory_bar[0].set_height(memory_usage)

fig, ax = plt.subplots()
cpu_bar = ax.bar(0, 0, color='b', width=0.4)
memory_bar = ax.bar(0.5, 0, color='r', width=0.4)
cpu_text = ax.text(-0.2, 90, "", fontsize=12, color='b')
memory_text = ax.text(0.3, 90, "", fontsize=12, color='r')

ax.set_ylim(0, 100)
ax.set_xticks([])
ax.set_ylabel("Kullanım Yüzdesi")
ax.set_title("İşlemci ve Bellek Kullanımı")

ani = FuncAnimation(fig, update, frames=None, interval=500, repeat=True, cache_frame_data=False)
plt.show()
