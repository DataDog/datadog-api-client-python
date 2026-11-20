# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v1_20270101.model.widget_number_format import WidgetNumberFormat
    from datadog_api_client.v1_20270101.model.formula_apm_stats_query import FormulaApmStatsQuery
    from datadog_api_client.v1_20270101.model.distribution_backend_request_any_of_any_of_item_request_type4445470944 import (
        DistributionBackendRequestAnyOfAnyOfItemRequestType4445470944,
    )
    from datadog_api_client.v1_20270101.model.request_style import RequestStyle
    from datadog_api_client.v1_20270101.model.formula_apm_dependency_stats_query import FormulaApmDependencyStatsQuery
    from datadog_api_client.v1_20270101.model.formula_apm_resource_stats_query import FormulaApmResourceStatsQuery


class DistributionBackendRequest20270101OneOf4455774496(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.widget_number_format import WidgetNumberFormat
        from datadog_api_client.v1_20270101.model.formula_apm_stats_query import FormulaApmStatsQuery
        from datadog_api_client.v1_20270101.model.distribution_backend_request_any_of_any_of_item_request_type4445470944 import (
            DistributionBackendRequestAnyOfAnyOfItemRequestType4445470944,
        )
        from datadog_api_client.v1_20270101.model.request_style import RequestStyle

        return {
            "number_format": (WidgetNumberFormat,),
            "query": (FormulaApmStatsQuery,),
            "request_type": (DistributionBackendRequestAnyOfAnyOfItemRequestType4445470944,),
            "style": (RequestStyle,),
        }

    attribute_map = {
        "number_format": "number_format",
        "query": "query",
        "request_type": "request_type",
        "style": "style",
    }

    def __init__(
        self_,
        query: Union[FormulaApmStatsQuery, FormulaApmDependencyStatsQuery, FormulaApmResourceStatsQuery],
        request_type: DistributionBackendRequestAnyOfAnyOfItemRequestType4445470944,
        number_format: Union[WidgetNumberFormat, UnsetType] = unset,
        style: Union[RequestStyle, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param number_format: Test-only generated schema for the dashboard versioning proof of concept.
        :type number_format: WidgetNumberFormat, optional

        :param query: Test-only generated schema for the dashboard versioning proof of concept.
        :type query: FormulaApmStatsQuery

        :param request_type: Test-only generated schema for the dashboard versioning proof of concept.
        :type request_type: DistributionBackendRequestAnyOfAnyOfItemRequestType4445470944

        :param style: Test-only generated schema for the dashboard versioning proof of concept.
        :type style: RequestStyle, optional
        """
        if number_format is not unset:
            kwargs["number_format"] = number_format
        if style is not unset:
            kwargs["style"] = style
        super().__init__(kwargs)

        self_.query = query
        self_.request_type = request_type
