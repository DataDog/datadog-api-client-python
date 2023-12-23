# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    StringEnum,
)

from typing import ClassVar


class MonitorRenotifyStatusType(StringEnum):
    """
    The different statuses for which renotification is supported.

    :param value: Must be one of ["alert", "warn", "no data"].
    :type value: str
    """

    allowed_values = {
        "alert",
        "warn",
        "no data",
    }
    ALERT: ClassVar["MonitorRenotifyStatusType"]
    WARN: ClassVar["MonitorRenotifyStatusType"]
    NO_DATA: ClassVar["MonitorRenotifyStatusType"]


MonitorRenotifyStatusType.ALERT = MonitorRenotifyStatusType("alert")
MonitorRenotifyStatusType.WARN = MonitorRenotifyStatusType("warn")
MonitorRenotifyStatusType.NO_DATA = MonitorRenotifyStatusType("no data")
