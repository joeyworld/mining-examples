import numpy as np
import matplotlib.pyplot as plt

score = {
    "henry": [100, 90, 80],
    "james": [90, 90, 70],
    "todd": [50, 40, 100]
}

henry = np.array(score['henry'])
james = np.array(score['james'])
todd = np.array(score['todd'])

align = np.arange(3)
plt.bar(align, henry, width=0.2, color='r', label='henry')
plt.bar(align+0.2, james, width=0.2, color='g', label='james')
plt.bar(align+0.4, todd, width=0.2, color='b', label='todd')

plt.xticks(align+0.2, ['mathematics', 'english', 'science'])
plt.legend()
plt.show()
