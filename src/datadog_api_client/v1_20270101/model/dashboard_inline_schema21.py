# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class DashboardInlineSchema21(ModelSimple):
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
    AUTO: ClassVar["DashboardInlineSchema21"]
    COMPACT: ClassVar["DashboardInlineSchema21"]
    FULL: ClassVar["DashboardInlineSchema21"]
    FIT_CONTENT: ClassVar["DashboardInlineSchema21"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


DashboardInlineSchema21.AUTO = DashboardInlineSchema21("auto")
DashboardInlineSchema21.COMPACT = DashboardInlineSchema21("compact")
DashboardInlineSchema21.FULL = DashboardInlineSchema21("full")
DashboardInlineSchema21.FIT_CONTENT = DashboardInlineSchema21("fit-content")
