# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    StringEnum,
)

from typing import ClassVar


class MonitorDowntimeMatchResourceType(StringEnum):
    """
    Monitor Downtime Match resource type.

    :param value: If omitted defaults to "downtime_match". Must be one of ["downtime_match"].
    :type value: str
    """

    allowed_values = {
        "downtime_match",
    }
    DOWNTIME_MATCH: ClassVar["MonitorDowntimeMatchResourceType"]


MonitorDowntimeMatchResourceType.DOWNTIME_MATCH = MonitorDowntimeMatchResourceType("downtime_match")
