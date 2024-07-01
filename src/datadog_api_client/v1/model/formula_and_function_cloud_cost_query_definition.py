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
    from datadog_api_client.v1.model.widget_aggregator import WidgetAggregator
    from datadog_api_client.v1.model.formula_and_function_cloud_cost_data_source import (
        FormulaAndFunctionCloudCostDataSource,
    )


class FormulaAndFunctionCloudCostQueryDefinition(ModelNormal):
    validations = {
        "cross_org_uuids": {
            "max_items": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.widget_aggregator import WidgetAggregator
        from datadog_api_client.v1.model.formula_and_function_cloud_cost_data_source import (
            FormulaAndFunctionCloudCostDataSource,
        )

        return {
            "aggregator": (WidgetAggregator,),
            "cross_org_uuids": ([str],),
            "data_source": (FormulaAndFunctionCloudCostDataSource,),
            "name": (str,),
            "query": (str,),
        }

    attribute_map = {
        "aggregator": "aggregator",
        "cross_org_uuids": "cross_org_uuids",
        "data_source": "data_source",
        "name": "name",
        "query": "query",
    }

    def __init__(
        self_,
        data_source: FormulaAndFunctionCloudCostDataSource,
        name: str,
        query: str,
        aggregator: Union[WidgetAggregator, UnsetType] = unset,
        cross_org_uuids: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        A formula and functions Cloud Cost query.

        :param aggregator: Aggregator used for the request.
        :type aggregator: WidgetAggregator, optional

        :param cross_org_uuids: The source organization UUID for cross organization queries. Feature in Private Beta.
        :type cross_org_uuids: [str], optional

        :param data_source: Data source for Cloud Cost queries.
        :type data_source: FormulaAndFunctionCloudCostDataSource

        :param name: Name of the query for use in formulas.
        :type name: str

        :param query: Query for Cloud Cost data.
        :type query: str
        """
        if aggregator is not unset:
            kwargs["aggregator"] = aggregator
        if cross_org_uuids is not unset:
            kwargs["cross_org_uuids"] = cross_org_uuids
        super().__init__(kwargs)

        self_.data_source = data_source
        self_.name = name
        self_.query = query
