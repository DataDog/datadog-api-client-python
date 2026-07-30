# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.elastic_cloud_interface import ElasticCloudInterface
    from datadog_api_client.v2.model.elastic_cloud_integration_type import ElasticCloudIntegrationType
    from datadog_api_client.v2.model.elastic_cloud_monitoring_interface import ElasticCloudMonitoringInterface
    from datadog_api_client.v2.model.elastic_cloud_ccm_interface import ElasticCloudCcmInterface


class ElasticCloudIntegration(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.elastic_cloud_interface import ElasticCloudInterface
        from datadog_api_client.v2.model.elastic_cloud_integration_type import ElasticCloudIntegrationType

        return {
            "interface": (ElasticCloudInterface,),
            "type": (ElasticCloudIntegrationType,),
        }

    attribute_map = {
        "interface": "interface",
        "type": "type",
    }

    def __init__(
        self_,
        interface: Union[ElasticCloudInterface, ElasticCloudMonitoringInterface, ElasticCloudCcmInterface],
        type: ElasticCloudIntegrationType,
        **kwargs,
    ):
        """
        Elastic Cloud integration configuration.

        :param interface: Elastic Cloud interface (source-type). Exactly one interface variant is set, selected by its ``type``.
        :type interface: ElasticCloudInterface

        :param type: Integration discriminator for Elastic Cloud.
        :type type: ElasticCloudIntegrationType
        """
        super().__init__(kwargs)

        self_.interface = interface
        self_.type = type
