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
    from datadog_api_client.v2.model.security_monitoring_critical_asset_attributes import (
        SecurityMonitoringCriticalAssetAttributes,
    )
    from datadog_api_client.v2.model.security_monitoring_critical_asset_type import SecurityMonitoringCriticalAssetType


class SecurityMonitoringCriticalAsset(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_critical_asset_attributes import (
            SecurityMonitoringCriticalAssetAttributes,
        )
        from datadog_api_client.v2.model.security_monitoring_critical_asset_type import (
            SecurityMonitoringCriticalAssetType,
        )

        return {
            "attributes": (SecurityMonitoringCriticalAssetAttributes,),
            "id": (str,),
            "type": (SecurityMonitoringCriticalAssetType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[SecurityMonitoringCriticalAssetAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        type: Union[SecurityMonitoringCriticalAssetType, UnsetType] = unset,
        **kwargs,
    ):
        """
        The critical asset's properties.

        :param attributes: The attributes of the critical asset.
        :type attributes: SecurityMonitoringCriticalAssetAttributes, optional

        :param id: The ID of the critical asset.
        :type id: str, optional

        :param type: The type of the resource. The value should always be ``critical_assets``.
        :type type: SecurityMonitoringCriticalAssetType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
