
import os
from PIL import Image
bad=[]
for root,_,files in os.walk("ui"):
    for f in files:
        if f.lower().endswith(".png"):
            p=os.path.join(root,f)
            with Image.open(p) as im:
                if "icc_profile" in im.info and im.info["icc_profile"]:
                    bad.append(p)
print("PNG dengan ICC:", bad or "Nihil")
