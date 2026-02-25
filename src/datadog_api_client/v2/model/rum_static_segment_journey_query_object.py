# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.rum_static_segment_journey_node import RumStaticSegmentJourneyNode


class RumStaticSegmentJourneyQueryObject(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_static_segment_journey_node import RumStaticSegmentJourneyNode

        return {
            "nodes": ([RumStaticSegmentJourneyNode],),
        }

    attribute_map = {
        "nodes": "nodes",
    }

    def __init__(self_, nodes: List[RumStaticSegmentJourneyNode], **kwargs):
        """
        The journey query object used to compute the static segment user list.

        :param nodes: The list of journey nodes defining the query.
        :type nodes: [RumStaticSegmentJourneyNode]
        """
        super().__init__(kwargs)

        self_.nodes = nodes
