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
    from datadog_api_client.v2.model.network_health_insight import NetworkHealthInsight


class NetworkHealthInsightsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.network_health_insight import NetworkHealthInsight

        return {
            "data": ([NetworkHealthInsight],),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: List[NetworkHealthInsight], **kwargs):
        """
        Response containing a list of network health insights for the organization.

        :param data: Array of network health insights returned for the query window.
        :type data: [NetworkHealthInsight]
        """
        super().__init__(kwargs)

        self_.data = data
