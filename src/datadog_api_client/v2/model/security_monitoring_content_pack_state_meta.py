# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.security_monitoring_sku import SecurityMonitoringSKU


class SecurityMonitoringContentPackStateMeta(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_sku import SecurityMonitoringSKU

        return {
            "cloud_siem_index_incorrect": (bool,),
            "sku": (SecurityMonitoringSKU,),
        }

    attribute_map = {
        "cloud_siem_index_incorrect": "cloud_siem_index_incorrect",
        "sku": "sku",
    }

    def __init__(self_, cloud_siem_index_incorrect: bool, sku: SecurityMonitoringSKU, **kwargs):
        """
        Metadata for content pack states

        :param cloud_siem_index_incorrect: Whether the cloud SIEM index configuration is incorrect at the organization level
        :type cloud_siem_index_incorrect: bool

        :param sku: The SIEM pricing model (SKU) for the organization
        :type sku: SecurityMonitoringSKU
        """
        super().__init__(kwargs)

        self_.cloud_siem_index_incorrect = cloud_siem_index_incorrect
        self_.sku = sku
