# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SecurityMonitoringStandardDataSource(ModelSimple):
    """
    Source of events, either logs or audit trail.

    :param value: If omitted defaults to "logs". Must be one of ["logs", "audit"].
    :type value: str
    """

    allowed_values = {
        "logs",
        "audit",
    }
    LOGS: ClassVar["SecurityMonitoringStandardDataSource"]
    AUDIT: ClassVar["SecurityMonitoringStandardDataSource"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SecurityMonitoringStandardDataSource.LOGS = SecurityMonitoringStandardDataSource("logs")
SecurityMonitoringStandardDataSource.AUDIT = SecurityMonitoringStandardDataSource("audit")
