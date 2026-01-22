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
    from datadog_api_client.v2.model.budget_with_entries_data_attributes_entries_items import (
        BudgetWithEntriesDataAttributesEntriesItems,
    )


class BudgetWithEntriesDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.budget_with_entries_data_attributes_entries_items import (
            BudgetWithEntriesDataAttributesEntriesItems,
        )

        return {
            "created_at": (int,),
            "created_by": (str,),
            "end_month": (int,),
            "entries": ([BudgetWithEntriesDataAttributesEntriesItems],),
            "metrics_query": (str,),
            "name": (str,),
            "org_id": (int,),
            "start_month": (int,),
            "total_amount": (float,),
            "updated_at": (int,),
            "updated_by": (str,),
        }

    attribute_map = {
        "created_at": "created_at",
        "created_by": "created_by",
        "end_month": "end_month",
        "entries": "entries",
        "metrics_query": "metrics_query",
        "name": "name",
        "org_id": "org_id",
        "start_month": "start_month",
        "total_amount": "total_amount",
        "updated_at": "updated_at",
        "updated_by": "updated_by",
    }

    def __init__(
        self_,
        created_at: Union[int, UnsetType] = unset,
        created_by: Union[str, UnsetType] = unset,
        end_month: Union[int, UnsetType] = unset,
        entries: Union[List[BudgetWithEntriesDataAttributesEntriesItems], UnsetType] = unset,
        metrics_query: Union[str, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        org_id: Union[int, UnsetType] = unset,
        start_month: Union[int, UnsetType] = unset,
        total_amount: Union[float, UnsetType] = unset,
        updated_at: Union[int, UnsetType] = unset,
        updated_by: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """


        :param created_at:
        :type created_at: int, optional

        :param created_by:
        :type created_by: str, optional

        :param end_month:
        :type end_month: int, optional

        :param entries:
        :type entries: [BudgetWithEntriesDataAttributesEntriesItems], optional

        :param metrics_query:
        :type metrics_query: str, optional

        :param name:
        :type name: str, optional

        :param org_id:
        :type org_id: int, optional

        :param start_month:
        :type start_month: int, optional

        :param total_amount:
        :type total_amount: float, optional

        :param updated_at:
        :type updated_at: int, optional

        :param updated_by:
        :type updated_by: str, optional
        """
        if created_at is not unset:
            kwargs["created_at"] = created_at
        if created_by is not unset:
            kwargs["created_by"] = created_by
        if end_month is not unset:
            kwargs["end_month"] = end_month
        if entries is not unset:
            kwargs["entries"] = entries
        if metrics_query is not unset:
            kwargs["metrics_query"] = metrics_query
        if name is not unset:
            kwargs["name"] = name
        if org_id is not unset:
            kwargs["org_id"] = org_id
        if start_month is not unset:
            kwargs["start_month"] = start_month
        if total_amount is not unset:
            kwargs["total_amount"] = total_amount
        if updated_at is not unset:
            kwargs["updated_at"] = updated_at
        if updated_by is not unset:
            kwargs["updated_by"] = updated_by
        super().__init__(kwargs)
