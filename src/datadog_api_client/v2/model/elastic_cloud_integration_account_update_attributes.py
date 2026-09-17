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
    from datadog_api_client.v2.model.elastic_cloud_integration_account_authentication_update import (
        ElasticCloudIntegrationAccountAuthenticationUpdate,
    )
    from datadog_api_client.v2.model.elastic_cloud_integration_dataflows_request import (
        ElasticCloudIntegrationDataflowsRequest,
    )
    from datadog_api_client.v2.model.elastic_cloud_integration_account_settings_update import (
        ElasticCloudIntegrationAccountSettingsUpdate,
    )
    from datadog_api_client.v2.model.elastic_cloud_integration_account_basic_auth_update import (
        ElasticCloudIntegrationAccountBasicAuthUpdate,
    )


class ElasticCloudIntegrationAccountUpdateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.elastic_cloud_integration_account_authentication_update import (
            ElasticCloudIntegrationAccountAuthenticationUpdate,
        )
        from datadog_api_client.v2.model.elastic_cloud_integration_dataflows_request import (
            ElasticCloudIntegrationDataflowsRequest,
        )
        from datadog_api_client.v2.model.elastic_cloud_integration_account_settings_update import (
            ElasticCloudIntegrationAccountSettingsUpdate,
        )

        return {
            "authentication": (ElasticCloudIntegrationAccountAuthenticationUpdate,),
            "dataflows": (ElasticCloudIntegrationDataflowsRequest,),
            "name": (str,),
            "settings": (ElasticCloudIntegrationAccountSettingsUpdate,),
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
            ElasticCloudIntegrationAccountAuthenticationUpdate, ElasticCloudIntegrationAccountBasicAuthUpdate, UnsetType
        ] = unset,
        dataflows: Union[ElasticCloudIntegrationDataflowsRequest, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        settings: Union[ElasticCloudIntegrationAccountSettingsUpdate, UnsetType] = unset,
        **kwargs,
    ):
        """
        Writable attributes used to update an Elastic Cloud integration account. Every field is optional; only the fields provided are changed. When ``dataflows`` is provided, only the dataflow ids included in the request are modified; dataflows omitted from the map keep their current configuration.

        :param authentication: Authentication for updating the Elastic Cloud integration account. Exactly one method is set.
        :type authentication: ElasticCloudIntegrationAccountAuthenticationUpdate, optional

        :param dataflows: Data Datadog collects from Elastic Cloud, keyed by dataflow id. Node-level cluster statistics are always collected; each dataflow here adds a further set of metrics on top of that baseline, so set ``enabled`` to start or stop it. Defaults listed on each dataflow apply when the account is created; on update, omitted fields keep their current values. Every dataflow queries the deployment as the user in ``authentication`` , so that user's role must hold the required Elasticsearch privileges; a dataflow enabled without them is stored but collects no data.
        :type dataflows: ElasticCloudIntegrationDataflowsRequest, optional

        :param name: Human-readable name of the Elastic Cloud integration account.
        :type name: str, optional

        :param settings: Settings for updating the Elastic Cloud integration account. Only the fields provided are changed.
        :type settings: ElasticCloudIntegrationAccountSettingsUpdate, optional
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
