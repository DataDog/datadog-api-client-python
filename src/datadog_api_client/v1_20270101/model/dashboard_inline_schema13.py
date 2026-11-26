# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class DashboardInlineSchema13(ModelSimple):
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
    AUTO: ClassVar["DashboardInlineSchema13"]
    COMPACT: ClassVar["DashboardInlineSchema13"]
    FULL: ClassVar["DashboardInlineSchema13"]
    FIT_CONTENT: ClassVar["DashboardInlineSchema13"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


DashboardInlineSchema13.AUTO = DashboardInlineSchema13("auto")
DashboardInlineSchema13.COMPACT = DashboardInlineSchema13("compact")
DashboardInlineSchema13.FULL = DashboardInlineSchema13("full")
DashboardInlineSchema13.FIT_CONTENT = DashboardInlineSchema13("fit-content")
