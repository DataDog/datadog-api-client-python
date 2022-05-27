# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class LogsAggregateResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.logs_aggregate_response_data import LogsAggregateResponseData
        from datadog_api_client.v2.model.logs_response_metadata import LogsResponseMetadata

        return {
            "data": (LogsAggregateResponseData,),
            "meta": (LogsResponseMetadata,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }

    def __init__(self, *args, **kwargs):
        """
        The response object for the logs aggregate API endpoint

        :param data: The query results
        :type data: LogsAggregateResponseData, optional

        :param meta: The metadata associated with a request
        :type meta: LogsResponseMetadata, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(LogsAggregateResponse, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
