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
    from datadog_api_client.v2.model.snowflake_cloud_cost_metrics_integration_dataflow_settings_request import (
        SnowflakeCloudCostMetricsIntegrationDataflowSettingsRequest,
    )


class SnowflakeCloudCostMetricsIntegrationDataflowRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.snowflake_cloud_cost_metrics_integration_dataflow_settings_request import (
            SnowflakeCloudCostMetricsIntegrationDataflowSettingsRequest,
        )

        return {
            "enabled": (bool,),
            "settings": (SnowflakeCloudCostMetricsIntegrationDataflowSettingsRequest,),
        }

    attribute_map = {
        "enabled": "enabled",
        "settings": "settings",
    }

    def __init__(
        self_,
        enabled: Union[bool, UnsetType] = unset,
        settings: Union[SnowflakeCloudCostMetricsIntegrationDataflowSettingsRequest, UnsetType] = unset,
        **kwargs,
    ):
        """
        Cost data aggregated from the Snowflake ``ORGANIZATION_USAGE`` schema. `Cloud Cost Management <https://docs.datadoghq.com/cloud_cost_management/>`_ must be enabled for your organization while this dataflow is enabled. Any request that enables this dataflow without Cloud Cost Management is rejected with a ``422`` response. The Snowflake role also needs the ORGANIZATION_BILLING_VIEWER database role to read the underlying cost views.

        :param enabled: Whether Datadog collects this data. Defaults to ``false`` ; set to ``true`` to start collection.
        :type enabled: bool, optional

        :param settings: Settings of the Cloud Cost Management dataflow. Only the fields provided are changed.
        :type settings: SnowflakeCloudCostMetricsIntegrationDataflowSettingsRequest, optional
        """
        if enabled is not unset:
            kwargs["enabled"] = enabled
        if settings is not unset:
            kwargs["settings"] = settings
        super().__init__(kwargs)
