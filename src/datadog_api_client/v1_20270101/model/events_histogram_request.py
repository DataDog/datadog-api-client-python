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
    from datadog_api_client.v1_20270101.model.formula_events_query import FormulaEventsQuery
    from datadog_api_client.v1_20270101.model.events_histogram_request_request_type import (
        EventsHistogramRequestRequestType,
    )


class EventsHistogramRequest(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.widget_number_format import WidgetNumberFormat
        from datadog_api_client.v1_20270101.model.formula_events_query import FormulaEventsQuery
        from datadog_api_client.v1_20270101.model.events_histogram_request_request_type import (
            EventsHistogramRequestRequestType,
        )

        return {
            "number_format": (WidgetNumberFormat,),
            "query": (FormulaEventsQuery,),
            "request_type": (EventsHistogramRequestRequestType,),
        }

    attribute_map = {
        "number_format": "number_format",
        "query": "query",
        "request_type": "request_type",
    }

    def __init__(
        self_,
        query: FormulaEventsQuery,
        request_type: EventsHistogramRequestRequestType,
        number_format: Union[WidgetNumberFormat, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param number_format: Test-only generated schema for the dashboard versioning proof of concept.
        :type number_format: WidgetNumberFormat, optional

        :param query: Test-only generated schema for the dashboard versioning proof of concept.
        :type query: FormulaEventsQuery

        :param request_type: Test-only generated schema for the dashboard versioning proof of concept.
        :type request_type: EventsHistogramRequestRequestType
        """
        if number_format is not unset:
            kwargs["number_format"] = number_format
        super().__init__(kwargs)

        self_.query = query
        self_.request_type = request_type
