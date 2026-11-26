# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class DashboardInlineSchema24(ModelSimple):
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
    AUTO: ClassVar["DashboardInlineSchema24"]
    COMPACT: ClassVar["DashboardInlineSchema24"]
    FULL: ClassVar["DashboardInlineSchema24"]
    FIT_CONTENT: ClassVar["DashboardInlineSchema24"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


DashboardInlineSchema24.AUTO = DashboardInlineSchema24("auto")
DashboardInlineSchema24.COMPACT = DashboardInlineSchema24("compact")
DashboardInlineSchema24.FULL = DashboardInlineSchema24("full")
DashboardInlineSchema24.FIT_CONTENT = DashboardInlineSchema24("fit-content")
