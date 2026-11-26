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
    from datadog_api_client.v1_20270101.model.formula_apm_metrics_query import FormulaApmMetricsQuery
    from datadog_api_client.v1_20270101.model.apm_metrics_histogram_request_request_type import (
        ApmMetricsHistogramRequestRequestType,
    )


class ApmMetricsHistogramRequest(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.widget_number_format import WidgetNumberFormat
        from datadog_api_client.v1_20270101.model.formula_apm_metrics_query import FormulaApmMetricsQuery
        from datadog_api_client.v1_20270101.model.apm_metrics_histogram_request_request_type import (
            ApmMetricsHistogramRequestRequestType,
        )

        return {
            "number_format": (WidgetNumberFormat,),
            "query": (FormulaApmMetricsQuery,),
            "request_type": (ApmMetricsHistogramRequestRequestType,),
        }

    attribute_map = {
        "number_format": "number_format",
        "query": "query",
        "request_type": "request_type",
    }

    def __init__(
        self_,
        query: FormulaApmMetricsQuery,
        request_type: ApmMetricsHistogramRequestRequestType,
        number_format: Union[WidgetNumberFormat, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param number_format: Test-only generated schema for the dashboard versioning proof of concept.
        :type number_format: WidgetNumberFormat, optional

        :param query: Test-only generated schema for the dashboard versioning proof of concept.
        :type query: FormulaApmMetricsQuery

        :param request_type: Test-only generated schema for the dashboard versioning proof of concept.
        :type request_type: ApmMetricsHistogramRequestRequestType
        """
        if number_format is not unset:
            kwargs["number_format"] = number_format
        super().__init__(kwargs)

        self_.query = query
        self_.request_type = request_type
