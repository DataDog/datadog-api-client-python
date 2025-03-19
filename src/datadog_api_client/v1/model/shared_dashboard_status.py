# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SharedDashboardStatus(ModelSimple):
    """
    Active means the dashboard is publicly available. Paused means the dashboard is not publicly available.

    :param value: Must be one of ["active", "paused"].
    :type value: str
    """

    allowed_values = {
        "active",
        "paused",
    }
    ACTIVE: ClassVar["SharedDashboardStatus"]
    PAUSED: ClassVar["SharedDashboardStatus"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SharedDashboardStatus.ACTIVE = SharedDashboardStatus("active")
SharedDashboardStatus.PAUSED = SharedDashboardStatus("paused")
