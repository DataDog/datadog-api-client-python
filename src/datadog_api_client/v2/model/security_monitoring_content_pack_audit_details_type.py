# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SecurityMonitoringContentPackAuditDetailsType(ModelSimple):
    """
    Type for audit trail content pack details.

    :param value: If omitted defaults to "audit". Must be one of ["audit"].
    :type value: str
    """

    allowed_values = {
        "audit",
    }
    AUDIT: ClassVar["SecurityMonitoringContentPackAuditDetailsType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SecurityMonitoringContentPackAuditDetailsType.AUDIT = SecurityMonitoringContentPackAuditDetailsType("audit")
