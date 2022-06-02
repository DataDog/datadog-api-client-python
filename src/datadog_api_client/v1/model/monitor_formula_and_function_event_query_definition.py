# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class MonitorFormulaAndFunctionEventQueryDefinition(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.monitor_formula_and_function_event_query_definition_compute import (
            MonitorFormulaAndFunctionEventQueryDefinitionCompute,
        )
        from datadog_api_client.v1.model.monitor_formula_and_function_events_data_source import (
            MonitorFormulaAndFunctionEventsDataSource,
        )
        from datadog_api_client.v1.model.monitor_formula_and_function_event_query_group_by import (
            MonitorFormulaAndFunctionEventQueryGroupBy,
        )
        from datadog_api_client.v1.model.monitor_formula_and_function_event_query_definition_search import (
            MonitorFormulaAndFunctionEventQueryDefinitionSearch,
        )

        return {
            "compute": (MonitorFormulaAndFunctionEventQueryDefinitionCompute,),
            "data_source": (MonitorFormulaAndFunctionEventsDataSource,),
            "group_by": ([MonitorFormulaAndFunctionEventQueryGroupBy],),
            "indexes": ([str],),
            "name": (str,),
            "search": (MonitorFormulaAndFunctionEventQueryDefinitionSearch,),
        }

    attribute_map = {
        "compute": "compute",
        "data_source": "data_source",
        "group_by": "group_by",
        "indexes": "indexes",
        "name": "name",
        "search": "search",
    }

    def __init__(self, compute, data_source, name, *args, **kwargs):
        """
        A formula and functions events query.

        :param compute: Compute options.
        :type compute: MonitorFormulaAndFunctionEventQueryDefinitionCompute

        :param data_source: Data source for event platform-based queries.
        :type data_source: MonitorFormulaAndFunctionEventsDataSource

        :param group_by: Group by options.
        :type group_by: [MonitorFormulaAndFunctionEventQueryGroupBy], optional

        :param indexes: An array of index names to query in the stream. Omit or use ``[]`` to query all indexes at once.
        :type indexes: [str], optional

        :param name: Name of the query for use in formulas.
        :type name: str

        :param search: Search options.
        :type search: MonitorFormulaAndFunctionEventQueryDefinitionSearch, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.compute = compute
        self.data_source = data_source
        self.name = name

    @classmethod
    def _from_openapi_data(cls, compute, data_source, name, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(MonitorFormulaAndFunctionEventQueryDefinition, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.compute = compute
        self.data_source = data_source
        self.name = name
        return self
