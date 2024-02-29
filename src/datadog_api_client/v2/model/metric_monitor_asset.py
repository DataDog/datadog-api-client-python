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
    from datadog_api_client.v2.model.metric_asset_attributes import MetricAssetAttributes
    from datadog_api_client.v2.model.metric_monitor_type import MetricMonitorType


class MetricMonitorAsset(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.metric_asset_attributes import MetricAssetAttributes
        from datadog_api_client.v2.model.metric_monitor_type import MetricMonitorType

        return {
            "attributes": (MetricAssetAttributes,),
            "id": (str,),
            "type": (MetricMonitorType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, id: str, type: MetricMonitorType, attributes: Union[MetricAssetAttributes, UnsetType] = unset, **kwargs
    ):
        """
        A monitor object with title.

        :param attributes: Assets where only included attribute is its title
        :type attributes: MetricAssetAttributes, optional

        :param id: The related monitor's ID.
        :type id: str

        :param type: Monitor resource type.
        :type type: MetricMonitorType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
