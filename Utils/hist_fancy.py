from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

#im=Image.open("./1_hist_eq.jpg")
im=Image.open("./B1_raw.jpg")
#im=Image.open("./B1_clahe_twice.jpg")

def is_grey_scale(img_path):
    img = Image.open(img_path).convert('RGB')
    w, h = img.size
    for i in range(w):
        for j in range(h):
            r, g, b = img.getpixel((i,j))
            if r != g != b: 
                return False
    return True
    
#print(is_grey_scale('./B1_clahe_twice.jpg'))  
print(is_grey_scale('./B1_raw.jpg'))    
 
a = np.array(im.getdata())

fig, ax = plt.subplots(figsize=(10,4))
#n,bins,patches = ax.hist(a, bins=range(256), edgecolor='none')
n,bins,patches = ax.hist(a[:,0], bins=range(256), edgecolor='none')
ax.set_title("histogram raw")
ax.set_xlim(0,255)



cm = plt.cm.get_cmap('gist_rainbow')  #was cool, then turbo the CMRmap, then ocean
norm = matplotlib.colors.Normalize(vmin=bins.min(), vmax=bins.max())
for b,p in zip(bins,patches):
    p.set_facecolor(cm(norm(b)))

plt.savefig('B1_raw_hist.jpg', transparent=True, bbox_inches='tight')
#plt.show()
