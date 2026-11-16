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
    from datadog_api_client.v1.model.monitor_formula_and_function_data_quality_data_source import (
        MonitorFormulaAndFunctionDataQualityDataSource,
    )
    from datadog_api_client.v1.model.monitor_formula_and_function_data_quality_monitor_options import (
        MonitorFormulaAndFunctionDataQualityMonitorOptions,
    )


class MonitorFormulaAndFunctionDataQualityQueryDefinition(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.monitor_formula_and_function_data_quality_data_source import (
            MonitorFormulaAndFunctionDataQualityDataSource,
        )
        from datadog_api_client.v1.model.monitor_formula_and_function_data_quality_monitor_options import (
            MonitorFormulaAndFunctionDataQualityMonitorOptions,
        )

        return {
            "data_source": (MonitorFormulaAndFunctionDataQualityDataSource,),
            "filter": (str,),
            "group_by": ([str],),
            "measure": (str,),
            "monitor_options": (MonitorFormulaAndFunctionDataQualityMonitorOptions,),
            "name": (str,),
            "schema_version": (str,),
            "scope": (str,),
        }

    attribute_map = {
        "data_source": "data_source",
        "filter": "filter",
        "group_by": "group_by",
        "measure": "measure",
        "monitor_options": "monitor_options",
        "name": "name",
        "schema_version": "schema_version",
        "scope": "scope",
    }

    def __init__(
        self_,
        data_source: MonitorFormulaAndFunctionDataQualityDataSource,
        filter: str,
        measure: str,
        name: str,
        group_by: Union[List[str], UnsetType] = unset,
        monitor_options: Union[MonitorFormulaAndFunctionDataQualityMonitorOptions, UnsetType] = unset,
        schema_version: Union[str, UnsetType] = unset,
        scope: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        A formula and functions data quality query.

        :param data_source: Data source for data quality queries.
        :type data_source: MonitorFormulaAndFunctionDataQualityDataSource

        :param filter: Filter expression used to match on data entities. Uses Aastra query syntax.
        :type filter: str

        :param group_by: Optional grouping fields for aggregation.
        :type group_by: [str], optional

        :param measure: The data quality measure to query. Common values include:
            ``bytes`` , ``cardinality`` , ``custom`` , ``freshness`` , ``max`` , ``mean`` , ``min`` ,
            ``nullness`` , ``percent_negative`` , ``percent_zero`` , ``row_count`` , ``stddev`` ,
            ``sum`` , ``uniqueness``. Additional values may be supported.
        :type measure: str

        :param monitor_options: Monitor configuration options for data quality queries.
        :type monitor_options: MonitorFormulaAndFunctionDataQualityMonitorOptions, optional

        :param name: Name of the query for use in formulas.
        :type name: str

        :param schema_version: Schema version for the data quality query.
        :type schema_version: str, optional

        :param scope: Optional scoping expression to further filter metrics. Uses metrics filter syntax.
            This is useful when an entity has been configured to emit metrics with additional tags.
        :type scope: str, optional
        """
        if group_by is not unset:
            kwargs["group_by"] = group_by
        if monitor_options is not unset:
            kwargs["monitor_options"] = monitor_options
        if schema_version is not unset:
            kwargs["schema_version"] = schema_version
        if scope is not unset:
            kwargs["scope"] = scope
        super().__init__(kwargs)

        self_.data_source = data_source
        self_.filter = filter
        self_.measure = measure
        self_.name = name
