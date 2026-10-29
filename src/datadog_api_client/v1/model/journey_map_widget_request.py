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
    from datadog_api_client.v1.model.journey_map_query import JourneyMapQuery
    from datadog_api_client.v1.model.journey_map_request_type import JourneyMapRequestType


class JourneyMapWidgetRequest(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.journey_map_query import JourneyMapQuery
        from datadog_api_client.v1.model.journey_map_request_type import JourneyMapRequestType

        return {
            "query": (JourneyMapQuery,),
            "request_type": (JourneyMapRequestType,),
        }

    attribute_map = {
        "query": "query",
        "request_type": "request_type",
    }

    def __init__(self_, query: JourneyMapQuery, request_type: JourneyMapRequestType, **kwargs):
        """
        Journey Paths widget request.

        :param query: Journey Paths query definition.
        :type query: JourneyMapQuery

        :param request_type: Request type for the Journey Paths widget.
        :type request_type: JourneyMapRequestType
        """
        super().__init__(kwargs)

        self_.query = query
        self_.request_type = request_type
