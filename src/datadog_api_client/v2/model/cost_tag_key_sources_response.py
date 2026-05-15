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
    from datadog_api_client.v2.model.cost_tag_key_source import CostTagKeySource


class CostTagKeySourcesResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.cost_tag_key_source import CostTagKeySource

        return {
            "data": ([CostTagKeySource],),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: List[CostTagKeySource], **kwargs):
        """
        List of Cloud Cost Management tag keys with their origin sources for the requested period.

        :param data: List of tag keys with their origin sources.
        :type data: [CostTagKeySource]
        """
        super().__init__(kwargs)

        self_.data = data
