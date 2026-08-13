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
    from datadog_api_client.v2.model.elastic_cloud_monitoring_interface_update import (
        ElasticCloudMonitoringInterfaceUpdate,
    )
    from datadog_api_client.v2.model.elastic_cloud_ccm_interface_update import ElasticCloudCcmInterfaceUpdate


class ElasticCloudIntegrationAccountUpdateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.elastic_cloud_interface_update import ElasticCloudInterfaceUpdate

        return {
            "interface": (ElasticCloudInterfaceUpdate,),
            "name": (str,),
        }

    attribute_map = {
        "interface": "interface",
        "name": "name",
    }

    def __init__(
        self_,
        interface: Union[
            ElasticCloudInterfaceUpdate,
            ElasticCloudMonitoringInterfaceUpdate,
            ElasticCloudCcmInterfaceUpdate,
            UnsetType,
        ] = unset,
        name: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Updatable attributes of an Elastic Cloud integration account. Every field is optional; only the fields provided are changed.

        :param interface: Partial Elastic Cloud interface for updates. Exactly one interface variant is set, selected by its ``type``.
        :type interface: ElasticCloudInterfaceUpdate, optional

        :param name: Human-readable name of the account.
        :type name: str, optional
        """
        if interface is not unset:
            kwargs["interface"] = interface
        if name is not unset:
            kwargs["name"] = name
        super().__init__(kwargs)
