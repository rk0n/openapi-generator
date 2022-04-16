# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""

import re  # noqa: F401
import sys  # noqa: F401
import typing  # noqa: F401

from frozendict import frozendict  # noqa: F401

import decimal  # noqa: F401
from datetime import date, datetime  # noqa: F401
from frozendict import frozendict  # noqa: F401

from petstore_api.schemas import (  # noqa: F401
    AnyTypeSchema,
    ComposedSchema,
    DictSchema,
    ListSchema,
    StrSchema,
    IntSchema,
    Int32Schema,
    Int64Schema,
    Float32Schema,
    Float64Schema,
    NumberSchema,
    UUIDSchema,
    DateSchema,
    DateTimeSchema,
    DecimalSchema,
    BoolSchema,
    BinarySchema,
    NoneSchema,
    none_type,
    Configuration,
    Unset,
    unset,
    ComposedBase,
    ListBase,
    DictBase,
    NoneBase,
    StrBase,
    IntBase,
    Int32Base,
    Int64Base,
    Float32Base,
    Float64Base,
    NumberBase,
    UUIDBase,
    DateBase,
    DateTimeBase,
    BoolBase,
    BinaryBase,
    Schema,
    _SchemaValidator,
    _SchemaTypeChecker,
    _SchemaEnumMaker
)


class ObjectModelWithRefProps(
    DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    a model that includes properties which should stay primitive (String + Boolean) and one which is defined as a class, NumberWithValidations
    """

    @classmethod
    @property
    def myNumber(cls) -> typing.Type['NumberWithValidations']:
        return NumberWithValidations
    myString = StrSchema
    myBoolean = BoolSchema


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict, ],
        myNumber: typing.Union['NumberWithValidations', Unset] = unset,
        myString: typing.Union[myString, Unset] = unset,
        myBoolean: typing.Union[myBoolean, Unset] = unset,
        _configuration: typing.Optional[Configuration] = None,
        **kwargs: typing.Type[Schema],
    ) -> 'ObjectModelWithRefProps':
        return super().__new__(
            cls,
            *args,
            myNumber=myNumber,
            myString=myString,
            myBoolean=myBoolean,
            _configuration=_configuration,
            **kwargs,
        )

from petstore_api.model.number_with_validations import NumberWithValidations
