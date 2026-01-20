class ModelError(Exception):
    """Generic model error class."""


class InvalidDocumentID(ModelError):
    """Raised when a document ID is invalid."""


class ModelNotFoundError(ModelError):
    """Raised when a model is not found."""


class CollectionNotDefined(ModelError):
    """Raised when the model collection is not defined."""


class VectorFieldNotDefined(ModelError):
    """Raised when a vector field is not defined in the model."""


class VectorFieldAmbiguous(ModelError):
    """Raised when there are multiple vector fields and none is specified."""
