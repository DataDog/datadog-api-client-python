# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class ListStreamWidgetRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.list_stream_column import ListStreamColumn
        from datadog_api_client.v1.model.list_stream_query import ListStreamQuery
        from datadog_api_client.v1.model.list_stream_response_format import ListStreamResponseFormat

        return {
            "columns": ([ListStreamColumn],),
            "query": (ListStreamQuery,),
            "response_format": (ListStreamResponseFormat,),
        }

    attribute_map = {
        "columns": "columns",
        "query": "query",
        "response_format": "response_format",
    }

    def __init__(self, columns, query, response_format, *args, **kwargs):
        """
        Updated list stream widget.

        :param columns: Widget columns.
        :type columns: [ListStreamColumn]

        :param query: Updated list stream widget.
        :type query: ListStreamQuery

        :param response_format: Widget response format.
        :type response_format: ListStreamResponseFormat
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.columns = columns
        self.query = query
        self.response_format = response_format

    @classmethod
    def _from_openapi_data(cls, columns, query, response_format, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(ListStreamWidgetRequest, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.columns = columns
        self.query = query
        self.response_format = response_format
        return self
