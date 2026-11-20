# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class CaseMetric(ModelSimple):
    """
    Test-only generated schema for the dashboard versioning proof of concept.

    :param value: Must be one of ["time_to_close", "time_to_assign", "event_count"].
    :type value: str
    """

    allowed_values = {
        "time_to_close",
        "time_to_assign",
        "event_count",
    }
    TIME_TO_CLOSE: ClassVar["CaseMetric"]
    TIME_TO_ASSIGN: ClassVar["CaseMetric"]
    EVENT_COUNT: ClassVar["CaseMetric"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


CaseMetric.TIME_TO_CLOSE = CaseMetric("time_to_close")
CaseMetric.TIME_TO_ASSIGN = CaseMetric("time_to_assign")
CaseMetric.EVENT_COUNT = CaseMetric("event_count")
