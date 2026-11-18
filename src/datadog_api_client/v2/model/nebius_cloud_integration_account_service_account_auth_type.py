# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class NebiusCloudIntegrationAccountServiceAccountAuthType(ModelSimple):
    """
    The authentication method type.

    :param value: If omitted defaults to "nebius_service_account". Must be one of ["nebius_service_account"].
    :type value: str
    """

    allowed_values = {
        "nebius_service_account",
    }
    NEBIUS_SERVICE_ACCOUNT: ClassVar["NebiusCloudIntegrationAccountServiceAccountAuthType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


NebiusCloudIntegrationAccountServiceAccountAuthType.NEBIUS_SERVICE_ACCOUNT = (
    NebiusCloudIntegrationAccountServiceAccountAuthType("nebius_service_account")
)
