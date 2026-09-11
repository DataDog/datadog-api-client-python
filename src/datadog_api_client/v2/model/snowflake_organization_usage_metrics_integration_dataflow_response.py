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
    from datadog_api_client.v2.model.snowflake_organization_usage_metrics_integration_dataflow_settings_response import (
        SnowflakeOrganizationUsageMetricsIntegrationDataflowSettingsResponse,
    )


class SnowflakeOrganizationUsageMetricsIntegrationDataflowResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.snowflake_organization_usage_metrics_integration_dataflow_settings_response import (
            SnowflakeOrganizationUsageMetricsIntegrationDataflowSettingsResponse,
        )

        return {
            "enabled": (bool,),
            "settings": (SnowflakeOrganizationUsageMetricsIntegrationDataflowSettingsResponse,),
        }

    attribute_map = {
        "enabled": "enabled",
        "settings": "settings",
    }

    def __init__(
        self_,
        enabled: Union[bool, UnsetType] = unset,
        settings: Union[SnowflakeOrganizationUsageMetricsIntegrationDataflowSettingsResponse, UnsetType] = unset,
        **kwargs,
    ):
        """
        Organization-level usage metrics read from the Snowflake ``ORGANIZATION_USAGE`` schema, covering the credit consumption of every account in the organization and the history of data transferred out of Snowflake. Reading that schema requires the ORGADMIN role.

        :param enabled: Whether Datadog collects this data.
        :type enabled: bool, optional

        :param settings: Settings of the organization usage metrics dataflow.
        :type settings: SnowflakeOrganizationUsageMetricsIntegrationDataflowSettingsResponse, optional
        """
        if enabled is not unset:
            kwargs["enabled"] = enabled
        if settings is not unset:
            kwargs["settings"] = settings
        super().__init__(kwargs)
