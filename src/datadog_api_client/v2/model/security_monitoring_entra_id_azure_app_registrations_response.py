# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.security_monitoring_entra_id_azure_app_registrations_data import (
        SecurityMonitoringEntraIdAzureAppRegistrationsData,
    )


class SecurityMonitoringEntraIdAzureAppRegistrationsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_entra_id_azure_app_registrations_data import (
            SecurityMonitoringEntraIdAzureAppRegistrationsData,
        )

        return {
            "data": (SecurityMonitoringEntraIdAzureAppRegistrationsData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: SecurityMonitoringEntraIdAzureAppRegistrationsData, **kwargs):
        """
        Response containing the Azure App Registration prerequisites for the Entra ID integration.

        :param data: The Azure App Registration prerequisites for the Entra ID integration.
        :type data: SecurityMonitoringEntraIdAzureAppRegistrationsData
        """
        super().__init__(kwargs)

        self_.data = data
