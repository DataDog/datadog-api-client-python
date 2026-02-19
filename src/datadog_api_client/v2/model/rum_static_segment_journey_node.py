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
    from datadog_api_client.v2.model.rum_static_segment_journey_filter import RumStaticSegmentJourneyFilter


class RumStaticSegmentJourneyNode(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_static_segment_journey_filter import RumStaticSegmentJourneyFilter

        return {
            "filters": ([RumStaticSegmentJourneyFilter],),
        }

    attribute_map = {
        "filters": "filters",
    }

    def __init__(self_, filters: List[RumStaticSegmentJourneyFilter], **kwargs):
        """
        A node in a journey query object.

        :param filters: The list of filters for this node.
        :type filters: [RumStaticSegmentJourneyFilter]
        """
        super().__init__(kwargs)

        self_.filters = filters
