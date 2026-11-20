# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class DashboardInlineSchema27(ModelSimple):
    """
    Test-only generated schema for the dashboard versioning proof of concept.

    :param value: Must be one of ["auto", "compact", "full", "fit-content"].
    :type value: str
    """

    allowed_values = {
        "auto",
        "compact",
        "full",
        "fit-content",
    }
    AUTO: ClassVar["DashboardInlineSchema27"]
    COMPACT: ClassVar["DashboardInlineSchema27"]
    FULL: ClassVar["DashboardInlineSchema27"]
    FIT_CONTENT: ClassVar["DashboardInlineSchema27"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


DashboardInlineSchema27.AUTO = DashboardInlineSchema27("auto")
DashboardInlineSchema27.COMPACT = DashboardInlineSchema27("compact")
DashboardInlineSchema27.FULL = DashboardInlineSchema27("full")
DashboardInlineSchema27.FIT_CONTENT = DashboardInlineSchema27("fit-content")
