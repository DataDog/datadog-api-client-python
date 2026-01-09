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
    from datadog_api_client.v2.model.security_monitoring_critical_asset_update_attributes import (
        SecurityMonitoringCriticalAssetUpdateAttributes,
    )
    from datadog_api_client.v2.model.security_monitoring_critical_asset_type import SecurityMonitoringCriticalAssetType


class SecurityMonitoringCriticalAssetUpdateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_critical_asset_update_attributes import (
            SecurityMonitoringCriticalAssetUpdateAttributes,
        )
        from datadog_api_client.v2.model.security_monitoring_critical_asset_type import (
            SecurityMonitoringCriticalAssetType,
        )

        return {
            "attributes": (SecurityMonitoringCriticalAssetUpdateAttributes,),
            "type": (SecurityMonitoringCriticalAssetType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: SecurityMonitoringCriticalAssetUpdateAttributes,
        type: SecurityMonitoringCriticalAssetType,
        **kwargs,
    ):
        """
        The new critical asset properties; partial updates are supported.

        :param attributes: The critical asset properties to be updated.
        :type attributes: SecurityMonitoringCriticalAssetUpdateAttributes

        :param type: The type of the resource. The value should always be ``critical_assets``.
        :type type: SecurityMonitoringCriticalAssetType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
