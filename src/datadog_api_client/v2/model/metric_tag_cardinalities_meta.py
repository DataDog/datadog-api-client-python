# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class MetricTagCardinalitiesMeta(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "metric_name": (str,),
        }

    attribute_map = {
        "metric_name": "metric_name",
    }

    def __init__(self_, metric_name: Union[str, UnsetType] = unset, **kwargs):
        """
        Response metadata object.

        :param metric_name: The name of metric for which the tag cardinalities are returned.
            This matches the metric name provided in the request.
        :type metric_name: str, optional
        """
        if metric_name is not unset:
            kwargs["metric_name"] = metric_name
        super().__init__(kwargs)
