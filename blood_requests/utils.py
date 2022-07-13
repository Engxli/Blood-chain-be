from typing import Annotated, Any, Union

from annotated_types import Ge
from graphene.types import Scalar
from graphql.language.ast import IntValue


MIN_INT = 1
MAX_INT = 2147483647

_PositiveIntFieldType = Annotated[int, Ge(1)]


class PositiveIntField(Scalar):
    """
    The `PositiveIntField` scalar type represents non-fractional signed whole numeric
    values. PositiveIntField can represent values between 0 and 2^53 - 1 since
    represented in JSON as double-precision floating point numbers specified
    by [IEEE 754](http://en.wikipedia.org/wiki/IEEE_floating_point).
    """

    @staticmethod
    def coerce_int(
        value: int,
    ) -> Union[_PositiveIntFieldType, None]:
        try:
            num = int(value)
        except ValueError:
            try:
                num = int(float(value))
            except ValueError:
                return None
        if MIN_INT <= num <= MAX_INT:
            return num

        return None

    serialize = coerce_int
    parse_value = coerce_int

    @staticmethod
    def parse_literal(ast: Any) -> Union[_PositiveIntFieldType, None]:
        if isinstance(ast, IntValue):
            num = int(ast.value)
            if MIN_INT <= num <= MAX_INT:
                return num

        return None
