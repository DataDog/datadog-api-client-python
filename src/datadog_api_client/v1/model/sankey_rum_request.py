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
    from datadog_api_client.v1.model.sankey_rum_query import SankeyRumQuery
    from datadog_api_client.v1.model.sankey_widget_definition_type import SankeyWidgetDefinitionType


class SankeyRumRequest(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.sankey_rum_query import SankeyRumQuery
        from datadog_api_client.v1.model.sankey_widget_definition_type import SankeyWidgetDefinitionType

        return {
            "query": (SankeyRumQuery,),
            "request_type": (SankeyWidgetDefinitionType,),
        }

    attribute_map = {
        "query": "query",
        "request_type": "request_type",
    }

    def __init__(self_, query: SankeyRumQuery, request_type: SankeyWidgetDefinitionType, **kwargs):
        """
        Sankey widget with RUM data source.

        :param query: Sankey widget with RUM data source query.
        :type query: SankeyRumQuery

        :param request_type: Type of the Sankey widget.
        :type request_type: SankeyWidgetDefinitionType
        """
        super().__init__(kwargs)

        self_.query = query
        self_.request_type = request_type
