# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class LogsListResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.log import Log

        return {
            "logs": ([Log],),
            "next_log_id": (str,),
            "status": (str,),
        }

    attribute_map = {
        "logs": "logs",
        "next_log_id": "nextLogId",
        "status": "status",
    }

    def __init__(self, *args, **kwargs):
        """
        Response object with all logs matching the request and pagination information.

        :param logs: Array of logs matching the request and the ``nextLogId`` if sent.
        :type logs: [Log], optional

        :param next_log_id: Hash identifier of the next log to return in the list.
            This parameter is used for the pagination feature.
        :type next_log_id: str, optional

        :param status: Status of the response.
        :type status: str, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(LogsListResponse, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
