# ArxivQ

Uses https://github.com/lukasschwab/arxiv.py to perform a query on ArXiv. The output is organized as a Pandas dataframe. By reindexing the dataframe according to 
date-like columns as `published` or `updated` it is possible to compute histograms showing the amount of papers published per year or month-year. Finally,
scipy is used to fit a curve to the histogram data.


### Installation and examples

Clone the repository, cd in the repository folder and type 

```
pip install -e .
```

A query, the histogram and fit are performed by running the following code

```
from arxivq.arxivq import ArxivQ
import matplotlib.pyplot as plt

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
```

## Acknowledgments

* See https://github.com/lukasschwab/arxiv.py for the code to call the ArXiv API