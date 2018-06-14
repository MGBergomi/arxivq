import arxivq.arxiv as ar
import platform
from collections import Counter
import numpy as np
import pandas as pd
from datetime import datetime
if platform.system() == "Darwin":
    import matplotlib
    matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.optimize as so
sns.set()

class ArxivQ:
    def __init__(self, search_query="", id_list=[], prune=True, start=0,
                 max_results=10, sort_by="", sort_order=""):
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.search_query = search_query
        self.id_list = id_list
        self.prune = prune
        self.start = start
        self.max_results = max_results
        self.sort_by = sort_by
        self.sort_order = sort_order
        self.arrange_as_dataframe(ar.query(search_query=self.search_query,
                             id_list=self.id_list,
                             prune=self.prune,
                             start=self.start,
                             max_results=self.max_results,
                             sort_by=self.sort_by,
                             sort_order=self.sort_order))

    def arrange_as_dataframe(self, query):
        self.data = pd.DataFrame(query)
        self.data.published = self.data.published.astype('datetime64')
        self.data.updated = self.data.updated.astype('datetime64')

    def reindex(self, column):
        name = column + "_date"
        self.data[name] = self.data[column].apply( lambda df :
        datetime(year=df.year, month=df.month, day=df.day))
        self.data.set_index(self.data[name],inplace=True)

    def plot_histogram(self, column = "published", bin_by = None,
                       fig = None, ax = None):
        self.reindex(column)
        if ax is None or fig is None:
            self.fig, self.ax = plt.subplots()
        if bin_by is None or bin_by == "Y":
            bin_by = "Y"
            cut_ind = 4
        elif bin_by == "M":
            cut_ind = 8
        else:
            raise NotImplementedError("Cannot bin by {}".format(bin_by))
        self.counted = self.data[column].resample(bin_by).count()
        self.counted.plot(kind="bar", ax = self.ax)
        xtl=[item.get_text()[:cut_ind] for item in self.ax.get_xticklabels()]
        _=self.ax.set_xticklabels(xtl)

        self.fig.autofmt_xdate()
        plt.show()

    def fit(self, func, nstd = 5):
        popt, pcov = so.curve_fit(func ,range(len(self.counted[:-1])), self.counted[:-1])
        xx = np.linspace(0, len(self.counted[:-1]),len(self.counted[:-1]))
        yy = func(xx, *popt)
        perr = np.sqrt(np.diag(pcov))
        popt_up = popt + nstd * perr
        popt_dw = popt - nstd * perr
        yy_up = func(xx, *popt_up)
        yy_dw = func(xx, *popt_dw)
        self.ax.plot(xx,yy, label = "fit")
        self.ax.fill_between(xx, yy_up, yy_dw, alpha=.25,
                             label="5-sigma interval")

    def save(self, path):
        np.save(path, self)

    @staticmethod
    def load(path):
        return np.load(path)
