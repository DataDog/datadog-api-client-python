# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class DashboardInlineSchema30(ModelSimple):
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
    AUTO: ClassVar["DashboardInlineSchema30"]
    COMPACT: ClassVar["DashboardInlineSchema30"]
    FULL: ClassVar["DashboardInlineSchema30"]
    FIT_CONTENT: ClassVar["DashboardInlineSchema30"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


DashboardInlineSchema30.AUTO = DashboardInlineSchema30("auto")
DashboardInlineSchema30.COMPACT = DashboardInlineSchema30("compact")
DashboardInlineSchema30.FULL = DashboardInlineSchema30("full")
DashboardInlineSchema30.FIT_CONTENT = DashboardInlineSchema30("fit-content")
