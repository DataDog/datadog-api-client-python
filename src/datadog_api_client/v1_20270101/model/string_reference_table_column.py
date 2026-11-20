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
    from datadog_api_client.v1_20270101.model.string_table_column_format import StringTableColumnFormat
    from datadog_api_client.v1_20270101.model.exclude_null_table_column_function import ExcludeNullTableColumnFunction
    from datadog_api_client.v1_20270101.model.string_reference_table_column_reference import (
        StringReferenceTableColumnReference,
    )
    from datadog_api_client.v1_20270101.model.string_reference_table_column_type import StringReferenceTableColumnType


class StringReferenceTableColumn(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.string_table_column_format import StringTableColumnFormat
        from datadog_api_client.v1_20270101.model.exclude_null_table_column_function import (
            ExcludeNullTableColumnFunction,
        )
        from datadog_api_client.v1_20270101.model.string_reference_table_column_reference import (
            StringReferenceTableColumnReference,
        )
        from datadog_api_client.v1_20270101.model.string_reference_table_column_type import (
            StringReferenceTableColumnType,
        )

        return {
            "alias": (str,),
            "format": (StringTableColumnFormat,),
            "functions": ([ExcludeNullTableColumnFunction],),
            "is_hidden": (bool,),
            "name": (str,),
            "reference": (StringReferenceTableColumnReference,),
            "type": (StringReferenceTableColumnType,),
        }

    attribute_map = {
        "alias": "alias",
        "format": "format",
        "functions": "functions",
        "is_hidden": "is_hidden",
        "name": "name",
        "reference": "reference",
        "type": "type",
    }

    def __init__(
        self_,
        format: StringTableColumnFormat,
        name: str,
        reference: StringReferenceTableColumnReference,
        type: StringReferenceTableColumnType,
        alias: Union[str, UnsetType] = unset,
        functions: Union[List[ExcludeNullTableColumnFunction], UnsetType] = unset,
        is_hidden: Union[bool, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param alias: Test-only generated schema for the dashboard versioning proof of concept.
        :type alias: str, optional

        :param format: Test-only generated schema for the dashboard versioning proof of concept.
        :type format: StringTableColumnFormat

        :param functions: Test-only generated schema for the dashboard versioning proof of concept.
        :type functions: [ExcludeNullTableColumnFunction], optional

        :param is_hidden: Test-only generated schema for the dashboard versioning proof of concept.
        :type is_hidden: bool, optional

        :param name: Test-only generated schema for the dashboard versioning proof of concept.
        :type name: str

        :param reference: Test-only generated schema for the dashboard versioning proof of concept.
        :type reference: StringReferenceTableColumnReference

        :param type: Test-only generated schema for the dashboard versioning proof of concept.
        :type type: StringReferenceTableColumnType
        """
        if alias is not unset:
            kwargs["alias"] = alias
        if functions is not unset:
            kwargs["functions"] = functions
        if is_hidden is not unset:
            kwargs["is_hidden"] = is_hidden
        super().__init__(kwargs)

        self_.format = format
        self_.name = name
        self_.reference = reference
        self_.type = type
