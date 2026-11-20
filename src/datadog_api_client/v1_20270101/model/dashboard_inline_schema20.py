# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class DashboardInlineSchema20(ModelSimple):
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
    AUTO: ClassVar["DashboardInlineSchema20"]
    COMPACT: ClassVar["DashboardInlineSchema20"]
    FULL: ClassVar["DashboardInlineSchema20"]
    FIT_CONTENT: ClassVar["DashboardInlineSchema20"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


DashboardInlineSchema20.AUTO = DashboardInlineSchema20("auto")
DashboardInlineSchema20.COMPACT = DashboardInlineSchema20("compact")
DashboardInlineSchema20.FULL = DashboardInlineSchema20("full")
DashboardInlineSchema20.FIT_CONTENT = DashboardInlineSchema20("fit-content")
