# force_strip_icc.py
import os
from PIL import Image
from PIL.PngImagePlugin import PngInfo

p = r"ui/logo.png"     # kalau perlu, loop semua PNG kamu

# 1) buka dan konversi (biar lepas dari profile lama)
im = Image.open(p).convert("RGBA")

# 2) bikin metadata kosong (tanpa icc_profile)
meta = PngInfo()  # tidak menambahkan apapun

# 3) simpan ulang TANPA icc_profile
im.save(p, pnginfo=meta, icc_profile=None, optimize=True)
print("STRIPPED:", p)
