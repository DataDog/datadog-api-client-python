# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class DashboardInlineSchema9(ModelSimple):
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
    AUTO: ClassVar["DashboardInlineSchema9"]
    COMPACT: ClassVar["DashboardInlineSchema9"]
    FULL: ClassVar["DashboardInlineSchema9"]
    FIT_CONTENT: ClassVar["DashboardInlineSchema9"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


DashboardInlineSchema9.AUTO = DashboardInlineSchema9("auto")
DashboardInlineSchema9.COMPACT = DashboardInlineSchema9("compact")
DashboardInlineSchema9.FULL = DashboardInlineSchema9("full")
DashboardInlineSchema9.FIT_CONTENT = DashboardInlineSchema9("fit-content")
