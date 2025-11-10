
from PIL import Image
p = r"ui/logo.png"
im = Image.open(p).convert("RGBA")
im.save(p)  # simpan ulang tanpa ICC/metadata
print("OK:", p)


