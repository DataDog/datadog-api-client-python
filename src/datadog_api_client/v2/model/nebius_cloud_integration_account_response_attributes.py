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
    from datadog_api_client.v2.model.nebius_cloud_integration_account_authentication_response import (
        NebiusCloudIntegrationAccountAuthenticationResponse,
    )
    from datadog_api_client.v2.model.nebius_cloud_integration_dataflows_response import (
        NebiusCloudIntegrationDataflowsResponse,
    )
    from datadog_api_client.v2.model.nebius_cloud_integration_account_settings_response import (
        NebiusCloudIntegrationAccountSettingsResponse,
    )
    from datadog_api_client.v2.model.nebius_cloud_integration_account_service_account_auth_response import (
        NebiusCloudIntegrationAccountServiceAccountAuthResponse,
    )


class NebiusCloudIntegrationAccountResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.nebius_cloud_integration_account_authentication_response import (
            NebiusCloudIntegrationAccountAuthenticationResponse,
        )
        from datadog_api_client.v2.model.nebius_cloud_integration_dataflows_response import (
            NebiusCloudIntegrationDataflowsResponse,
        )
        from datadog_api_client.v2.model.nebius_cloud_integration_account_settings_response import (
            NebiusCloudIntegrationAccountSettingsResponse,
        )

        return {
            "authentication": (NebiusCloudIntegrationAccountAuthenticationResponse,),
            "dataflows": (NebiusCloudIntegrationDataflowsResponse,),
            "name": (str,),
            "settings": (NebiusCloudIntegrationAccountSettingsResponse,),
        }

    attribute_map = {
        "authentication": "authentication",
        "dataflows": "dataflows",
        "name": "name",
        "settings": "settings",
    }

    def __init__(
        self_,
        name: str,
        settings: NebiusCloudIntegrationAccountSettingsResponse,
        authentication: Union[
            NebiusCloudIntegrationAccountAuthenticationResponse,
            NebiusCloudIntegrationAccountServiceAccountAuthResponse,
            UnsetType,
        ] = unset,
        dataflows: Union[NebiusCloudIntegrationDataflowsResponse, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of a Nebius Cloud integration account returned in responses.

        :param authentication: Authentication configured on the Nebius Cloud integration account.
        :type authentication: NebiusCloudIntegrationAccountAuthenticationResponse, optional

        :param dataflows: Data Datadog collects from Nebius Cloud, keyed by dataflow id.
        :type dataflows: NebiusCloudIntegrationDataflowsResponse, optional

        :param name: Human-readable name of the Nebius Cloud integration account.
        :type name: str

        :param settings: Settings configured on the Nebius Cloud integration account.
        :type settings: NebiusCloudIntegrationAccountSettingsResponse
        """
        if authentication is not unset:
            kwargs["authentication"] = authentication
        if dataflows is not unset:
            kwargs["dataflows"] = dataflows
        super().__init__(kwargs)

        self_.name = name
        self_.settings = settings
