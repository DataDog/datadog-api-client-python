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
    from datadog_api_client.v1_20270101.model.cell_display_mode_option import CellDisplayModeOption
    from datadog_api_client.v1_20270101.model.query_sort_order import QuerySortOrder


class QueryTableColumnRequest(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.cell_display_mode_option import CellDisplayModeOption
        from datadog_api_client.v1_20270101.model.query_sort_order import QuerySortOrder

        return {
            "alias": (str,),
            "cell_display_mode": (CellDisplayModeOption,),
            "name": (str,),
            "order": (QuerySortOrder,),
        }

    attribute_map = {
        "alias": "alias",
        "cell_display_mode": "cell_display_mode",
        "name": "name",
        "order": "order",
    }

    def __init__(
        self_,
        name: str,
        alias: Union[str, UnsetType] = unset,
        cell_display_mode: Union[CellDisplayModeOption, UnsetType] = unset,
        order: Union[QuerySortOrder, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param alias: Test-only generated schema for the dashboard versioning proof of concept.
        :type alias: str, optional

        :param cell_display_mode: Test-only generated schema for the dashboard versioning proof of concept.
        :type cell_display_mode: CellDisplayModeOption, optional

        :param name: Test-only generated schema for the dashboard versioning proof of concept.
        :type name: str

        :param order: Test-only generated schema for the dashboard versioning proof of concept.
        :type order: QuerySortOrder, optional
        """
        if alias is not unset:
            kwargs["alias"] = alias
        if cell_display_mode is not unset:
            kwargs["cell_display_mode"] = cell_display_mode
        if order is not unset:
            kwargs["order"] = order
        super().__init__(kwargs)

        self_.name = name
