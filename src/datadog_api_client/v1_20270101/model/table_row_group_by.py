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
    from datadog_api_client.v1_20270101.model.table_row_group_by_format import TableRowGroupByFormat
    from datadog_api_client.v1_20270101.model.table_group_key import TableGroupKey


class TableRowGroupBy(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.table_row_group_by_format import TableRowGroupByFormat
        from datadog_api_client.v1_20270101.model.table_group_key import TableGroupKey

        return {
            "alias": (str,),
            "format": (TableRowGroupByFormat,),
            "group_keys": ([TableGroupKey],),
            "is_hidden": (bool,),
            "name": (str,),
        }

    attribute_map = {
        "alias": "alias",
        "format": "format",
        "group_keys": "group_keys",
        "is_hidden": "is_hidden",
        "name": "name",
    }

    def __init__(
        self_,
        group_keys: List[TableGroupKey],
        name: str,
        alias: Union[str, UnsetType] = unset,
        format: Union[TableRowGroupByFormat, UnsetType] = unset,
        is_hidden: Union[bool, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param alias: Test-only generated schema for the dashboard versioning proof of concept.
        :type alias: str, optional

        :param format: Test-only generated schema for the dashboard versioning proof of concept.
        :type format: TableRowGroupByFormat, optional

        :param group_keys: Test-only generated schema for the dashboard versioning proof of concept.
        :type group_keys: [TableGroupKey]

        :param is_hidden: Test-only generated schema for the dashboard versioning proof of concept.
        :type is_hidden: bool, optional

        :param name: Test-only generated schema for the dashboard versioning proof of concept.
        :type name: str
        """
        if alias is not unset:
            kwargs["alias"] = alias
        if format is not unset:
            kwargs["format"] = format
        if is_hidden is not unset:
            kwargs["is_hidden"] = is_hidden
        super().__init__(kwargs)

        self_.group_keys = group_keys
        self_.name = name
