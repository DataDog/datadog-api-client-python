# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SecurityMonitoringCriticalAssetType(ModelSimple):
    """
    The type of the resource. The value should always be `critical_assets`.

    :param value: If omitted defaults to "critical_assets". Must be one of ["critical_assets"].
    :type value: str
    """

    allowed_values = {
        "critical_assets",
    }
    CRITICAL_ASSETS: ClassVar["SecurityMonitoringCriticalAssetType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SecurityMonitoringCriticalAssetType.CRITICAL_ASSETS = SecurityMonitoringCriticalAssetType("critical_assets")
