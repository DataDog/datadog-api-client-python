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
    from datadog_api_client.v2.model.security_monitoring_critical_asset_create_data import (
        SecurityMonitoringCriticalAssetCreateData,
    )


class SecurityMonitoringCriticalAssetCreateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_critical_asset_create_data import (
            SecurityMonitoringCriticalAssetCreateData,
        )

        return {
            "data": (SecurityMonitoringCriticalAssetCreateData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: SecurityMonitoringCriticalAssetCreateData, **kwargs):
        """
        Request object that includes the critical asset that you would like to create.

        :param data: Object for a single critical asset.
        :type data: SecurityMonitoringCriticalAssetCreateData
        """
        super().__init__(kwargs)

        self_.data = data
