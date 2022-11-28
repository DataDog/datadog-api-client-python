# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v1.model.list_stream_source import ListStreamSource


class ListStreamQuery(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.list_stream_source import ListStreamSource

        return {
            "data_source": (ListStreamSource,),
            "indexes": ([str],),
            "query_string": (str,),
            "storage": (str,),
        }

    attribute_map = {
        "data_source": "data_source",
        "indexes": "indexes",
        "query_string": "query_string",
        "storage": "storage",
    }

    def __init__(
        self_,
        data_source: ListStreamSource,
        query_string: str,
        indexes: Union[List[str], UnsetType] = unset,
        storage: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Updated list stream widget.

        :param data_source: Source from which to query items to display in the stream.
        :type data_source: ListStreamSource

        :param indexes: List of indexes.
        :type indexes: [str], optional

        :param query_string: Widget query.
        :type query_string: str

        :param storage: Option for storage location. Feature in Private Beta.
        :type storage: str, optional
        """
        if indexes is not unset:
            kwargs["indexes"] = indexes
        if storage is not unset:
            kwargs["storage"] = storage
        super().__init__(kwargs)

        self_.data_source = data_source
        self_.query_string = query_string
