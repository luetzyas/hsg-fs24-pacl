# not topic found in API
class NotFound(Exception):
    """Custom exception for handling not found errors."""
    pass

# invalid input option
# 1: You want to analyse movie scripts?
# 2: You want to analyse lyrics?
# 3: You want to analyse peotries?
class InvalidOption(Exception):
    """Custom exception for handling not found errors."""
    pass