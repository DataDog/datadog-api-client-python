# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class DashboardInlineSchema22(ModelSimple):
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
    AUTO: ClassVar["DashboardInlineSchema22"]
    COMPACT: ClassVar["DashboardInlineSchema22"]
    FULL: ClassVar["DashboardInlineSchema22"]
    FIT_CONTENT: ClassVar["DashboardInlineSchema22"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


DashboardInlineSchema22.AUTO = DashboardInlineSchema22("auto")
DashboardInlineSchema22.COMPACT = DashboardInlineSchema22("compact")
DashboardInlineSchema22.FULL = DashboardInlineSchema22("full")
DashboardInlineSchema22.FIT_CONTENT = DashboardInlineSchema22("fit-content")
