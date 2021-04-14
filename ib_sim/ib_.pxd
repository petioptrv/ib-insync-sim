cdef class IB:
    cdef public:
        float value
    cpdef connect(
        self,
        str host = *,
        int port = *,
        int clientId = *,
        float timeout = *,
        bint readonly = *,
        str account = *,
    )