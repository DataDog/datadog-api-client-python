# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class DashboardInlineSchema35(ModelSimple):
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
    AUTO: ClassVar["DashboardInlineSchema35"]
    COMPACT: ClassVar["DashboardInlineSchema35"]
    FULL: ClassVar["DashboardInlineSchema35"]
    FIT_CONTENT: ClassVar["DashboardInlineSchema35"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


DashboardInlineSchema35.AUTO = DashboardInlineSchema35("auto")
DashboardInlineSchema35.COMPACT = DashboardInlineSchema35("compact")
DashboardInlineSchema35.FULL = DashboardInlineSchema35("full")
DashboardInlineSchema35.FIT_CONTENT = DashboardInlineSchema35("fit-content")
