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
    from datadog_api_client.v2.model.nebius_cloud_cost_collection_integration_dataflow_settings_request import (
        NebiusCloudCostCollectionIntegrationDataflowSettingsRequest,
    )


class NebiusCloudCostCollectionIntegrationDataflowRequest(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.nebius_cloud_cost_collection_integration_dataflow_settings_request import (
            NebiusCloudCostCollectionIntegrationDataflowSettingsRequest,
        )

        return {
            "enabled": (bool,),
            "settings": (NebiusCloudCostCollectionIntegrationDataflowSettingsRequest,),
        }

    attribute_map = {
        "enabled": "enabled",
        "settings": "settings",
    }

    def __init__(
        self_,
        enabled: Union[bool, UnsetType] = unset,
        settings: Union[NebiusCloudCostCollectionIntegrationDataflowSettingsRequest, UnsetType] = unset,
        **kwargs,
    ):
        """
        Cloud cost data read from a Nebius Object Storage bucket export and used by `Cloud Cost Management <https://docs.datadoghq.com/cloud_cost_management/>`_. Enabling it requires a bucket holding your cost export and a Nebius access key pair that can read it; a request that enables this dataflow without them is rejected with a ``422`` response.

        :param enabled: Whether Datadog collects this data. Defaults to ``false`` ; set to ``true`` to start collection.
        :type enabled: bool, optional

        :param settings: Settings of the Cloud Cost Management dataflow. Only the fields provided are changed.
        :type settings: NebiusCloudCostCollectionIntegrationDataflowSettingsRequest, optional
        """
        if enabled is not unset:
            kwargs["enabled"] = enabled
        if settings is not unset:
            kwargs["settings"] = settings
        super().__init__(kwargs)
