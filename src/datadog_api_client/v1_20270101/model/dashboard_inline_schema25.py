# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class DashboardInlineSchema25(ModelSimple):
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
    AUTO: ClassVar["DashboardInlineSchema25"]
    COMPACT: ClassVar["DashboardInlineSchema25"]
    FULL: ClassVar["DashboardInlineSchema25"]
    FIT_CONTENT: ClassVar["DashboardInlineSchema25"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


DashboardInlineSchema25.AUTO = DashboardInlineSchema25("auto")
DashboardInlineSchema25.COMPACT = DashboardInlineSchema25("compact")
DashboardInlineSchema25.FULL = DashboardInlineSchema25("full")
DashboardInlineSchema25.FIT_CONTENT = DashboardInlineSchema25("fit-content")
