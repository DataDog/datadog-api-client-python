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
    from datadog_api_client.v2.model.snowflake_data_observability_quality_monitoring_integration_dataflow_settings_request import (
        SnowflakeDataObservabilityQualityMonitoringIntegrationDataflowSettingsRequest,
    )


class SnowflakeDataObservabilityQualityMonitoringIntegrationDataflowRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.snowflake_data_observability_quality_monitoring_integration_dataflow_settings_request import (
            SnowflakeDataObservabilityQualityMonitoringIntegrationDataflowSettingsRequest,
        )

        return {
            "enabled": (bool,),
            "settings": (SnowflakeDataObservabilityQualityMonitoringIntegrationDataflowSettingsRequest,),
        }

    attribute_map = {
        "enabled": "enabled",
        "settings": "settings",
    }

    def __init__(
        self_,
        enabled: Union[bool, UnsetType] = unset,
        settings: Union[
            SnowflakeDataObservabilityQualityMonitoringIntegrationDataflowSettingsRequest, UnsetType
        ] = unset,
        **kwargs,
    ):
        """
        Data Observability, which collects lineage and data quality information from your Snowflake databases so you can explore how data flows and detect and resolve quality issues.

        :param enabled: Whether Datadog collects this data. Defaults to ``false`` ; set to ``true`` to start collection.
        :type enabled: bool, optional

        :param settings: Settings of the Data Observability dataflow. Only the fields provided are changed.
        :type settings: SnowflakeDataObservabilityQualityMonitoringIntegrationDataflowSettingsRequest, optional
        """
        if enabled is not unset:
            kwargs["enabled"] = enabled
        if settings is not unset:
            kwargs["settings"] = settings
        super().__init__(kwargs)
