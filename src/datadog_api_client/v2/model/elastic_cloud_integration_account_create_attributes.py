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
    from datadog_api_client.v2.model.elastic_cloud_integration_account_authentication_request import (
        ElasticCloudIntegrationAccountAuthenticationRequest,
    )
    from datadog_api_client.v2.model.elastic_cloud_integration_dataflows_request import (
        ElasticCloudIntegrationDataflowsRequest,
    )
    from datadog_api_client.v2.model.elastic_cloud_integration_account_settings_request import (
        ElasticCloudIntegrationAccountSettingsRequest,
    )
    from datadog_api_client.v2.model.integration_account_basic_auth_request import IntegrationAccountBasicAuthRequest


class ElasticCloudIntegrationAccountCreateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.elastic_cloud_integration_account_authentication_request import (
            ElasticCloudIntegrationAccountAuthenticationRequest,
        )
        from datadog_api_client.v2.model.elastic_cloud_integration_dataflows_request import (
            ElasticCloudIntegrationDataflowsRequest,
        )
        from datadog_api_client.v2.model.elastic_cloud_integration_account_settings_request import (
            ElasticCloudIntegrationAccountSettingsRequest,
        )

        return {
            "authentication": (ElasticCloudIntegrationAccountAuthenticationRequest,),
            "dataflows": (ElasticCloudIntegrationDataflowsRequest,),
            "name": (str,),
            "settings": (ElasticCloudIntegrationAccountSettingsRequest,),
        }

    attribute_map = {
        "authentication": "authentication",
        "dataflows": "dataflows",
        "name": "name",
        "settings": "settings",
    }

    def __init__(
        self_,
        authentication: Union[ElasticCloudIntegrationAccountAuthenticationRequest, IntegrationAccountBasicAuthRequest],
        name: str,
        settings: ElasticCloudIntegrationAccountSettingsRequest,
        dataflows: Union[ElasticCloudIntegrationDataflowsRequest, UnsetType] = unset,
        **kwargs,
    ):
        """
        Writable attributes used to create an Elastic Cloud integration account.

        :param authentication: Authentication for creating the Elastic Cloud integration account. Exactly one method is set.
        :type authentication: ElasticCloudIntegrationAccountAuthenticationRequest

        :param dataflows: Dataflows to configure on the Elastic Cloud integration account, keyed by dataflow id.
        :type dataflows: ElasticCloudIntegrationDataflowsRequest, optional

        :param name: Human-readable name of the Elastic Cloud integration account.
        :type name: str

        :param settings: Settings for creating the Elastic Cloud integration account.
        :type settings: ElasticCloudIntegrationAccountSettingsRequest
        """
        if dataflows is not unset:
            kwargs["dataflows"] = dataflows
        super().__init__(kwargs)

        self_.authentication = authentication
        self_.name = name
        self_.settings = settings
