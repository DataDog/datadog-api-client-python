# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SecurityMonitoringIntegrationTypeEntraId(ModelSimple):
    """
    The source type for an Entra ID entity context sync.

    :param value: If omitted defaults to "ENTRA_ID". Must be one of ["ENTRA_ID"].
    :type value: str
    """

    allowed_values = {
        "ENTRA_ID",
    }
    ENTRA_ID: ClassVar["SecurityMonitoringIntegrationTypeEntraId"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SecurityMonitoringIntegrationTypeEntraId.ENTRA_ID = SecurityMonitoringIntegrationTypeEntraId("ENTRA_ID")
