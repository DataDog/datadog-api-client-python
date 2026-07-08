# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.security_monitoring_azure_app_registration import (
        SecurityMonitoringAzureAppRegistration,
    )


class SecurityMonitoringEntraIdAzureAppRegistrationsAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_azure_app_registration import (
            SecurityMonitoringAzureAppRegistration,
        )

        return {
            "azure_app_registrations": ([SecurityMonitoringAzureAppRegistration],),
            "has_valid_prerequisite": (bool,),
            "integration_id": (str,),
            "is_enabled": (bool,),
            "subscribed_at": (datetime,),
        }

    attribute_map = {
        "azure_app_registrations": "azure_app_registrations",
        "has_valid_prerequisite": "has_valid_prerequisite",
        "integration_id": "integration_id",
        "is_enabled": "is_enabled",
        "subscribed_at": "subscribed_at",
    }

    def __init__(
        self_,
        azure_app_registrations: List[SecurityMonitoringAzureAppRegistration],
        has_valid_prerequisite: bool,
        integration_id: Union[str, UnsetType] = unset,
        is_enabled: Union[bool, UnsetType] = unset,
        subscribed_at: Union[datetime, UnsetType] = unset,
        **kwargs,
    ):
        """
        The attributes of the Entra ID Azure App Registration prerequisites.

        :param azure_app_registrations: The Azure App Registrations discovered for the organization.
        :type azure_app_registrations: [SecurityMonitoringAzureAppRegistration]

        :param has_valid_prerequisite: Whether at least one Azure App Registration has resource collection enabled.
        :type has_valid_prerequisite: bool

        :param integration_id: The ID of the Entra ID integration configuration, if one exists.
        :type integration_id: str, optional

        :param is_enabled: Whether the Entra ID integration configuration is enabled, if one exists.
        :type is_enabled: bool, optional

        :param subscribed_at: The time at which the Entra ID integration configuration was created, if one exists.
        :type subscribed_at: datetime, optional
        """
        if integration_id is not unset:
            kwargs["integration_id"] = integration_id
        if is_enabled is not unset:
            kwargs["is_enabled"] = is_enabled
        if subscribed_at is not unset:
            kwargs["subscribed_at"] = subscribed_at
        super().__init__(kwargs)

        self_.azure_app_registrations = azure_app_registrations
        self_.has_valid_prerequisite = has_valid_prerequisite
