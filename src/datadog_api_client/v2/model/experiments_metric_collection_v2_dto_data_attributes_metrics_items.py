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


class ExperimentsMetricCollectionV2DTODataAttributesMetricsItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "metric_id": (str,),
            "metric_name": (str,),
        }

    attribute_map = {
        "metric_id": "metric_id",
        "metric_name": "metric_name",
    }

    def __init__(self_, metric_id: Union[str, UnsetType] = unset, metric_name: Union[str, UnsetType] = unset, **kwargs):
        """
        A metric included in the collection.

        :param metric_id: ID of the metric represented by this entry.
        :type metric_id: str, optional

        :param metric_name: Display name of the metric represented by this entry.
        :type metric_name: str, optional
        """
        if metric_id is not unset:
            kwargs["metric_id"] = metric_id
        if metric_name is not unset:
            kwargs["metric_name"] = metric_name
        super().__init__(kwargs)
