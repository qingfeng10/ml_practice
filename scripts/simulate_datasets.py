from sklearn import datasets
import numpy

if __name__ == "__main__":
    X, y = datasets.make_classification(
        n_samples=1000,
        n_features=5,
        n_informative=2
    )

    with open('~/Work/Career/ml_practice/data/target.txt', 'w') as f:
        f.write("\n".join(map(str, y)))
