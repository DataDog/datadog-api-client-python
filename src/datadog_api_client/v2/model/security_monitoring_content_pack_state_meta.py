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
    from datadog_api_client.v2.model.security_monitoring_sku import SecurityMonitoringSKU


class SecurityMonitoringContentPackStateMeta(ModelNormal):
    validations = {
        "retention_months": {
            "inclusive_maximum": 60,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_sku import SecurityMonitoringSKU

        return {
            "cloud_siem_index_incorrect": (bool,),
            "retention_months": (int,),
            "sku": (SecurityMonitoringSKU,),
        }

    attribute_map = {
        "cloud_siem_index_incorrect": "cloud_siem_index_incorrect",
        "retention_months": "retention_months",
        "sku": "sku",
    }

    def __init__(
        self_,
        cloud_siem_index_incorrect: bool,
        sku: SecurityMonitoringSKU,
        retention_months: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Metadata for content pack states.

        :param cloud_siem_index_incorrect: Whether the Cloud SIEM index configuration is incorrect for the organization.
        :type cloud_siem_index_incorrect: bool

        :param retention_months: The number of months that standard logs are retained for organizations on the standalone_indexed` pricing model. This field is omitted for other pricing models.
        :type retention_months: int, optional

        :param sku: The Cloud SIEM pricing model (SKU) for the organization.
        :type sku: SecurityMonitoringSKU
        """
        if retention_months is not unset:
            kwargs["retention_months"] = retention_months
        super().__init__(kwargs)

        self_.cloud_siem_index_incorrect = cloud_siem_index_incorrect
        self_.sku = sku
