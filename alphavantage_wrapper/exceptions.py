class APIError(Exception):
    """Raised when the API request fails."""
    pass

class RateLimitError(APIError):
    """Raised when the API rate limit is hit."""
    pass

class ResponseError(APIError):
    """Raised when the API response is not in the expected format."""
    pass