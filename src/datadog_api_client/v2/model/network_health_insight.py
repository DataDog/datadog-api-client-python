# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.network_health_insight_attributes import NetworkHealthInsightAttributes
    from datadog_api_client.v2.model.network_health_insights_type import NetworkHealthInsightsType


class NetworkHealthInsight(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.network_health_insight_attributes import NetworkHealthInsightAttributes
        from datadog_api_client.v2.model.network_health_insights_type import NetworkHealthInsightsType

        return {
            "attributes": (NetworkHealthInsightAttributes,),
            "id": (str,),
            "type": (NetworkHealthInsightsType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: NetworkHealthInsightAttributes, id: str, type: NetworkHealthInsightsType, **kwargs):
        """
        A single network health insight describing a service-to-service connectivity issue.

        :param attributes: Detailed attributes of a network health insight.
        :type attributes: NetworkHealthInsightAttributes

        :param id: Unique identifier for this network health insight.
        :type id: str

        :param type: The resource type for network health insights. Always ``network-health-insights``.
        :type type: NetworkHealthInsightsType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
