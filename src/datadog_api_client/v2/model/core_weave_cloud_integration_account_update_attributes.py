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
    from datadog_api_client.v2.model.core_weave_cloud_integration_account_authentication_update import (
        CoreWeaveCloudIntegrationAccountAuthenticationUpdate,
    )
    from datadog_api_client.v2.model.core_weave_cloud_integration_dataflows_request import (
        CoreWeaveCloudIntegrationDataflowsRequest,
    )
    from datadog_api_client.v2.model.core_weave_cloud_integration_account_settings_update import (
        CoreWeaveCloudIntegrationAccountSettingsUpdate,
    )
    from datadog_api_client.v2.model.core_weave_cloud_integration_account_api_token_auth_update import (
        CoreWeaveCloudIntegrationAccountAPITokenAuthUpdate,
    )


class CoreWeaveCloudIntegrationAccountUpdateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.core_weave_cloud_integration_account_authentication_update import (
            CoreWeaveCloudIntegrationAccountAuthenticationUpdate,
        )
        from datadog_api_client.v2.model.core_weave_cloud_integration_dataflows_request import (
            CoreWeaveCloudIntegrationDataflowsRequest,
        )
        from datadog_api_client.v2.model.core_weave_cloud_integration_account_settings_update import (
            CoreWeaveCloudIntegrationAccountSettingsUpdate,
        )

        return {
            "authentication": (CoreWeaveCloudIntegrationAccountAuthenticationUpdate,),
            "dataflows": (CoreWeaveCloudIntegrationDataflowsRequest,),
            "name": (str,),
            "settings": (CoreWeaveCloudIntegrationAccountSettingsUpdate,),
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
            CoreWeaveCloudIntegrationAccountAuthenticationUpdate,
            CoreWeaveCloudIntegrationAccountAPITokenAuthUpdate,
            UnsetType,
        ] = unset,
        dataflows: Union[CoreWeaveCloudIntegrationDataflowsRequest, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        settings: Union[CoreWeaveCloudIntegrationAccountSettingsUpdate, UnsetType] = unset,
        **kwargs,
    ):
        """
        Writable attributes used to update a CoreWeave integration account. Every field is optional; only the fields provided are changed. When ``dataflows`` is provided, only the dataflow ids included in the request are modified; dataflows omitted from the map keep their current configuration.

        :param authentication: Authentication for updating the CoreWeave integration account. Exactly one method is set.
        :type authentication: CoreWeaveCloudIntegrationAccountAuthenticationUpdate, optional

        :param dataflows: Data Datadog collects from CoreWeave, keyed by dataflow id. Each dataflow turns on a distinct kind of collection: set ``enabled`` to start or stop it. Defaults listed on each dataflow apply when the account is created; on update, omitted dataflow ids keep their current values. Collection runs with the API access token in ``authentication`` , whose user must have the Observability Viewer role; a dataflow enabled without that role is stored but collects no data.
        :type dataflows: CoreWeaveCloudIntegrationDataflowsRequest, optional

        :param name: Human-readable name of the CoreWeave integration account.
        :type name: str, optional

        :param settings: Settings for updating the CoreWeave integration account. Only the fields provided are changed.
        :type settings: CoreWeaveCloudIntegrationAccountSettingsUpdate, optional
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
