# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class DashboardInlineSchema23(ModelSimple):
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
    AUTO: ClassVar["DashboardInlineSchema23"]
    COMPACT: ClassVar["DashboardInlineSchema23"]
    FULL: ClassVar["DashboardInlineSchema23"]
    FIT_CONTENT: ClassVar["DashboardInlineSchema23"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


DashboardInlineSchema23.AUTO = DashboardInlineSchema23("auto")
DashboardInlineSchema23.COMPACT = DashboardInlineSchema23("compact")
DashboardInlineSchema23.FULL = DashboardInlineSchema23("full")
DashboardInlineSchema23.FIT_CONTENT = DashboardInlineSchema23("fit-content")
