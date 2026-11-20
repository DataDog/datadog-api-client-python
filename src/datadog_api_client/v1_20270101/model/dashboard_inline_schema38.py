# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class DashboardInlineSchema38(ModelSimple):
    """
    Test-only generated schema for the dashboard versioning proof of concept.

    :param value: Must be one of ["id", "title", "subtitle"].
    :type value: str
    """

    allowed_values = {
        "id",
        "title",
        "subtitle",
    }
    ID: ClassVar["DashboardInlineSchema38"]
    TITLE: ClassVar["DashboardInlineSchema38"]
    SUBTITLE: ClassVar["DashboardInlineSchema38"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


DashboardInlineSchema38.ID = DashboardInlineSchema38("id")
DashboardInlineSchema38.TITLE = DashboardInlineSchema38("title")
DashboardInlineSchema38.SUBTITLE = DashboardInlineSchema38("subtitle")
