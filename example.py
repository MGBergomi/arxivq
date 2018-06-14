from arxivq.arxivq import ArxivQ
import matplotlib.pyplot as plt

if __name__ == "__main__":
    plt.ion()

    def func(x, a, b, c):
        return a * np.exp(-b * x)

    query_dlm = ArxivQ(search_query="deep learning AND music",
                       id_list=[],
                       prune=True,
                       start=0,
                       max_results=10000,
                       sort_by="submittedDate",
                       sort_order="descending")
    query_dlm.plot_histogram(bin_by = "Y", column = "published")
    query_dlm.fit(func)
