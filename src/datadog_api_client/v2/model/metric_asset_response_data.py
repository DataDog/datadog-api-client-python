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
    from datadog_api_client.v2.model.metric_asset_response_relationships import MetricAssetResponseRelationships
    from datadog_api_client.v2.model.metric_type import MetricType


class MetricAssetResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.metric_asset_response_relationships import MetricAssetResponseRelationships
        from datadog_api_client.v2.model.metric_type import MetricType

        return {
            "id": (str,),
            "relationships": (MetricAssetResponseRelationships,),
            "type": (MetricType,),
        }

    attribute_map = {
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        id: str,
        type: MetricType,
        relationships: Union[MetricAssetResponseRelationships, UnsetType] = unset,
        **kwargs,
    ):
        """
        Metric assets response data.

        :param id: The metric name for this resource.
        :type id: str

        :param relationships: Relationships to assets related to the metric.
        :type relationships: MetricAssetResponseRelationships, optional

        :param type: The metric resource type.
        :type type: MetricType
        """
        if relationships is not unset:
            kwargs["relationships"] = relationships
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
