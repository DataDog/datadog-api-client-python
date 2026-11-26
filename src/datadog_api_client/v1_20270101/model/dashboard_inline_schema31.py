# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class DashboardInlineSchema31(ModelSimple):
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
    AUTO: ClassVar["DashboardInlineSchema31"]
    COMPACT: ClassVar["DashboardInlineSchema31"]
    FULL: ClassVar["DashboardInlineSchema31"]
    FIT_CONTENT: ClassVar["DashboardInlineSchema31"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


DashboardInlineSchema31.AUTO = DashboardInlineSchema31("auto")
DashboardInlineSchema31.COMPACT = DashboardInlineSchema31("compact")
DashboardInlineSchema31.FULL = DashboardInlineSchema31("full")
DashboardInlineSchema31.FIT_CONTENT = DashboardInlineSchema31("fit-content")
