# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class ListStreamColumn(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.list_stream_column_width import ListStreamColumnWidth

        return {
            "field": (str,),
            "width": (ListStreamColumnWidth,),
        }

    attribute_map = {
        "field": "field",
        "width": "width",
    }

    def __init__(self, field, width, *args, **kwargs):
        """
        Widget column.

        :param field: Widget column field.
        :type field: str

        :param width: Widget column width.
        :type width: ListStreamColumnWidth
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.field = field
        self.width = width

    @classmethod
    def _from_openapi_data(cls, field, width, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(ListStreamColumn, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.field = field
        self.width = width
        return self
