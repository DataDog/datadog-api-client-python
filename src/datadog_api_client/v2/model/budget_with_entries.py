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
    from datadog_api_client.v2.model.budget_with_entries_data import BudgetWithEntriesData
    from datadog_api_client.v2.model.budget_with_entries_meta import BudgetWithEntriesMeta


class BudgetWithEntries(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.budget_with_entries_data import BudgetWithEntriesData
        from datadog_api_client.v2.model.budget_with_entries_meta import BudgetWithEntriesMeta

        return {
            "data": (BudgetWithEntriesData,),
            "meta": (BudgetWithEntriesMeta,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }

    def __init__(
        self_,
        data: Union[BudgetWithEntriesData, UnsetType] = unset,
        meta: Union[BudgetWithEntriesMeta, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of the ``BudgetWithEntries`` object.

        :param data: A budget and all its entries.
        :type data: BudgetWithEntriesData, optional

        :param meta: Additional information about errors encountered while retrieving budget cost data.
        :type meta: BudgetWithEntriesMeta, optional
        """
        if data is not unset:
            kwargs["data"] = data
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)
