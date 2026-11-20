# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Dict, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v1_20270101.model.dashboard_inline_schema8 import DashboardInlineSchema8
    from datadog_api_client.v1_20270101.model.change_type_options import ChangeTypeOptions
    from datadog_api_client.v1_20270101.model.compare_to_options import CompareToOptions
    from datadog_api_client.v1_20270101.model.order_by_options import OrderByOptions
    from datadog_api_client.v1_20270101.model.query_sort_order import QuerySortOrder


class ChangeBackendRequest20270101OneOf4454622976(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.dashboard_inline_schema8 import DashboardInlineSchema8
        from datadog_api_client.v1_20270101.model.change_type_options import ChangeTypeOptions
        from datadog_api_client.v1_20270101.model.compare_to_options import CompareToOptions
        from datadog_api_client.v1_20270101.model.order_by_options import OrderByOptions
        from datadog_api_client.v1_20270101.model.query_sort_order import QuerySortOrder

        return {
            "_query_options": (
                {
                    str: (
                        DashboardInlineSchema8,
                        none_type,
                    )
                },
            ),
            "change_type": (ChangeTypeOptions,),
            "compare_to": (CompareToOptions,),
            "increase_good": (bool,),
            "limit": (float,),
            "order_by": (OrderByOptions,),
            "order_dir": (QuerySortOrder,),
            "q": (str,),
            "show_present": (bool,),
        }

    attribute_map = {
        "_query_options": "_query_options",
        "change_type": "change_type",
        "compare_to": "compare_to",
        "increase_good": "increase_good",
        "limit": "limit",
        "order_by": "order_by",
        "order_dir": "order_dir",
        "q": "q",
        "show_present": "show_present",
    }

    def __init__(
        self_,
        q: str,
        _query_options: Union[Dict[str, Union[DashboardInlineSchema8, str, float, bool]], UnsetType] = unset,
        change_type: Union[ChangeTypeOptions, UnsetType] = unset,
        compare_to: Union[CompareToOptions, UnsetType] = unset,
        increase_good: Union[bool, UnsetType] = unset,
        limit: Union[float, UnsetType] = unset,
        order_by: Union[OrderByOptions, UnsetType] = unset,
        order_dir: Union[QuerySortOrder, UnsetType] = unset,
        show_present: Union[bool, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param _query_options: Test-only generated schema for the dashboard versioning proof of concept.
        :type _query_options: {str: (DashboardInlineSchema8, none_type,)}, optional

        :param change_type: Test-only generated schema for the dashboard versioning proof of concept.
        :type change_type: ChangeTypeOptions, optional

        :param compare_to: Test-only generated schema for the dashboard versioning proof of concept.
        :type compare_to: CompareToOptions, optional

        :param increase_good: Test-only generated schema for the dashboard versioning proof of concept.
        :type increase_good: bool, optional

        :param limit: Test-only generated schema for the dashboard versioning proof of concept.
        :type limit: float, optional

        :param order_by: Test-only generated schema for the dashboard versioning proof of concept.
        :type order_by: OrderByOptions, optional

        :param order_dir: Test-only generated schema for the dashboard versioning proof of concept.
        :type order_dir: QuerySortOrder, optional

        :param q: Test-only generated schema for the dashboard versioning proof of concept.
        :type q: str

        :param show_present: Test-only generated schema for the dashboard versioning proof of concept.
        :type show_present: bool, optional
        """
        if _query_options is not unset:
            kwargs["_query_options"] = _query_options
        if change_type is not unset:
            kwargs["change_type"] = change_type
        if compare_to is not unset:
            kwargs["compare_to"] = compare_to
        if increase_good is not unset:
            kwargs["increase_good"] = increase_good
        if limit is not unset:
            kwargs["limit"] = limit
        if order_by is not unset:
            kwargs["order_by"] = order_by
        if order_dir is not unset:
            kwargs["order_dir"] = order_dir
        if show_present is not unset:
            kwargs["show_present"] = show_present
        super().__init__(kwargs)

        self_.q = q
