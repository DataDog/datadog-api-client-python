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
    from datadog_api_client.v2.model.security_monitoring_entra_id_azure_app_registrations_attributes import (
        SecurityMonitoringEntraIdAzureAppRegistrationsAttributes,
    )
    from datadog_api_client.v2.model.security_monitoring_entra_id_azure_app_registrations_resource_type import (
        SecurityMonitoringEntraIdAzureAppRegistrationsResourceType,
    )


class SecurityMonitoringEntraIdAzureAppRegistrationsData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_entra_id_azure_app_registrations_attributes import (
            SecurityMonitoringEntraIdAzureAppRegistrationsAttributes,
        )
        from datadog_api_client.v2.model.security_monitoring_entra_id_azure_app_registrations_resource_type import (
            SecurityMonitoringEntraIdAzureAppRegistrationsResourceType,
        )

        return {
            "attributes": (SecurityMonitoringEntraIdAzureAppRegistrationsAttributes,),
            "id": (str,),
            "type": (SecurityMonitoringEntraIdAzureAppRegistrationsResourceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: SecurityMonitoringEntraIdAzureAppRegistrationsAttributes,
        id: str,
        type: SecurityMonitoringEntraIdAzureAppRegistrationsResourceType,
        **kwargs,
    ):
        """
        The Azure App Registration prerequisites for the Entra ID integration.

        :param attributes: The attributes of the Entra ID Azure App Registration prerequisites.
        :type attributes: SecurityMonitoringEntraIdAzureAppRegistrationsAttributes

        :param id: The ID of the organization the Azure App Registrations belong to.
        :type id: str

        :param type: The type of the resource. The value should always be ``entra_id_azure_app_registrations``.
        :type type: SecurityMonitoringEntraIdAzureAppRegistrationsResourceType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
