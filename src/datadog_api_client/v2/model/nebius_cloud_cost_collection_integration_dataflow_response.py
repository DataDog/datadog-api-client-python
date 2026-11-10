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
    from datadog_api_client.v2.model.nebius_cloud_cost_collection_integration_dataflow_settings_response import (
        NebiusCloudCostCollectionIntegrationDataflowSettingsResponse,
    )


class NebiusCloudCostCollectionIntegrationDataflowResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.nebius_cloud_cost_collection_integration_dataflow_settings_response import (
            NebiusCloudCostCollectionIntegrationDataflowSettingsResponse,
        )

        return {
            "enabled": (bool,),
            "settings": (NebiusCloudCostCollectionIntegrationDataflowSettingsResponse,),
        }

    attribute_map = {
        "enabled": "enabled",
        "settings": "settings",
    }

    def __init__(
        self_,
        enabled: Union[bool, UnsetType] = unset,
        settings: Union[NebiusCloudCostCollectionIntegrationDataflowSettingsResponse, UnsetType] = unset,
        **kwargs,
    ):
        """
        Cloud cost data read from a Nebius Object Storage bucket export and used by `Cloud Cost Management <https://docs.datadoghq.com/cloud_cost_management/>`_. Requires a bucket holding your cost export and a Nebius access key pair that can read it; without both this dataflow collects no data.

        :param enabled: Whether Datadog collects this data. Absent when the dataflow has never been configured.
        :type enabled: bool, optional

        :param settings: Settings of the Cloud Cost Management dataflow.
        :type settings: NebiusCloudCostCollectionIntegrationDataflowSettingsResponse, optional
        """
        if enabled is not unset:
            kwargs["enabled"] = enabled
        if settings is not unset:
            kwargs["settings"] = settings
        super().__init__(kwargs)
