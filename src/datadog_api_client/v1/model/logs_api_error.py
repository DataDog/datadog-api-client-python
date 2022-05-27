# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class LogsAPIError(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.logs_api_error import LogsAPIError

        return {
            "code": (str,),
            "details": ([LogsAPIError],),
            "message": (str,),
        }

    attribute_map = {
        "code": "code",
        "details": "details",
        "message": "message",
    }

    def __init__(self, *args, **kwargs):
        """
        Error returned by the Logs API

        :param code: Code identifying the error
        :type code: str, optional

        :param details: Additional error details
        :type details: [LogsAPIError], optional

        :param message: Error message
        :type message: str, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(LogsAPIError, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
