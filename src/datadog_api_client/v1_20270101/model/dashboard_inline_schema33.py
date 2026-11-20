# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class DashboardInlineSchema33(ModelSimple):
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
    AUTO: ClassVar["DashboardInlineSchema33"]
    COMPACT: ClassVar["DashboardInlineSchema33"]
    FULL: ClassVar["DashboardInlineSchema33"]
    FIT_CONTENT: ClassVar["DashboardInlineSchema33"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


DashboardInlineSchema33.AUTO = DashboardInlineSchema33("auto")
DashboardInlineSchema33.COMPACT = DashboardInlineSchema33("compact")
DashboardInlineSchema33.FULL = DashboardInlineSchema33("full")
DashboardInlineSchema33.FIT_CONTENT = DashboardInlineSchema33("fit-content")
