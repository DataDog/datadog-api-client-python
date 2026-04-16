# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SlosMeasure(ModelSimple):
    """
    The SLO measurement to retrieve.

    :param value: Must be one of ["good_events", "bad_events", "slo_status", "error_budget_remaining", "error_budget_remaining_history", "error_budget_burndown", "burn_rate", "slo_status_history", "good_minutes", "bad_minutes"].
    :type value: str
    """

    allowed_values = {
        "good_events",
        "bad_events",
        "slo_status",
        "error_budget_remaining",
        "error_budget_remaining_history",
        "error_budget_burndown",
        "burn_rate",
        "slo_status_history",
        "good_minutes",
        "bad_minutes",
    }
    GOOD_EVENTS: ClassVar["SlosMeasure"]
    BAD_EVENTS: ClassVar["SlosMeasure"]
    SLO_STATUS: ClassVar["SlosMeasure"]
    ERROR_BUDGET_REMAINING: ClassVar["SlosMeasure"]
    ERROR_BUDGET_REMAINING_HISTORY: ClassVar["SlosMeasure"]
    ERROR_BUDGET_BURNDOWN: ClassVar["SlosMeasure"]
    BURN_RATE: ClassVar["SlosMeasure"]
    SLO_STATUS_HISTORY: ClassVar["SlosMeasure"]
    GOOD_MINUTES: ClassVar["SlosMeasure"]
    BAD_MINUTES: ClassVar["SlosMeasure"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SlosMeasure.GOOD_EVENTS = SlosMeasure("good_events")
SlosMeasure.BAD_EVENTS = SlosMeasure("bad_events")
SlosMeasure.SLO_STATUS = SlosMeasure("slo_status")
SlosMeasure.ERROR_BUDGET_REMAINING = SlosMeasure("error_budget_remaining")
SlosMeasure.ERROR_BUDGET_REMAINING_HISTORY = SlosMeasure("error_budget_remaining_history")
SlosMeasure.ERROR_BUDGET_BURNDOWN = SlosMeasure("error_budget_burndown")
SlosMeasure.BURN_RATE = SlosMeasure("burn_rate")
SlosMeasure.SLO_STATUS_HISTORY = SlosMeasure("slo_status_history")
SlosMeasure.GOOD_MINUTES = SlosMeasure("good_minutes")
SlosMeasure.BAD_MINUTES = SlosMeasure("bad_minutes")
