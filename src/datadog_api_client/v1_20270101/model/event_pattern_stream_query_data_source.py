# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class EventPatternStreamQueryDataSource(ModelSimple):
    """
    Test-only generated schema for the dashboard versioning proof of concept.

    :param value: If omitted defaults to "event_pattern_stream". Must be one of ["event_pattern_stream"].
    :type value: str
    """

    allowed_values = {
        "event_pattern_stream",
    }
    EVENT_PATTERN_STREAM: ClassVar["EventPatternStreamQueryDataSource"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


EventPatternStreamQueryDataSource.EVENT_PATTERN_STREAM = EventPatternStreamQueryDataSource("event_pattern_stream")
