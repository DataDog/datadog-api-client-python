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
    from datadog_api_client.v2.model.rum_static_segment_journey_query_object import RumStaticSegmentJourneyQueryObject


class RumStaticSegmentCreateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_static_segment_journey_query_object import (
            RumStaticSegmentJourneyQueryObject,
        )

        return {
            "description": (str,),
            "journey_query_object": (RumStaticSegmentJourneyQueryObject,),
            "name": (str,),
            "tags": ([str],),
        }

    attribute_map = {
        "description": "description",
        "journey_query_object": "journey_query_object",
        "name": "name",
        "tags": "tags",
    }

    def __init__(
        self_,
        description: str,
        journey_query_object: RumStaticSegmentJourneyQueryObject,
        name: str,
        tags: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for creating a new static segment.

        :param description: A description of the static segment.
        :type description: str

        :param journey_query_object: The journey query object used to compute the static segment user list.
        :type journey_query_object: RumStaticSegmentJourneyQueryObject

        :param name: The name of the static segment.
        :type name: str

        :param tags: A list of tags for the static segment.
        :type tags: [str], optional
        """
        if tags is not unset:
            kwargs["tags"] = tags
        super().__init__(kwargs)

        self_.description = description
        self_.journey_query_object = journey_query_object
        self_.name = name
