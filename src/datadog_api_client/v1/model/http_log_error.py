# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class HTTPLogError(ModelNormal):
    validations = {
        "code": {
            "inclusive_maximum": 2147483647,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "code": (int,),
            "message": (str,),
        }

    attribute_map = {
        "code": "code",
        "message": "message",
    }

    def __init__(self, code, message, *args, **kwargs):
        """
        Invalid query performed.

        :param code: Error code.
        :type code: int

        :param message: Error message.
        :type message: str
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
