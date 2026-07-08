# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SecurityMonitoringEntraIdAzureAppRegistrationsResourceType(ModelSimple):
    """
    The type of the resource. The value should always be `entra_id_azure_app_registrations`.

    :param value: If omitted defaults to "entra_id_azure_app_registrations". Must be one of ["entra_id_azure_app_registrations"].
    :type value: str
    """

    allowed_values = {
        "entra_id_azure_app_registrations",
    }
    ENTRA_ID_AZURE_APP_REGISTRATIONS: ClassVar["SecurityMonitoringEntraIdAzureAppRegistrationsResourceType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SecurityMonitoringEntraIdAzureAppRegistrationsResourceType.ENTRA_ID_AZURE_APP_REGISTRATIONS = (
    SecurityMonitoringEntraIdAzureAppRegistrationsResourceType("entra_id_azure_app_registrations")
)
