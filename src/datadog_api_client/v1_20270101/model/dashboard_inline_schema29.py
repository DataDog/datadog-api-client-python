# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class DashboardInlineSchema29(ModelSimple):
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
    AUTO: ClassVar["DashboardInlineSchema29"]
    COMPACT: ClassVar["DashboardInlineSchema29"]
    FULL: ClassVar["DashboardInlineSchema29"]
    FIT_CONTENT: ClassVar["DashboardInlineSchema29"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


DashboardInlineSchema29.AUTO = DashboardInlineSchema29("auto")
DashboardInlineSchema29.COMPACT = DashboardInlineSchema29("compact")
DashboardInlineSchema29.FULL = DashboardInlineSchema29("full")
DashboardInlineSchema29.FIT_CONTENT = DashboardInlineSchema29("fit-content")
