''''
copyright @prwl_nght



'''


import pandas as pd
import matplotlib.pyplot as plt
import cv2
import os, sys, inspect, platform

if platform.system().lower().__contains__('darwin'):
    import resources_mac as resources
elif platform.system().lower().__contains__('windows'):
    import resources_windows as resources
else:
    import resources_unix as resources


data_dir = os.path.join(resources.data_dir, 'figures_all_smoothing5', 'a0')

for file in os.listdir(data_dir):
    if file.startswith('.'):
        continue
    if file.__contains__('.jpeg'):
        m_img_file = file
        break
m_img_file = os.path.join(data_dir, m_img_file)

img = cv2.imread(m_img_file, cv2.IMREAD_COLOR)

# cv2.imshow('image', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

plt.imshow(img, cmap='gray', interpolation = 'bicubic')
plt.plot([500, 100], [80, 100], 'c', linewidth = 5)
plt.show()







