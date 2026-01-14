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
    from datadog_api_client.v2.model.security_monitoring_critical_asset_create_attributes import (
        SecurityMonitoringCriticalAssetCreateAttributes,
    )
    from datadog_api_client.v2.model.security_monitoring_critical_asset_type import SecurityMonitoringCriticalAssetType


class SecurityMonitoringCriticalAssetCreateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_critical_asset_create_attributes import (
            SecurityMonitoringCriticalAssetCreateAttributes,
        )
        from datadog_api_client.v2.model.security_monitoring_critical_asset_type import (
            SecurityMonitoringCriticalAssetType,
        )

        return {
            "attributes": (SecurityMonitoringCriticalAssetCreateAttributes,),
            "type": (SecurityMonitoringCriticalAssetType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: SecurityMonitoringCriticalAssetCreateAttributes,
        type: SecurityMonitoringCriticalAssetType,
        **kwargs,
    ):
        """
        Object for a single critical asset.

        :param attributes: Object containing the attributes of the critical asset to be created.
        :type attributes: SecurityMonitoringCriticalAssetCreateAttributes

        :param type: The type of the resource. The value should always be ``critical_assets``.
        :type type: SecurityMonitoringCriticalAssetType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
