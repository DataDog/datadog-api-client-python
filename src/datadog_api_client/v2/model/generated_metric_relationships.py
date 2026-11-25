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
    from datadog_api_client.v2.model.generated_metric_attributes_relationship import (
        GeneratedMetricAttributesRelationship,
    )


class GeneratedMetricRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.generated_metric_attributes_relationship import (
            GeneratedMetricAttributesRelationship,
        )

        return {
            "generated_metric_attributes": (GeneratedMetricAttributesRelationship,),
        }

    attribute_map = {
        "generated_metric_attributes": "generated_metric_attributes",
    }

    def __init__(
        self_, generated_metric_attributes: Union[GeneratedMetricAttributesRelationship, UnsetType] = unset, **kwargs
    ):
        """
        Relationships for a generated metric.

        :param generated_metric_attributes: Relationship to the attributes of a generated metric.
        :type generated_metric_attributes: GeneratedMetricAttributesRelationship, optional
        """
        if generated_metric_attributes is not unset:
            kwargs["generated_metric_attributes"] = generated_metric_attributes
        super().__init__(kwargs)
