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
    from datadog_api_client.v1_20270101.model.dashboard_inline_schema48 import DashboardInlineSchema48
    from datadog_api_client.v1_20270101.model.table_column_modifier_name import TableColumnModifierName


class TableColumnModifier(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.dashboard_inline_schema48 import DashboardInlineSchema48
        from datadog_api_client.v1_20270101.model.table_column_modifier_name import TableColumnModifierName

        return {
            "args": ([DashboardInlineSchema48],),
            "name": (TableColumnModifierName,),
        }

    attribute_map = {
        "args": "args",
        "name": "name",
    }

    def __init__(
        self_,
        name: TableColumnModifierName,
        args: Union[List[Union[DashboardInlineSchema48, str, float]], UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param args: Test-only generated schema for the dashboard versioning proof of concept.
        :type args: [DashboardInlineSchema48], optional

        :param name: Test-only generated schema for the dashboard versioning proof of concept.
        :type name: TableColumnModifierName
        """
        if args is not unset:
            kwargs["args"] = args
        super().__init__(kwargs)

        self_.name = name
