# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.elastic_cloud_authentication import ElasticCloudAuthentication
    from datadog_api_client.v2.model.elastic_cloud_dataflow import ElasticCloudDataflow
    from datadog_api_client.v2.model.integration_account_permissions import IntegrationAccountPermissions
    from datadog_api_client.v2.model.elastic_cloud_settings import ElasticCloudSettings
    from datadog_api_client.v2.model.elastic_cloud_basic_auth import ElasticCloudBasicAuth


class ElasticCloudMonitoringAccountAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.elastic_cloud_authentication import ElasticCloudAuthentication
        from datadog_api_client.v2.model.elastic_cloud_dataflow import ElasticCloudDataflow
        from datadog_api_client.v2.model.integration_account_permissions import IntegrationAccountPermissions
        from datadog_api_client.v2.model.elastic_cloud_settings import ElasticCloudSettings

        return {
            "authentication": (ElasticCloudAuthentication,),
            "dataflows": ([ElasticCloudDataflow],),
            "name": (str,),
            "permissions": (IntegrationAccountPermissions,),
            "settings": (ElasticCloudSettings,),
        }

    attribute_map = {
        "authentication": "authentication",
        "dataflows": "dataflows",
        "name": "name",
        "permissions": "permissions",
        "settings": "settings",
    }
    read_only_vars = {
        "permissions",
    }

    def __init__(
        self_,
        authentication: Union[ElasticCloudAuthentication, ElasticCloudBasicAuth],
        name: str,
        dataflows: Union[List[ElasticCloudDataflow], UnsetType] = unset,
        permissions: Union[IntegrationAccountPermissions, UnsetType] = unset,
        settings: Union[ElasticCloudSettings, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of an Elastic Cloud monitoring account. The configuration is hoisted directly onto the attributes; there is no interface wrapper because the ``elastic-cloud`` interface is fixed by the endpoint path.

        :param authentication: Authentication methods supported by the Elastic Cloud monitoring interface. Exactly one is set, selected by its ``type``.
        :type authentication: ElasticCloudAuthentication

        :param dataflows: Dataflows for the Elastic Cloud monitoring interface.
        :type dataflows: [ElasticCloudDataflow], optional

        :param name: Human-readable name of the account.
        :type name: str

        :param permissions: Read-only permission information for the account, derived from its restriction policy.
        :type permissions: IntegrationAccountPermissions, optional

        :param settings: Elastic Cloud monitoring interface settings.
        :type settings: ElasticCloudSettings, optional
        """
        if dataflows is not unset:
            kwargs["dataflows"] = dataflows
        if permissions is not unset:
            kwargs["permissions"] = permissions
        if settings is not unset:
            kwargs["settings"] = settings
        super().__init__(kwargs)

        self_.authentication = authentication
        self_.name = name
