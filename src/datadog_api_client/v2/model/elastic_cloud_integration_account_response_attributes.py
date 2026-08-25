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
    from datadog_api_client.v2.model.elastic_cloud_integration_account_authentication_response import (
        ElasticCloudIntegrationAccountAuthenticationResponse,
    )
    from datadog_api_client.v2.model.elastic_cloud_integration_dataflows_response import (
        ElasticCloudIntegrationDataflowsResponse,
    )
    from datadog_api_client.v2.model.elastic_cloud_integration_account_settings_response import (
        ElasticCloudIntegrationAccountSettingsResponse,
    )
    from datadog_api_client.v2.model.integration_account_basic_auth_response import IntegrationAccountBasicAuthResponse


class ElasticCloudIntegrationAccountResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.elastic_cloud_integration_account_authentication_response import (
            ElasticCloudIntegrationAccountAuthenticationResponse,
        )
        from datadog_api_client.v2.model.elastic_cloud_integration_dataflows_response import (
            ElasticCloudIntegrationDataflowsResponse,
        )
        from datadog_api_client.v2.model.elastic_cloud_integration_account_settings_response import (
            ElasticCloudIntegrationAccountSettingsResponse,
        )

        return {
            "authentication": (ElasticCloudIntegrationAccountAuthenticationResponse,),
            "dataflows": (ElasticCloudIntegrationDataflowsResponse,),
            "name": (str,),
            "settings": (ElasticCloudIntegrationAccountSettingsResponse,),
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
        settings: ElasticCloudIntegrationAccountSettingsResponse,
        authentication: Union[
            ElasticCloudIntegrationAccountAuthenticationResponse, IntegrationAccountBasicAuthResponse, UnsetType
        ] = unset,
        dataflows: Union[ElasticCloudIntegrationDataflowsResponse, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of an Elastic Cloud integration account returned in responses.

        :param authentication: Authentication configured on the Elastic Cloud integration account.
        :type authentication: ElasticCloudIntegrationAccountAuthenticationResponse, optional

        :param dataflows: Dataflows configured on the Elastic Cloud integration account, keyed by dataflow id.
        :type dataflows: ElasticCloudIntegrationDataflowsResponse, optional

        :param name: Human-readable name of the Elastic Cloud integration account.
        :type name: str

        :param settings: Settings configured on the Elastic Cloud integration account.
        :type settings: ElasticCloudIntegrationAccountSettingsResponse
        """
        if authentication is not unset:
            kwargs["authentication"] = authentication
        if dataflows is not unset:
            kwargs["dataflows"] = dataflows
        super().__init__(kwargs)

        self_.name = name
        self_.settings = settings
