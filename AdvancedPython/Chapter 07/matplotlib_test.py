import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "x":range(1,11), # 1 to 10
    "y":[11,12,6,5,15,6,7,8,9,10]
})

df.plot(x = 'x', y='y', kind="area")
plt.show()