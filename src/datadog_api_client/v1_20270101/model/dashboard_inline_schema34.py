# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class DashboardInlineSchema34(ModelSimple):
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
    AUTO: ClassVar["DashboardInlineSchema34"]
    COMPACT: ClassVar["DashboardInlineSchema34"]
    FULL: ClassVar["DashboardInlineSchema34"]
    FIT_CONTENT: ClassVar["DashboardInlineSchema34"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


DashboardInlineSchema34.AUTO = DashboardInlineSchema34("auto")
DashboardInlineSchema34.COMPACT = DashboardInlineSchema34("compact")
DashboardInlineSchema34.FULL = DashboardInlineSchema34("full")
DashboardInlineSchema34.FIT_CONTENT = DashboardInlineSchema34("fit-content")
