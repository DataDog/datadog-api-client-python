# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (
    ModelNormal,
    cached_property,
)


class HTTPLogError(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    validations = {
        "code": {
            "inclusive_maximum": 2147483647,
        },
    }

    @cached_property
    def openapi_types():
        return {
            "code": (int,),
            "message": (str,),
        }

    attribute_map = {
        "code": "code",
        "message": "message",
    }

    read_only_vars = {}

    def __init__(self, code, message, *args, **kwargs):
        """HTTPLogError - a model defined in OpenAPI

        Args:
            code (int): Error code.
            message (str): Error message.

        Keyword Args:
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.code = code
        self.message = message

    @classmethod
    def _from_openapi_data(cls, code, message, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(HTTPLogError, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.code = code
        self.message = message
        return self
