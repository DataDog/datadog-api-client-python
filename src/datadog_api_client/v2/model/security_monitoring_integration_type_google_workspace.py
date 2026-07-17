# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SecurityMonitoringIntegrationTypeGoogleWorkspace(ModelSimple):
    """
    The source type for a Google Workspace entity context sync.

    :param value: If omitted defaults to "GOOGLE_WORKSPACE". Must be one of ["GOOGLE_WORKSPACE"].
    :type value: str
    """

    allowed_values = {
        "GOOGLE_WORKSPACE",
    }
    GOOGLE_WORKSPACE: ClassVar["SecurityMonitoringIntegrationTypeGoogleWorkspace"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SecurityMonitoringIntegrationTypeGoogleWorkspace.GOOGLE_WORKSPACE = SecurityMonitoringIntegrationTypeGoogleWorkspace(
    "GOOGLE_WORKSPACE"
)
