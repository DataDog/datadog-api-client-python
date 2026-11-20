# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class DashboardInlineSchema12(ModelSimple):
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
    AUTO: ClassVar["DashboardInlineSchema12"]
    COMPACT: ClassVar["DashboardInlineSchema12"]
    FULL: ClassVar["DashboardInlineSchema12"]
    FIT_CONTENT: ClassVar["DashboardInlineSchema12"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


DashboardInlineSchema12.AUTO = DashboardInlineSchema12("auto")
DashboardInlineSchema12.COMPACT = DashboardInlineSchema12("compact")
DashboardInlineSchema12.FULL = DashboardInlineSchema12("full")
DashboardInlineSchema12.FIT_CONTENT = DashboardInlineSchema12("fit-content")
