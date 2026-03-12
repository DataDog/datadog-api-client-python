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
    from datadog_api_client.v2.model.metric_volumes_relationship import MetricVolumesRelationship


class MetricRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.metric_volumes_relationship import MetricVolumesRelationship

        return {
            "metric_volumes": (MetricVolumesRelationship,),
        }

    attribute_map = {
        "metric_volumes": "metric_volumes",
    }

    def __init__(self_, metric_volumes: Union[MetricVolumesRelationship, UnsetType] = unset, **kwargs):
        """
        Relationships to related metric objects.

        :param metric_volumes: Relationship to a metric's ingested and indexed volumes.
        :type metric_volumes: MetricVolumesRelationship, optional
        """
        if metric_volumes is not unset:
            kwargs["metric_volumes"] = metric_volumes
        super().__init__(kwargs)
