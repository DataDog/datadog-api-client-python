# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class AWSLogsAsyncResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.aws_logs_async_error import AWSLogsAsyncError

        return {
            "errors": ([AWSLogsAsyncError],),
            "status": (str,),
        }

    attribute_map = {
        "errors": "errors",
        "status": "status",
    }

    def __init__(self, *args, **kwargs):
        """
        A list of all Datadog-AWS logs integrations available in your Datadog organization.

        :param errors: List of errors.
        :type errors: [AWSLogsAsyncError], optional

        :param status: Status of the properties.
        :type status: str, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(AWSLogsAsyncResponse, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
