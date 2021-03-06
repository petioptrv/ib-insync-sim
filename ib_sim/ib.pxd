from ib_sim.client cimport Client
from ib_sim.wrapper cimport Wrapper

cdef class IB:
    cdef Wrapper wrapper
    cdef Client client
    cdef object _logger

    cpdef void connect(
        self,
        char *host = *,
        int port = *,
        int clientId = *,
        float timeout = *,
        bint readonly = *,
        char *account = *,
    )
    cpdef void disconnect(self)
    cpdef bint isConnected(self)