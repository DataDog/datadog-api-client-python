# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class DashboardInlineSchema28(ModelSimple):
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
    AUTO: ClassVar["DashboardInlineSchema28"]
    COMPACT: ClassVar["DashboardInlineSchema28"]
    FULL: ClassVar["DashboardInlineSchema28"]
    FIT_CONTENT: ClassVar["DashboardInlineSchema28"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


DashboardInlineSchema28.AUTO = DashboardInlineSchema28("auto")
DashboardInlineSchema28.COMPACT = DashboardInlineSchema28("compact")
DashboardInlineSchema28.FULL = DashboardInlineSchema28("full")
DashboardInlineSchema28.FIT_CONTENT = DashboardInlineSchema28("fit-content")
