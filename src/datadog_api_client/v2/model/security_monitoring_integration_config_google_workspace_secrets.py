# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.security_monitoring_integration_config_google_workspace_service_account import (
        SecurityMonitoringIntegrationConfigGoogleWorkspaceServiceAccount,
    )


class SecurityMonitoringIntegrationConfigGoogleWorkspaceSecrets(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_integration_config_google_workspace_service_account import (
            SecurityMonitoringIntegrationConfigGoogleWorkspaceServiceAccount,
        )

        return {
            "admin_email": (str,),
            "service_account_json": (SecurityMonitoringIntegrationConfigGoogleWorkspaceServiceAccount,),
        }

    attribute_map = {
        "admin_email": "admin_email",
        "service_account_json": "service_account_json",
    }

    def __init__(
        self_,
        service_account_json: SecurityMonitoringIntegrationConfigGoogleWorkspaceServiceAccount,
        admin_email: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Credentials for a Google Workspace entity context sync.

        :param admin_email: The admin email to impersonate for domain-wide delegation.
        :type admin_email: str, optional

        :param service_account_json: The Google Cloud service account JSON used to authenticate against the Google Workspace Admin SDK. Additional keys beyond those documented are preserved.
        :type service_account_json: SecurityMonitoringIntegrationConfigGoogleWorkspaceServiceAccount
        """
        if admin_email is not unset:
            kwargs["admin_email"] = admin_email
        super().__init__(kwargs)

        self_.service_account_json = service_account_json
