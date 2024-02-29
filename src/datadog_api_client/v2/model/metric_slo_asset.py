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
    from datadog_api_client.v2.model.metric_slo_type import MetricSLOType


class MetricSLOAsset(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.metric_asset_attributes import MetricAssetAttributes
        from datadog_api_client.v2.model.metric_slo_type import MetricSLOType

        return {
            "attributes": (MetricAssetAttributes,),
            "id": (str,),
            "type": (MetricSLOType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, id: str, type: MetricSLOType, attributes: Union[MetricAssetAttributes, UnsetType] = unset, **kwargs
    ):
        """
        A SLO object with title.

        :param attributes: Assets where only included attribute is its title
        :type attributes: MetricAssetAttributes, optional

        :param id: The SLO ID.
        :type id: str

        :param type: SLO resource type.
        :type type: MetricSLOType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
