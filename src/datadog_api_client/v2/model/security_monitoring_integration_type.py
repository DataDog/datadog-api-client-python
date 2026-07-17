# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SecurityMonitoringIntegrationType(ModelSimple):
    """
    The type of external source that provides entities to Cloud SIEM.

    :param value: Must be one of ["GOOGLE_WORKSPACE", "OKTA", "ENTRA_ID"].
    :type value: str
    """

    allowed_values = {
        "GOOGLE_WORKSPACE",
        "OKTA",
        "ENTRA_ID",
    }
    GOOGLE_WORKSPACE: ClassVar["SecurityMonitoringIntegrationType"]
    OKTA: ClassVar["SecurityMonitoringIntegrationType"]
    ENTRA_ID: ClassVar["SecurityMonitoringIntegrationType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SecurityMonitoringIntegrationType.GOOGLE_WORKSPACE = SecurityMonitoringIntegrationType("GOOGLE_WORKSPACE")
SecurityMonitoringIntegrationType.OKTA = SecurityMonitoringIntegrationType("OKTA")
SecurityMonitoringIntegrationType.ENTRA_ID = SecurityMonitoringIntegrationType("ENTRA_ID")
