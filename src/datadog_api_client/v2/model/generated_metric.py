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
    from datadog_api_client.v2.model.generated_metric_relationships import GeneratedMetricRelationships
    from datadog_api_client.v2.model.generated_metric_type import GeneratedMetricType


class GeneratedMetric(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.generated_metric_relationships import GeneratedMetricRelationships
        from datadog_api_client.v2.model.generated_metric_type import GeneratedMetricType

        return {
            "id": (str,),
            "relationships": (GeneratedMetricRelationships,),
            "type": (GeneratedMetricType,),
        }

    attribute_map = {
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        id: str,
        type: GeneratedMetricType,
        relationships: Union[GeneratedMetricRelationships, UnsetType] = unset,
        **kwargs,
    ):
        """
        Object for a single generated (derived) metric. Only returned for organizations with
        generated metrics enabled.

        :param id: The metric name for this resource.
        :type id: str

        :param relationships: Relationships for a generated metric.
        :type relationships: GeneratedMetricRelationships, optional

        :param type: The generated metric resource type.
        :type type: GeneratedMetricType
        """
        if relationships is not unset:
            kwargs["relationships"] = relationships
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
