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
    from datadog_api_client.v2.model.elastic_cloud_settings_update import ElasticCloudSettingsUpdate
    from datadog_api_client.v2.model.elastic_cloud_basic_auth import ElasticCloudBasicAuth


class ElasticCloudMonitoringAccountUpdateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.elastic_cloud_authentication import ElasticCloudAuthentication
        from datadog_api_client.v2.model.elastic_cloud_dataflow import ElasticCloudDataflow
        from datadog_api_client.v2.model.elastic_cloud_settings_update import ElasticCloudSettingsUpdate

        return {
            "authentication": (ElasticCloudAuthentication,),
            "dataflows": ([ElasticCloudDataflow],),
            "name": (str,),
            "settings": (ElasticCloudSettingsUpdate,),
        }

    attribute_map = {
        "authentication": "authentication",
        "dataflows": "dataflows",
        "name": "name",
        "settings": "settings",
    }

    def __init__(
        self_,
        authentication: Union[ElasticCloudAuthentication, ElasticCloudBasicAuth, UnsetType] = unset,
        dataflows: Union[List[ElasticCloudDataflow], UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        settings: Union[ElasticCloudSettingsUpdate, UnsetType] = unset,
        **kwargs,
    ):
        """
        Updatable attributes of an Elastic Cloud monitoring account. Every field is optional; only the fields provided are changed.

        :param authentication: Authentication methods supported by the Elastic Cloud monitoring interface. Exactly one is set, selected by its ``type``.
        :type authentication: ElasticCloudAuthentication, optional

        :param dataflows: Dataflows for the Elastic Cloud monitoring interface.
        :type dataflows: [ElasticCloudDataflow], optional

        :param name: Human-readable name of the account.
        :type name: str, optional

        :param settings: Partial Elastic Cloud monitoring interface settings for updates.
        :type settings: ElasticCloudSettingsUpdate, optional
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
