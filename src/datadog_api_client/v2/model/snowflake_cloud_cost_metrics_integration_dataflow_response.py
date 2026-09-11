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
    from datadog_api_client.v2.model.snowflake_cloud_cost_metrics_integration_dataflow_settings_response import (
        SnowflakeCloudCostMetricsIntegrationDataflowSettingsResponse,
    )


class SnowflakeCloudCostMetricsIntegrationDataflowResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.snowflake_cloud_cost_metrics_integration_dataflow_settings_response import (
            SnowflakeCloudCostMetricsIntegrationDataflowSettingsResponse,
        )

        return {
            "enabled": (bool,),
            "settings": (SnowflakeCloudCostMetricsIntegrationDataflowSettingsResponse,),
        }

    attribute_map = {
        "enabled": "enabled",
        "settings": "settings",
    }

    def __init__(
        self_,
        enabled: Union[bool, UnsetType] = unset,
        settings: Union[SnowflakeCloudCostMetricsIntegrationDataflowSettingsResponse, UnsetType] = unset,
        **kwargs,
    ):
        """
        Cost data aggregated from the Snowflake ``ORGANIZATION_USAGE`` schema. Requires `Cloud Cost Management <https://docs.datadoghq.com/cloud_cost_management/>`_ to be set up for your organization, and the ORGANIZATION_BILLING_VIEWER database role on the Snowflake role.

        :param enabled: Whether Datadog collects this data.
        :type enabled: bool, optional

        :param settings: Settings of the Cloud Cost Management dataflow.
        :type settings: SnowflakeCloudCostMetricsIntegrationDataflowSettingsResponse, optional
        """
        if enabled is not unset:
            kwargs["enabled"] = enabled
        if settings is not unset:
            kwargs["settings"] = settings
        super().__init__(kwargs)
