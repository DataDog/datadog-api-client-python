# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.budget_with_entries_data_attributes_entries_items_tag_filters_items import (
        BudgetWithEntriesDataAttributesEntriesItemsTagFiltersItems,
    )


class BudgetWithEntriesDataAttributesEntriesItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.budget_with_entries_data_attributes_entries_items_tag_filters_items import (
            BudgetWithEntriesDataAttributesEntriesItemsTagFiltersItems,
        )

        return {
            "amount": (float,),
            "month": (int,),
            "tag_filters": ([BudgetWithEntriesDataAttributesEntriesItemsTagFiltersItems],),
        }

    attribute_map = {
        "amount": "amount",
        "month": "month",
        "tag_filters": "tag_filters",
    }

    def __init__(
        self_,
        amount: Union[float, UnsetType] = unset,
        month: Union[int, UnsetType] = unset,
        tag_filters: Union[List[BudgetWithEntriesDataAttributesEntriesItemsTagFiltersItems], UnsetType] = unset,
        **kwargs,
    ):
        """


        :param amount:
        :type amount: float, optional

        :param month:
        :type month: int, optional

        :param tag_filters:
        :type tag_filters: [BudgetWithEntriesDataAttributesEntriesItemsTagFiltersItems], optional
        """
        if amount is not unset:
            kwargs["amount"] = amount
        if month is not unset:
            kwargs["month"] = month
        if tag_filters is not unset:
            kwargs["tag_filters"] = tag_filters
        super().__init__(kwargs)
