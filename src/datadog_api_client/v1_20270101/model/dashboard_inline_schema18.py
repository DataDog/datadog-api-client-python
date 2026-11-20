# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class DashboardInlineSchema18(ModelSimple):
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
    AUTO: ClassVar["DashboardInlineSchema18"]
    COMPACT: ClassVar["DashboardInlineSchema18"]
    FULL: ClassVar["DashboardInlineSchema18"]
    FIT_CONTENT: ClassVar["DashboardInlineSchema18"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


DashboardInlineSchema18.AUTO = DashboardInlineSchema18("auto")
DashboardInlineSchema18.COMPACT = DashboardInlineSchema18("compact")
DashboardInlineSchema18.FULL = DashboardInlineSchema18("full")
DashboardInlineSchema18.FIT_CONTENT = DashboardInlineSchema18("fit-content")
