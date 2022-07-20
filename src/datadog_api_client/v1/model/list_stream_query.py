# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class ListStreamQuery(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.list_stream_source import ListStreamSource

        return {
            "data_source": (ListStreamSource,),
            "indexes": ([str],),
            "query_string": (str,),
        }

    attribute_map = {
        "data_source": "data_source",
        "indexes": "indexes",
        "query_string": "query_string",
    }

    def __init__(self, data_source, query_string, *args, **kwargs):
        """
        Updated list stream widget.

        :param data_source: Source from which to query items to display in the stream.
        :type data_source: ListStreamSource

        :param indexes: List of indexes.
        :type indexes: [str], optional

        :param query_string: Widget query.
        :type query_string: str
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.data_source = data_source
        self.query_string = query_string

    @classmethod
    def _from_openapi_data(cls, data_source, query_string, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(ListStreamQuery, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.data_source = data_source
        self.query_string = query_string
        return self
