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
    from datadog_api_client.v2.model.generated_metric_attributes_relationship_data import (
        GeneratedMetricAttributesRelationshipData,
    )
    from datadog_api_client.v2.model.generated_metric_attributes_relationship_links import (
        GeneratedMetricAttributesRelationshipLinks,
    )


class GeneratedMetricAttributesRelationship(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.generated_metric_attributes_relationship_data import (
            GeneratedMetricAttributesRelationshipData,
        )
        from datadog_api_client.v2.model.generated_metric_attributes_relationship_links import (
            GeneratedMetricAttributesRelationshipLinks,
        )

        return {
            "data": (GeneratedMetricAttributesRelationshipData,),
            "links": (GeneratedMetricAttributesRelationshipLinks,),
        }

    attribute_map = {
        "data": "data",
        "links": "links",
    }

    def __init__(
        self_,
        data: Union[GeneratedMetricAttributesRelationshipData, UnsetType] = unset,
        links: Union[GeneratedMetricAttributesRelationshipLinks, UnsetType] = unset,
        **kwargs,
    ):
        """
        Relationship to the attributes of a generated metric.

        :param data: Relationship data for the attributes of a generated metric.
        :type data: GeneratedMetricAttributesRelationshipData, optional

        :param links: Links for the generated metric attributes relationship.
        :type links: GeneratedMetricAttributesRelationshipLinks, optional
        """
        if data is not unset:
            kwargs["data"] = data
        if links is not unset:
            kwargs["links"] = links
        super().__init__(kwargs)
