class BookingError(Exception): 
    """Raised when train ID is invalid or no seat is available""" 
    def __init__(self, message="Booking failed"):
        super().__init__(message)

class PNRNotFoundError(Exception): 
    """Raised when PNR is invalid"""
    def __init__(self, message="PNR not found"):
        super().__init__(message)