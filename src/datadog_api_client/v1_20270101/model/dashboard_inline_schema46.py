# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class DashboardInlineSchema46(ModelSimple):
    """
    Test-only generated schema for the dashboard versioning proof of concept.

    :param value: Must be one of ["burn_rate", "error_budget_burndown", "error_budget_remaining", "slo_status"].
    :type value: str
    """

    allowed_values = {
        "burn_rate",
        "error_budget_burndown",
        "error_budget_remaining",
        "slo_status",
    }
    BURN_RATE: ClassVar["DashboardInlineSchema46"]
    ERROR_BUDGET_BURNDOWN: ClassVar["DashboardInlineSchema46"]
    ERROR_BUDGET_REMAINING: ClassVar["DashboardInlineSchema46"]
    SLO_STATUS: ClassVar["DashboardInlineSchema46"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


DashboardInlineSchema46.BURN_RATE = DashboardInlineSchema46("burn_rate")
DashboardInlineSchema46.ERROR_BUDGET_BURNDOWN = DashboardInlineSchema46("error_budget_burndown")
DashboardInlineSchema46.ERROR_BUDGET_REMAINING = DashboardInlineSchema46("error_budget_remaining")
DashboardInlineSchema46.SLO_STATUS = DashboardInlineSchema46("slo_status")
