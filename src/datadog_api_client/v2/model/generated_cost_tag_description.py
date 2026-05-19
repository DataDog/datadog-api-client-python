# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.generated_cost_tag_description_attributes import (
        GeneratedCostTagDescriptionAttributes,
    )
    from datadog_api_client.v2.model.generated_cost_tag_description_type import GeneratedCostTagDescriptionType


class GeneratedCostTagDescription(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.generated_cost_tag_description_attributes import (
            GeneratedCostTagDescriptionAttributes,
        )
        from datadog_api_client.v2.model.generated_cost_tag_description_type import GeneratedCostTagDescriptionType

        return {
            "attributes": (GeneratedCostTagDescriptionAttributes,),
            "id": (str,),
            "type": (GeneratedCostTagDescriptionType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: GeneratedCostTagDescriptionAttributes,
        id: str,
        type: GeneratedCostTagDescriptionType,
        **kwargs,
    ):
        """
        AI-generated Cloud Cost Management tag key description returned by the generate endpoint. The result is returned to the client but is not persisted by this endpoint.

        :param attributes: Attributes of an AI-generated Cloud Cost Management tag key description.
        :type attributes: GeneratedCostTagDescriptionAttributes

        :param id: The tag key the AI description was generated for.
        :type id: str

        :param type: Type of the AI-generated Cloud Cost Management tag description resource.
        :type type: GeneratedCostTagDescriptionType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
