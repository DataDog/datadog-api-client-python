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
    from datadog_api_client.v2.model.nebius_cloud_integration_account_authentication_update import (
        NebiusCloudIntegrationAccountAuthenticationUpdate,
    )
    from datadog_api_client.v2.model.nebius_cloud_integration_dataflows_request import (
        NebiusCloudIntegrationDataflowsRequest,
    )
    from datadog_api_client.v2.model.nebius_cloud_integration_account_settings_update import (
        NebiusCloudIntegrationAccountSettingsUpdate,
    )
    from datadog_api_client.v2.model.nebius_cloud_integration_account_service_account_auth_update import (
        NebiusCloudIntegrationAccountServiceAccountAuthUpdate,
    )


class NebiusCloudIntegrationAccountUpdateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.nebius_cloud_integration_account_authentication_update import (
            NebiusCloudIntegrationAccountAuthenticationUpdate,
        )
        from datadog_api_client.v2.model.nebius_cloud_integration_dataflows_request import (
            NebiusCloudIntegrationDataflowsRequest,
        )
        from datadog_api_client.v2.model.nebius_cloud_integration_account_settings_update import (
            NebiusCloudIntegrationAccountSettingsUpdate,
        )

        return {
            "authentication": (NebiusCloudIntegrationAccountAuthenticationUpdate,),
            "dataflows": (NebiusCloudIntegrationDataflowsRequest,),
            "name": (str,),
            "settings": (NebiusCloudIntegrationAccountSettingsUpdate,),
        }

    attribute_map = {
        "authentication": "authentication",
        "dataflows": "dataflows",
        "name": "name",
        "settings": "settings",
    }

    def __init__(
        self_,
        authentication: Union[
            NebiusCloudIntegrationAccountAuthenticationUpdate,
            NebiusCloudIntegrationAccountServiceAccountAuthUpdate,
            UnsetType,
        ] = unset,
        dataflows: Union[NebiusCloudIntegrationDataflowsRequest, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        settings: Union[NebiusCloudIntegrationAccountSettingsUpdate, UnsetType] = unset,
        **kwargs,
    ):
        """
        Writable attributes used to update a Nebius Cloud integration account. Every field is optional; only the fields provided are changed. When ``dataflows`` is provided, only the dataflow ids included in the request are modified; dataflows omitted from the map keep their current configuration, as do the settings of an included dataflow that provides only ``enabled``.

        :param authentication: Authentication for updating the Nebius Cloud integration account. Exactly one method is set.
        :type authentication: NebiusCloudIntegrationAccountAuthenticationUpdate, optional

        :param dataflows: Data Datadog collects from Nebius Cloud, keyed by dataflow id. Each dataflow turns on a distinct kind of collection: set ``enabled`` to stop or start it, and use ``settings`` to configure what it collects. Defaults listed on each dataflow apply when the account is created; on update, omitted fields keep their current values. Every dataflow except ``nebius-cloud-cost-collection`` runs as the service account in ``authentication`` , using its authorized key pair and the static API key; enabling one of them without those keys is rejected with a ``422`` response, and one enabled with keys that later expire is stored but collects no data.
        :type dataflows: NebiusCloudIntegrationDataflowsRequest, optional

        :param name: Human-readable name of the Nebius Cloud integration account.
        :type name: str, optional

        :param settings: Settings for updating the Nebius Cloud integration account. Only the fields provided are changed.
        :type settings: NebiusCloudIntegrationAccountSettingsUpdate, optional
        """
        if authentication is not unset:
            kwargs["authentication"] = authentication
        if dataflows is not unset:
            kwargs["dataflows"] = dataflows
        if name is not unset:
            kwargs["name"] = name
        if settings is not unset:
            kwargs["settings"] = settings
        super().__init__(kwargs)
