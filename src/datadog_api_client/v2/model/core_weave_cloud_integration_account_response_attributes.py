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
    from datadog_api_client.v2.model.core_weave_cloud_integration_account_authentication_response import (
        CoreWeaveCloudIntegrationAccountAuthenticationResponse,
    )
    from datadog_api_client.v2.model.core_weave_cloud_integration_dataflows_response import (
        CoreWeaveCloudIntegrationDataflowsResponse,
    )
    from datadog_api_client.v2.model.core_weave_cloud_integration_account_settings_response import (
        CoreWeaveCloudIntegrationAccountSettingsResponse,
    )
    from datadog_api_client.v2.model.core_weave_cloud_integration_account_api_token_auth_response import (
        CoreWeaveCloudIntegrationAccountAPITokenAuthResponse,
    )


class CoreWeaveCloudIntegrationAccountResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.core_weave_cloud_integration_account_authentication_response import (
            CoreWeaveCloudIntegrationAccountAuthenticationResponse,
        )
        from datadog_api_client.v2.model.core_weave_cloud_integration_dataflows_response import (
            CoreWeaveCloudIntegrationDataflowsResponse,
        )
        from datadog_api_client.v2.model.core_weave_cloud_integration_account_settings_response import (
            CoreWeaveCloudIntegrationAccountSettingsResponse,
        )

        return {
            "authentication": (CoreWeaveCloudIntegrationAccountAuthenticationResponse,),
            "dataflows": (CoreWeaveCloudIntegrationDataflowsResponse,),
            "name": (str,),
            "settings": (CoreWeaveCloudIntegrationAccountSettingsResponse,),
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
        settings: CoreWeaveCloudIntegrationAccountSettingsResponse,
        authentication: Union[
            CoreWeaveCloudIntegrationAccountAuthenticationResponse,
            CoreWeaveCloudIntegrationAccountAPITokenAuthResponse,
            UnsetType,
        ] = unset,
        dataflows: Union[CoreWeaveCloudIntegrationDataflowsResponse, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of a CoreWeave integration account returned in responses.

        :param authentication: Authentication configured on the CoreWeave integration account.
        :type authentication: CoreWeaveCloudIntegrationAccountAuthenticationResponse, optional

        :param dataflows: Data Datadog collects from CoreWeave, keyed by dataflow id.
        :type dataflows: CoreWeaveCloudIntegrationDataflowsResponse, optional

        :param name: Human-readable name of the CoreWeave integration account.
        :type name: str

        :param settings: Settings configured on the CoreWeave integration account.
        :type settings: CoreWeaveCloudIntegrationAccountSettingsResponse
        """
        if authentication is not unset:
            kwargs["authentication"] = authentication
        if dataflows is not unset:
            kwargs["dataflows"] = dataflows
        super().__init__(kwargs)

        self_.name = name
        self_.settings = settings
