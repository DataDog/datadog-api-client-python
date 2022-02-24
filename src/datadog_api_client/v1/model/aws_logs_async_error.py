# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (
    ModelNormal,
    cached_property,
)


class AWSLogsAsyncError(ModelNormal):

    validations = {}

    @cached_property
    def openapi_types():
        return {
            "code": (str,),
            "message": (str,),
        }

    attribute_map = {
        "code": "code",
        "message": "message",
    }

    read_only_vars = {}

    def __init__(self, *args, **kwargs):
        """
        Description of errors.

        :param code: Code properties
        :type code: str, optional

        :param message: Message content.
        :type message: str, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(AWSLogsAsyncError, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
