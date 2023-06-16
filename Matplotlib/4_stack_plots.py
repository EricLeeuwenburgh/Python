# Youtube: https://www.youtube.com/watch?v=xN-Supd4H38&list=PLICW5UpCwEj0GIC7WLVHf3SnZKmAchsUy&index=4

from matplotlib import pyplot as plt

## Stack plot - Best used to track values (over time) and a certain total

plt.style.use("fivethirtyeight")


minutes = [1, 2, 3, 4, 5, 6, 7, 8, 9]

player1 = [8, 6, 5, 5, 4, 2, 1, 1, 0]       # Data = example of hourly distribution of three people one a single project
player2 = [0, 1, 2, 2, 2, 4, 4, 4, 4]
player3 = [0, 1, 1, 1, 2, 2, 3, 3, 4]

labels = ["player1", "player2", "player3"]
colors = ["#6d904f", "#fc4f30", "#008fd5"]

plt.stackplot(minutes, player1, player2, player3, labels=labels, colors=colors)

plt.legend(loc=(0.07, 0.05))

plt.title("My Awesome Stack Plot")
plt.tight_layout()
plt.show()

# Colors:
# Blue = #008fd5
# Red = #fc4f30
# Yellow = #e5ae37
# Green = #6d904f