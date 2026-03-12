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
    from datadog_api_client.v1.model.monitor_formula_and_function_reference_table_column import (
        MonitorFormulaAndFunctionReferenceTableColumn,
    )
    from datadog_api_client.v1.model.monitor_formula_and_function_reference_table_data_source import (
        MonitorFormulaAndFunctionReferenceTableDataSource,
    )


class MonitorFormulaAndFunctionReferenceTableQueryDefinition(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.monitor_formula_and_function_reference_table_column import (
            MonitorFormulaAndFunctionReferenceTableColumn,
        )
        from datadog_api_client.v1.model.monitor_formula_and_function_reference_table_data_source import (
            MonitorFormulaAndFunctionReferenceTableDataSource,
        )

        return {
            "columns": ([MonitorFormulaAndFunctionReferenceTableColumn],),
            "data_source": (MonitorFormulaAndFunctionReferenceTableDataSource,),
            "name": (str,),
            "query_filter": (str,),
            "table_name": (str,),
        }

    attribute_map = {
        "columns": "columns",
        "data_source": "data_source",
        "name": "name",
        "query_filter": "query_filter",
        "table_name": "table_name",
    }

    def __init__(
        self_,
        data_source: MonitorFormulaAndFunctionReferenceTableDataSource,
        table_name: str,
        columns: Union[List[MonitorFormulaAndFunctionReferenceTableColumn], UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        query_filter: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        A reference table query for use in aggregate queries.

        :param columns: List of columns to retrieve from the reference table.
        :type columns: [MonitorFormulaAndFunctionReferenceTableColumn], optional

        :param data_source: Data source for reference table queries.
        :type data_source: MonitorFormulaAndFunctionReferenceTableDataSource

        :param name: Name of the query.
        :type name: str, optional

        :param query_filter: Optional filter expression for the reference table query.
        :type query_filter: str, optional

        :param table_name: Name of the reference table.
        :type table_name: str
        """
        if columns is not unset:
            kwargs["columns"] = columns
        if name is not unset:
            kwargs["name"] = name
        if query_filter is not unset:
            kwargs["query_filter"] = query_filter
        super().__init__(kwargs)

        self_.data_source = data_source
        self_.table_name = table_name
