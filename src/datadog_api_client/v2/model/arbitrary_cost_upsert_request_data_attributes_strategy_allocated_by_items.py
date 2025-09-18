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
    from datadog_api_client.v2.model.arbitrary_cost_upsert_request_data_attributes_strategy_allocated_by_items_allocated_tags_items import (
        ArbitraryCostUpsertRequestDataAttributesStrategyAllocatedByItemsAllocatedTagsItems,
    )


class ArbitraryCostUpsertRequestDataAttributesStrategyAllocatedByItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.arbitrary_cost_upsert_request_data_attributes_strategy_allocated_by_items_allocated_tags_items import (
            ArbitraryCostUpsertRequestDataAttributesStrategyAllocatedByItemsAllocatedTagsItems,
        )

        return {
            "allocated_tags": ([ArbitraryCostUpsertRequestDataAttributesStrategyAllocatedByItemsAllocatedTagsItems],),
            "percentage": (float,),
        }

    attribute_map = {
        "allocated_tags": "allocated_tags",
        "percentage": "percentage",
    }

    def __init__(
        self_,
        allocated_tags: List[ArbitraryCostUpsertRequestDataAttributesStrategyAllocatedByItemsAllocatedTagsItems],
        percentage: float,
        **kwargs,
    ):
        """
        The definition of ``ArbitraryCostUpsertRequestDataAttributesStrategyAllocatedByItems`` object.

        :param allocated_tags: The ``items`` ``allocated_tags``.
        :type allocated_tags: [ArbitraryCostUpsertRequestDataAttributesStrategyAllocatedByItemsAllocatedTagsItems]

        :param percentage: The ``items`` ``percentage``. The numeric value format should be a 32bit float value.
        :type percentage: float
        """
        super().__init__(kwargs)

        self_.allocated_tags = allocated_tags
        self_.percentage = percentage
