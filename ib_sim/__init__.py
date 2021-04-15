from ib_sim.ib import IB

__all__ = ["IB"]

from ._version import get_versions

__version__ = get_versions()["version"]
del get_versions
