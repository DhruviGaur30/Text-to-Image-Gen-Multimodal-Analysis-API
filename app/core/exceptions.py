class ModelLoadError(Exception):
    """Raised when a model fails to load."""
    pass


class InferenceError(Exception):
    """Raised when model inference fails."""
    pass


class FileSaveError(Exception):
    """Raised when saving an image fails."""
    pass
