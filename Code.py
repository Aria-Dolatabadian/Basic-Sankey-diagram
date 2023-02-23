import pandas as pd
import matplotlib.pyplot as plt
from pySankey.sankey import sankey
url = "https://raw.githubusercontent.com/Aria-Dolatabadian/Basic-Sankey-diagram/main/fruits.txt"
df = pd.read_csv(url, sep=" ", names=["true", "predicted"])

colors = {
    "apple": "#f71b1b",
    "blueberry": "#1b7ef7",
    "banana": "#f3f71b",
    "lime": "#12e23f",
    "orange": "#f78c1b"
}

sankey(df["true"], df["predicted"], aspect=20, colorDict=colors, fontsize=12)

plt.show()
