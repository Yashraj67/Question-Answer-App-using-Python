import numpy as np
import matplotlib.pyplot as plt
from personality import fp,fp2
from tkinter import *
plt.figure(figsize=(50,50))



X = ['Extrovert             Introvert','Intuitive             Sensing','Perceving             Judging','Feeling             Thinking']

Ygirls = fp
Zboys = fp2
X_axis = np.arange(len(X))

plt.bar(X_axis - 0.2 , Ygirls, 0.35)
plt.bar(X_axis + 0.2 , Zboys, 0.35)

plt.xticks(X_axis, X)
plt.xlabel("Types of Personalities")
plt.ylabel("percentage")
plt.title("Checkout Your Personality Traits")
plt.legend()
plt.show()

