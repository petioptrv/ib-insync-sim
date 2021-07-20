from ib_sim.ib cimport IB

cdef class Wrapper:
    cdef IB ib
    cdef object _logger