# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.metric_tag_cardinality import MetricTagCardinality
    from datadog_api_client.v2.model.metric_tag_cardinalities_meta import MetricTagCardinalitiesMeta


class MetricTagCardinalitiesResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.metric_tag_cardinality import MetricTagCardinality
        from datadog_api_client.v2.model.metric_tag_cardinalities_meta import MetricTagCardinalitiesMeta

        return {
            "data": ([MetricTagCardinality],),
            "meta": (MetricTagCardinalitiesMeta,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }

    def __init__(
        self_,
        data: Union[List[MetricTagCardinality], UnsetType] = unset,
        meta: Union[MetricTagCardinalitiesMeta, UnsetType] = unset,
        **kwargs,
    ):
        """
        Response object that includes an array of objects representing the cardinality details of a metric's tags.

        :param data: A list of tag cardinalities associated with the given metric.
        :type data: [MetricTagCardinality], optional

        :param meta: Response metadata object.
        :type meta: MetricTagCardinalitiesMeta, optional
        """
        if data is not unset:
            kwargs["data"] = data
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)
