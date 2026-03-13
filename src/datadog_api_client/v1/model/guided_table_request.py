# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v1.model.guided_table_column import GuidedTableColumn
    from datadog_api_client.v1.model.guided_table_query import GuidedTableQuery
    from datadog_api_client.v1.model.guided_table_request_request_type import GuidedTableRequestRequestType
    from datadog_api_client.v1.model.guided_table_rows import GuidedTableRows
    from datadog_api_client.v1.model.guided_table_compute_column import GuidedTableComputeColumn
    from datadog_api_client.v1.model.guided_table_preset_column import GuidedTablePresetColumn
    from datadog_api_client.v1.model.guided_table_formula_column import GuidedTableFormulaColumn
    from datadog_api_client.v1.model.guided_table_metrics_query import GuidedTableMetricsQuery
    from datadog_api_client.v1.model.guided_table_events_query import GuidedTableEventsQuery


class GuidedTableRequest(ModelNormal):
    validations = {
        "queries": {
            "min_items": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.guided_table_column import GuidedTableColumn
        from datadog_api_client.v1.model.guided_table_query import GuidedTableQuery
        from datadog_api_client.v1.model.guided_table_request_request_type import GuidedTableRequestRequestType
        from datadog_api_client.v1.model.guided_table_rows import GuidedTableRows

        return {
            "columns": ([GuidedTableColumn],),
            "queries": ([GuidedTableQuery],),
            "request_type": (GuidedTableRequestRequestType,),
            "rows": (GuidedTableRows,),
        }

    attribute_map = {
        "columns": "columns",
        "queries": "queries",
        "request_type": "request_type",
        "rows": "rows",
    }

    def __init__(
        self_,
        columns: List[
            Union[GuidedTableColumn, GuidedTableComputeColumn, GuidedTablePresetColumn, GuidedTableFormulaColumn]
        ],
        queries: List[Union[GuidedTableQuery, GuidedTableMetricsQuery, GuidedTableEventsQuery]],
        request_type: GuidedTableRequestRequestType,
        rows: GuidedTableRows,
        **kwargs,
    ):
        """
        Request definition for the guided table widget — a structured, guided format for defining a table of data. Used when the ``graphing_new_table_widget_editor`` feature flag is enabled; otherwise use the classic ``TableWidgetRequest``. Defines base queries, how to produce rows, and how to compute columns.

        :param columns: Column definitions that describe how to compute and display table values.
        :type columns: [GuidedTableColumn]

        :param queries: Base queries that provide the source data for the table.
        :type queries: [GuidedTableQuery]

        :param request_type: Identifies this as a guided table request.
        :type request_type: GuidedTableRequestRequestType

        :param rows: Defines how to compute the rows of a guided table.
        :type rows: GuidedTableRows
        """
        super().__init__(kwargs)

        self_.columns = columns
        self_.queries = queries
        self_.request_type = request_type
        self_.rows = rows
