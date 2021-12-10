# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v2.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    date,
    datetime,
    file_type,
    none_type,
)


class FullApplicationKeyAttributes(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    validations = {
        "last4": {
            "max_length": 4,
            "min_length": 4,
        },
    }

    @cached_property
    def openapi_types():
        return {
            "created_at": (str,),
            "key": (str,),
            "last4": (str,),
            "name": (str,),
        }

    attribute_map = {
        "created_at": "created_at",
        "key": "key",
        "last4": "last4",
        "name": "name",
    }

    read_only_vars = {
        "created_at",
        "key",
        "last4",
    }

    def __init__(self, *args, **kwargs):
        """FullApplicationKeyAttributes - a model defined in OpenAPI

        Keyword Args:
            created_at (str): [optional] Creation date of the application key.
            key (str): [optional] The application key.
            last4 (str): [optional] The last four characters of the application key.
            name (str): [optional] Name of the application key.
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(FullApplicationKeyAttributes, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
