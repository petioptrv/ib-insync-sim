from ib_sim.wrapper cimport Wrapper


cdef class Client:
    cdef Wrapper wrapper
    cdef char *host
    cdef int port
    cdef int clientId
    cdef int conState
    cdef object _logger

    cpdef void reset(self)
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
