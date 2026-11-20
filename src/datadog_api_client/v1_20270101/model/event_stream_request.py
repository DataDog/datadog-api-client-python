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
    from datadog_api_client.v1_20270101.model.event_stream_request_columns_items import EventStreamRequestColumnsItems
    from datadog_api_client.v1_20270101.model.event_stream_query import EventStreamQuery
    from datadog_api_client.v1_20270101.model.event_stream_request_response_format import (
        EventStreamRequestResponseFormat,
    )


class EventStreamRequest(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.event_stream_request_columns_items import (
            EventStreamRequestColumnsItems,
        )
        from datadog_api_client.v1_20270101.model.event_stream_query import EventStreamQuery
        from datadog_api_client.v1_20270101.model.event_stream_request_response_format import (
            EventStreamRequestResponseFormat,
        )

        return {
            "columns": ([EventStreamRequestColumnsItems],),
            "query": (EventStreamQuery,),
            "response_format": (EventStreamRequestResponseFormat,),
        }

    attribute_map = {
        "columns": "columns",
        "query": "query",
        "response_format": "response_format",
    }

    def __init__(
        self_,
        columns: List[EventStreamRequestColumnsItems],
        query: EventStreamQuery,
        response_format: EventStreamRequestResponseFormat,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param columns: Test-only generated schema for the dashboard versioning proof of concept.
        :type columns: [EventStreamRequestColumnsItems]

        :param query: Test-only generated schema for the dashboard versioning proof of concept.
        :type query: EventStreamQuery

        :param response_format: Test-only generated schema for the dashboard versioning proof of concept.
        :type response_format: EventStreamRequestResponseFormat
        """
        super().__init__(kwargs)

        self_.columns = columns
        self_.query = query
        self_.response_format = response_format
