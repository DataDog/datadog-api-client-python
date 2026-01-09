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
    from datadog_api_client.v2.model.security_monitoring_critical_asset_update_data import (
        SecurityMonitoringCriticalAssetUpdateData,
    )


class SecurityMonitoringCriticalAssetUpdateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_critical_asset_update_data import (
            SecurityMonitoringCriticalAssetUpdateData,
        )

        return {
            "data": (SecurityMonitoringCriticalAssetUpdateData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: SecurityMonitoringCriticalAssetUpdateData, **kwargs):
        """
        Request object containing the fields to update on the critical asset.

        :param data: The new critical asset properties; partial updates are supported.
        :type data: SecurityMonitoringCriticalAssetUpdateData
        """
        super().__init__(kwargs)

        self_.data = data
