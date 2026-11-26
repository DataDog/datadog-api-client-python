# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v1_20270101.model.scalar_aggregator import ScalarAggregator
    from datadog_api_client.v1_20270101.model.formula_dataset_metric_query_data_source import (
        FormulaDatasetMetricQueryDataSource,
    )


class FormulaDatasetMetricQuery(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.scalar_aggregator import ScalarAggregator
        from datadog_api_client.v1_20270101.model.formula_dataset_metric_query_data_source import (
            FormulaDatasetMetricQueryDataSource,
        )

        return {
            "aggregator": (ScalarAggregator,),
            "data_source": (FormulaDatasetMetricQueryDataSource,),
            "name": (str,),
            "query": (str,),
        }

    attribute_map = {
        "aggregator": "aggregator",
        "data_source": "data_source",
        "name": "name",
        "query": "query",
    }

    def __init__(
        self_,
        data_source: FormulaDatasetMetricQueryDataSource,
        name: str,
        query: str,
        aggregator: Union[ScalarAggregator, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param aggregator: Test-only generated schema for the dashboard versioning proof of concept.
        :type aggregator: ScalarAggregator, optional

        :param data_source: Test-only generated schema for the dashboard versioning proof of concept.
        :type data_source: FormulaDatasetMetricQueryDataSource

        :param name: Test-only generated schema for the dashboard versioning proof of concept.
        :type name: str

        :param query: Test-only generated schema for the dashboard versioning proof of concept.
        :type query: str
        """
        if aggregator is not unset:
            kwargs["aggregator"] = aggregator
        super().__init__(kwargs)

        self_.data_source = data_source
        self_.name = name
        self_.query = query
