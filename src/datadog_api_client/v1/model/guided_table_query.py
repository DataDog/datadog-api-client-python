# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class GuidedTableQuery(ModelComposed):
    def __init__(self, **kwargs):
        """
        A base query used as source data for a guided table widget. Either a metrics query or an events-platform query.

        :param alias: Display alias for the query.
        :type alias: str, optional

        :param data_source: Metrics data source.
        :type data_source: GuidedTableMetricsQueryDataSource

        :param filter: Filter string to apply to the metric query.
        :type filter: str, optional

        :param metric_name: Name of the metric to query.
        :type metric_name: str

        :param name: Variable name used to reference this query in columns and formulas.
        :type name: str

        :param indexes: Indexes to search for events.
        :type indexes: [str], optional

        :param search: Search filter for matching events.
        :type search: GuidedTableEventsQuerySearch, optional

        :param storage: Storage tier to target for an events-platform query in a guided table.
        :type storage: GuidedTableStorageType, optional
        """
        super().__init__(kwargs)

    @cached_property
    def _composed_schemas(_):
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        from datadog_api_client.v1.model.guided_table_metrics_query import GuidedTableMetricsQuery
        from datadog_api_client.v1.model.guided_table_events_query import GuidedTableEventsQuery

        return {
            "oneOf": [
                GuidedTableMetricsQuery,
                GuidedTableEventsQuery,
            ],
        }
