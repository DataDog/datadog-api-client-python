# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    StringEnum,
)

from typing import ClassVar


class SecurityMonitoringSignalsSort(StringEnum):
    """
    The sort parameters used for querying security signals.

    :param value: Must be one of ["timestamp", "-timestamp"].
    :type value: str
    """

    allowed_values = {
        "timestamp",
        "-timestamp",
    }
    TIMESTAMP_ASCENDING: ClassVar["SecurityMonitoringSignalsSort"]
    TIMESTAMP_DESCENDING: ClassVar["SecurityMonitoringSignalsSort"]


SecurityMonitoringSignalsSort.TIMESTAMP_ASCENDING = SecurityMonitoringSignalsSort("timestamp")
SecurityMonitoringSignalsSort.TIMESTAMP_DESCENDING = SecurityMonitoringSignalsSort("-timestamp")
