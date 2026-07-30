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
    from datadog_api_client.v2.model.elastic_cloud_settings import ElasticCloudSettings
    from datadog_api_client.v2.model.elastic_cloud_monitoring_interface_type import ElasticCloudMonitoringInterfaceType
    from datadog_api_client.v2.model.elastic_cloud_basic_auth import ElasticCloudBasicAuth


class ElasticCloudMonitoringInterface(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.elastic_cloud_authentication import ElasticCloudAuthentication
        from datadog_api_client.v2.model.elastic_cloud_dataflow import ElasticCloudDataflow
        from datadog_api_client.v2.model.elastic_cloud_settings import ElasticCloudSettings
        from datadog_api_client.v2.model.elastic_cloud_monitoring_interface_type import (
            ElasticCloudMonitoringInterfaceType,
        )

        return {
            "authentication": (ElasticCloudAuthentication,),
            "dataflows": ([ElasticCloudDataflow],),
            "settings": (ElasticCloudSettings,),
            "type": (ElasticCloudMonitoringInterfaceType,),
        }

    attribute_map = {
        "authentication": "authentication",
        "dataflows": "dataflows",
        "settings": "settings",
        "type": "type",
    }

    def __init__(
        self_,
        authentication: Union[ElasticCloudAuthentication, ElasticCloudBasicAuth],
        type: ElasticCloudMonitoringInterfaceType,
        dataflows: Union[List[ElasticCloudDataflow], UnsetType] = unset,
        settings: Union[ElasticCloudSettings, UnsetType] = unset,
        **kwargs,
    ):
        """
        Elastic Cloud monitoring interface (source-type) configuration.

        :param authentication: Authentication methods supported by the Elastic Cloud interface. Exactly one is set, selected by its ``type``.
        :type authentication: ElasticCloudAuthentication

        :param dataflows: Dataflows for the Elastic Cloud monitoring interface.
        :type dataflows: [ElasticCloudDataflow], optional

        :param settings: Elastic Cloud interface settings.
        :type settings: ElasticCloudSettings, optional

        :param type: Interface discriminator for the Elastic Cloud monitoring interface.
        :type type: ElasticCloudMonitoringInterfaceType
        """
        if dataflows is not unset:
            kwargs["dataflows"] = dataflows
        if settings is not unset:
            kwargs["settings"] = settings
        super().__init__(kwargs)

        self_.authentication = authentication
        self_.type = type
