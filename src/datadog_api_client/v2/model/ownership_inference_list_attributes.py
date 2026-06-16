# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.ownership_inference_item import OwnershipInferenceItem


class OwnershipInferenceListAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ownership_inference_item import OwnershipInferenceItem

        return {
            "items": ([OwnershipInferenceItem],),
        }

    attribute_map = {
        "items": "items",
    }

    def __init__(self_, items: List[OwnershipInferenceItem], **kwargs):
        """
        The attributes of the ownership inferences collection response.

        :param items: The list of inferences for a resource, with one inference per owner type.
        :type items: [OwnershipInferenceItem]
        """
        super().__init__(kwargs)

        self_.items = items
