# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class LogsAPIErrorResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.logs_api_error import LogsAPIError

        return {
            "error": (LogsAPIError,),
        }

    attribute_map = {
        "error": "error",
    }

    def __init__(self, *args, **kwargs):
        """
        Response returned by the Logs API when errors occur.

        :param error: Error returned by the Logs API
        :type error: LogsAPIError, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(LogsAPIErrorResponse, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
