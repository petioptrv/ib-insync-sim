import logging

cdef class Wrapper:
    def __init__(self, ib):
        self.ib = ib
        self._logger = logging.getLogger('ib_sim.wrapper')
