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
    from datadog_api_client.v2.model.elastic_cloud_interface_update import ElasticCloudInterfaceUpdate
    from datadog_api_client.v2.model.elastic_cloud_integration_type import ElasticCloudIntegrationType
    from datadog_api_client.v2.model.elastic_cloud_monitoring_interface_update import (
        ElasticCloudMonitoringInterfaceUpdate,
    )
    from datadog_api_client.v2.model.elastic_cloud_ccm_interface_update import ElasticCloudCcmInterfaceUpdate


class ElasticCloudIntegrationUpdate(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.elastic_cloud_interface_update import ElasticCloudInterfaceUpdate
        from datadog_api_client.v2.model.elastic_cloud_integration_type import ElasticCloudIntegrationType

        return {
            "interface": (ElasticCloudInterfaceUpdate,),
            "type": (ElasticCloudIntegrationType,),
        }

    attribute_map = {
        "interface": "interface",
        "type": "type",
    }

    def __init__(
        self_,
        type: ElasticCloudIntegrationType,
        interface: Union[
            ElasticCloudInterfaceUpdate,
            ElasticCloudMonitoringInterfaceUpdate,
            ElasticCloudCcmInterfaceUpdate,
            UnsetType,
        ] = unset,
        **kwargs,
    ):
        """
        Partial Elastic Cloud integration configuration for updates.

        :param interface: Partial Elastic Cloud interface for updates. Exactly one interface variant is set, selected by its ``type``.
        :type interface: ElasticCloudInterfaceUpdate, optional

        :param type: Integration discriminator for Elastic Cloud.
        :type type: ElasticCloudIntegrationType
        """
        if interface is not unset:
            kwargs["interface"] = interface
        super().__init__(kwargs)

        self_.type = type
