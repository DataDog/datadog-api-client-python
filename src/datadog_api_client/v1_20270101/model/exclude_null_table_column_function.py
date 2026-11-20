# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v1_20270101.model.exclude_null_table_column_function_name import (
        ExcludeNullTableColumnFunctionName,
    )


class ExcludeNullTableColumnFunction(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.exclude_null_table_column_function_name import (
            ExcludeNullTableColumnFunctionName,
        )

        return {
            "name": (ExcludeNullTableColumnFunctionName,),
        }

    attribute_map = {
        "name": "name",
    }

    def __init__(self_, name: ExcludeNullTableColumnFunctionName, **kwargs):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param name: Test-only generated schema for the dashboard versioning proof of concept.
        :type name: ExcludeNullTableColumnFunctionName
        """
        super().__init__(kwargs)

        self_.name = name
