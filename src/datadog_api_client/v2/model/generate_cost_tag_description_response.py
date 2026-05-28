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
    from datadog_api_client.v2.model.generated_cost_tag_description import GeneratedCostTagDescription


class GenerateCostTagDescriptionResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.generated_cost_tag_description import GeneratedCostTagDescription

        return {
            "data": (GeneratedCostTagDescription,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: GeneratedCostTagDescription, **kwargs):
        """
        Response wrapping an AI-generated Cloud Cost Management tag key description.

        :param data: AI-generated Cloud Cost Management tag key description returned by the generate endpoint. The result is returned to the client but is not persisted by this endpoint.
        :type data: GeneratedCostTagDescription
        """
        super().__init__(kwargs)

        self_.data = data
