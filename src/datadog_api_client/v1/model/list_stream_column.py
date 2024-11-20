# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v1.model.list_stream_column_width import ListStreamColumnWidth


class ListStreamColumn(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.list_stream_column_width import ListStreamColumnWidth

        return {
            "field": (str,),
            "is_clustering_pattern_field_path": (bool,),
            "width": (ListStreamColumnWidth,),
        }

    attribute_map = {
        "field": "field",
        "is_clustering_pattern_field_path": "is_clustering_pattern_field_path",
        "width": "width",
    }

    def __init__(
        self_,
        field: str,
        width: ListStreamColumnWidth,
        is_clustering_pattern_field_path: Union[bool, UnsetType] = unset,
        **kwargs,
    ):
        """
        Widget column.

        :param field: Widget column field.
        :type field: str

        :param is_clustering_pattern_field_path: Identifies the clustering pattern field column, usable only with logs_pattern_stream.
        :type is_clustering_pattern_field_path: bool, optional

        :param width: Widget column width.
        :type width: ListStreamColumnWidth
        """
        if is_clustering_pattern_field_path is not unset:
            kwargs["is_clustering_pattern_field_path"] = is_clustering_pattern_field_path
        super().__init__(kwargs)

        self_.field = field
        self_.width = width
