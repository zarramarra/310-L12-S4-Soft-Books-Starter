import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

with open("books.csv", "r") as datafile:
    data = pd.read_csv(datafile, delimiter=",")

# BUBBLEPLOT: books rating Vs. page nubers
# rating_and_pages = data.loc[:, ["average_rating", "# num_pages"]]
# fig = sns.scatterplot(
#     x="# num_pages",
#     y="average_rating",
#     hue="average_rating",
#     size="average_rating",
#     data=rating_and_pages)
# plt.title("Books rating Vs page numbers")
# plt.xlabel("Book page number")
# plt.ylabel("Book average rating")
# fig.set_facecolor("#E5E5E5")
# plt.savefig("rating_and_pages.png")

# BUBBLEPLOT: books rating Vs. number of reviews
rating_and_pages = data.loc[:, ["average_rating", "text_reviews_count"]]
fig = sns.scatterplot(
    x="text_reviews_count",
    y="average_rating",
    hue="average_rating",
    size="average_rating",
    data=rating_and_pages)
plt.title("Books rating Vs review numbers")
plt.xlabel("Book review number")
plt.ylabel("Book average rating")
fig.set_facecolor("#E5E5E5")
plt.savefig("rating_and_reviews.png")
