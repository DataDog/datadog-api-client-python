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
    from datadog_api_client.v2.model.core_weave_cloud_integration_account_authentication_request import (
        CoreWeaveCloudIntegrationAccountAuthenticationRequest,
    )
    from datadog_api_client.v2.model.core_weave_cloud_integration_dataflows_request import (
        CoreWeaveCloudIntegrationDataflowsRequest,
    )
    from datadog_api_client.v2.model.core_weave_cloud_integration_account_settings_request import (
        CoreWeaveCloudIntegrationAccountSettingsRequest,
    )
    from datadog_api_client.v2.model.core_weave_cloud_integration_account_api_token_auth_request import (
        CoreWeaveCloudIntegrationAccountAPITokenAuthRequest,
    )


class CoreWeaveCloudIntegrationAccountCreateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.core_weave_cloud_integration_account_authentication_request import (
            CoreWeaveCloudIntegrationAccountAuthenticationRequest,
        )
        from datadog_api_client.v2.model.core_weave_cloud_integration_dataflows_request import (
            CoreWeaveCloudIntegrationDataflowsRequest,
        )
        from datadog_api_client.v2.model.core_weave_cloud_integration_account_settings_request import (
            CoreWeaveCloudIntegrationAccountSettingsRequest,
        )

        return {
            "authentication": (CoreWeaveCloudIntegrationAccountAuthenticationRequest,),
            "dataflows": (CoreWeaveCloudIntegrationDataflowsRequest,),
            "name": (str,),
            "settings": (CoreWeaveCloudIntegrationAccountSettingsRequest,),
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
            CoreWeaveCloudIntegrationAccountAuthenticationRequest, CoreWeaveCloudIntegrationAccountAPITokenAuthRequest
        ],
        name: str,
        settings: CoreWeaveCloudIntegrationAccountSettingsRequest,
        dataflows: Union[CoreWeaveCloudIntegrationDataflowsRequest, UnsetType] = unset,
        **kwargs,
    ):
        """
        Writable attributes used to create a CoreWeave integration account.

        :param authentication: Authentication for creating the CoreWeave integration account. Exactly one method is set.
        :type authentication: CoreWeaveCloudIntegrationAccountAuthenticationRequest

        :param dataflows: Data Datadog collects from CoreWeave, keyed by dataflow id. Each dataflow turns on a distinct kind of collection: set ``enabled`` to start or stop it. Defaults listed on each dataflow apply when the account is created; on update, omitted dataflow ids keep their current values. Collection runs with the API access token in ``authentication`` , whose user must have the Observability Viewer role; a dataflow enabled without that role is stored but collects no data.
        :type dataflows: CoreWeaveCloudIntegrationDataflowsRequest, optional

        :param name: Human-readable name of the CoreWeave integration account.
        :type name: str

        :param settings: Settings for creating the CoreWeave integration account.
        :type settings: CoreWeaveCloudIntegrationAccountSettingsRequest
        """
        if dataflows is not unset:
            kwargs["dataflows"] = dataflows
        super().__init__(kwargs)

        self_.authentication = authentication
        self_.name = name
        self_.settings = settings
