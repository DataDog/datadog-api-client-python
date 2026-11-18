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
    from datadog_api_client.v2.model.segment_data_query import SegmentDataQuery


class SegmentUpdateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.segment_data_query import SegmentDataQuery

        return {
            "data_query": (SegmentDataQuery,),
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
        data_query: Union[SegmentDataQuery, UnsetType] = unset,
        description: Union[str, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        tags: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes to update on a segment. Fields that are not set are left unchanged.

        :param data_query: Defines who belongs to the segment. It contains one or more blocks, up to 20 in total.
            Use ``combination`` to combine named blocks with a boolean formula such as ``A AND NOT B``.
        :type data_query: SegmentDataQuery, optional

        :param description: Description of the segment.
        :type description: str, optional

        :param name: Name of the segment. It must be unique in the organization.
        :type name: str, optional

        :param tags: Tags of the segment. Replaces the stored tags.
        :type tags: [str], optional
        """
        if data_query is not unset:
            kwargs["data_query"] = data_query
        if description is not unset:
            kwargs["description"] = description
        if name is not unset:
            kwargs["name"] = name
        if tags is not unset:
            kwargs["tags"] = tags
        super().__init__(kwargs)
