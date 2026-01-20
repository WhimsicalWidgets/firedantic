from typing import Annotated, Any, Dict, Literal, NamedTuple, Optional, Tuple, Union

from google.cloud.firestore_v1.vector import Vector
from pydantic import BeforeValidator

OrderDirection = Union[Literal["ASCENDING"], Literal["DESCENDING"]]

FiredanticVector = Annotated[
    Vector,
    BeforeValidator(lambda v: v if isinstance(v, Vector) else Vector(v)),
]


class VectorConfig(NamedTuple):
    dimension: int
    flat: bool = True


class IndexField(NamedTuple):
    name: str
    order: Optional[OrderDirection] = None
    vector_config: Optional[VectorConfig] = None


IndexDefinition = NamedTuple(
    "IndexDefinition", [("query_scope", str), ("fields", Tuple[IndexField, ...])]
)


def collection_index(*fields: IndexField) -> IndexDefinition:
    """
    Shorter way to create an index definition with collection query scope

    :param fields: Index fields, each element is a tuple of name and order
    :return: IndexDefinition tuple
    """
    return IndexDefinition(query_scope="COLLECTION", fields=fields)


def collection_group_index(*fields: IndexField) -> IndexDefinition:
    """
    Shorter way to create an index definition with collection group query scope

    :param fields: Index fields, each element is a tuple of name and order
    :return: IndexDefinition tuple
    """
    return IndexDefinition(query_scope="COLLECTION_GROUP", fields=fields)
