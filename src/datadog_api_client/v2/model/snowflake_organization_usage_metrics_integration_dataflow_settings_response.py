# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class SnowflakeOrganizationUsageMetricsIntegrationDataflowSettingsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "organization_usage_metrics_aggregate_last_24h": (bool,),
        }

    attribute_map = {
        "organization_usage_metrics_aggregate_last_24h": "organization_usage_metrics_aggregate_last_24h",
    }

    def __init__(self_, organization_usage_metrics_aggregate_last_24h: Union[bool, UnsetType] = unset, **kwargs):
        """
        Settings of the organization usage metrics dataflow.

        :param organization_usage_metrics_aggregate_last_24h: Period each metric aggregates over. When ``true`` , metrics aggregate the past 24 hours on a rolling basis; when ``false`` , they aggregate the current day so far.
        :type organization_usage_metrics_aggregate_last_24h: bool, optional
        """
        if organization_usage_metrics_aggregate_last_24h is not unset:
            kwargs["organization_usage_metrics_aggregate_last_24h"] = organization_usage_metrics_aggregate_last_24h
        super().__init__(kwargs)
