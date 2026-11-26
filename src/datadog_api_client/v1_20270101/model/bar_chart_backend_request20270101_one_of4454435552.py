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
    from datadog_api_client.v1_20270101.model.threshold_formatting_rule import ThresholdFormattingRule
    from datadog_api_client.v1_20270101.model.bar_chart_backend_request_any_of_any_of_item_request_type4443922944 import (
        BarChartBackendRequestAnyOfAnyOfItemRequestType4443922944,
    )
    from datadog_api_client.v1_20270101.model.bar_chart_backend_request_any_of_any_of_item_response_format4443923264 import (
        BarChartBackendRequestAnyOfAnyOfItemResponseFormat4443923264,
    )


class BarChartBackendRequest20270101OneOf4454435552(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.threshold_formatting_rule import ThresholdFormattingRule
        from datadog_api_client.v1_20270101.model.bar_chart_backend_request_any_of_any_of_item_request_type4443922944 import (
            BarChartBackendRequestAnyOfAnyOfItemRequestType4443922944,
        )
        from datadog_api_client.v1_20270101.model.bar_chart_backend_request_any_of_any_of_item_response_format4443923264 import (
            BarChartBackendRequestAnyOfAnyOfItemResponseFormat4443923264,
        )

        return {
            "conditional_formats": ([ThresholdFormattingRule],),
            "ddsql_query": (str,),
            "request_type": (BarChartBackendRequestAnyOfAnyOfItemRequestType4443922944,),
            "response_format": (BarChartBackendRequestAnyOfAnyOfItemResponseFormat4443923264,),
        }

    attribute_map = {
        "conditional_formats": "conditional_formats",
        "ddsql_query": "ddsql_query",
        "request_type": "request_type",
        "response_format": "response_format",
    }

    def __init__(
        self_,
        ddsql_query: str,
        request_type: BarChartBackendRequestAnyOfAnyOfItemRequestType4443922944,
        response_format: BarChartBackendRequestAnyOfAnyOfItemResponseFormat4443923264,
        conditional_formats: Union[List[ThresholdFormattingRule], UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param conditional_formats: Test-only generated schema for the dashboard versioning proof of concept.
        :type conditional_formats: [ThresholdFormattingRule], optional

        :param ddsql_query: Test-only generated schema for the dashboard versioning proof of concept.
        :type ddsql_query: str

        :param request_type: Test-only generated schema for the dashboard versioning proof of concept.
        :type request_type: BarChartBackendRequestAnyOfAnyOfItemRequestType4443922944

        :param response_format: Test-only generated schema for the dashboard versioning proof of concept.
        :type response_format: BarChartBackendRequestAnyOfAnyOfItemResponseFormat4443923264
        """
        if conditional_formats is not unset:
            kwargs["conditional_formats"] = conditional_formats
        super().__init__(kwargs)

        self_.ddsql_query = ddsql_query
        self_.request_type = request_type
        self_.response_format = response_format
