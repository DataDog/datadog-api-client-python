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
    from datadog_api_client.v2.model.rum_segment_data_query import RumSegmentDataQuery


class RumSegmentCreateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_segment_data_query import RumSegmentDataQuery

        return {
            "data_query": (RumSegmentDataQuery,),
            "description": (str,),
            "name": (str,),
            "tags": ([str],),
        }

    attribute_map = {
        "data_query": "data_query",
        "description": "description",
        "name": "name",
        "tags": "tags",
    }

    def __init__(
        self_,
        data_query: RumSegmentDataQuery,
        name: str,
        description: Union[str, UnsetType] = unset,
        tags: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for creating a new segment.

        :param data_query: Query definition for the segment. Contains one or more query blocks and an optional combination formula.
        :type data_query: RumSegmentDataQuery

        :param description: A description of the segment.
        :type description: str, optional

        :param name: The name of the segment.
        :type name: str

        :param tags: A list of tags for the segment.
        :type tags: [str], optional
        """
        if description is not unset:
            kwargs["description"] = description
        if tags is not unset:
            kwargs["tags"] = tags
        super().__init__(kwargs)

        self_.data_query = data_query
        self_.name = name
