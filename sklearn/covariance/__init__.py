"""
The :mod:`sklearn.covariance` module includes methods and algorithms to
robustly estimate the covariance of features given a set of points. The
precision matrix defined as the inverse of the covariance is also estimated.
Covariance estimation is closely related to the theory of Gaussian Graphical
Models.
"""

from .empirical_covariance_ import empirical_covariance, EmpiricalCovariance, \
    log_likelihood
from .shrunk_covariance_ import shrunk_covariance, ShrunkCovariance, \
    ledoit_wolf, LedoitWolf, oas, OAS
from .robust_covariance import fast_mcd, MinCovDet
from .graph_lasso_ import graph_lasso, GraphLasso, GraphLassoCV
from .outlier_detection import EllipticEnvelop