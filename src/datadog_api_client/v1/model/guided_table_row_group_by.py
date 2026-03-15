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
    from datadog_api_client.v1.model.guided_table_row_group_by_format import GuidedTableRowGroupByFormat
    from datadog_api_client.v1.model.guided_table_group_key import GuidedTableGroupKey


class GuidedTableRowGroupBy(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.guided_table_row_group_by_format import GuidedTableRowGroupByFormat
        from datadog_api_client.v1.model.guided_table_group_key import GuidedTableGroupKey

        return {
            "alias": (str,),
            "format": (GuidedTableRowGroupByFormat,),
            "group_keys": ([GuidedTableGroupKey],),
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
        group_keys: List[GuidedTableGroupKey],
        name: str,
        alias: Union[str, UnsetType] = unset,
        format: Union[GuidedTableRowGroupByFormat, UnsetType] = unset,
        is_hidden: Union[bool, UnsetType] = unset,
        **kwargs,
    ):
        """
        Defines one group-by dimension used to produce the rows of a guided table.

        :param alias: Display name used as the column header for this group-by.
        :type alias: str, optional

        :param format: Text formatting configuration for this group-by column.
        :type format: GuidedTableRowGroupByFormat, optional

        :param group_keys: Mapping from each source query to the field name used as the grouping key. Different data sources may use different field names for the same concept.
        :type group_keys: [GuidedTableGroupKey]

        :param is_hidden: Whether this group-by column is hidden in the rendered table.
        :type is_hidden: bool, optional

        :param name: Auto-generated name for this group-by parameter.
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
