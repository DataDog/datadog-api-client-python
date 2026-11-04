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
    from datadog_api_client.v2.model.commitments_query_definition_aggregator import CommitmentsQueryDefinitionAggregator
    from datadog_api_client.v2.model.commitments_query_definition_data_source import (
        CommitmentsQueryDefinitionDataSource,
    )


class CommitmentsQueryDefinitionQuery(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.commitments_query_definition_aggregator import (
            CommitmentsQueryDefinitionAggregator,
        )
        from datadog_api_client.v2.model.commitments_query_definition_data_source import (
            CommitmentsQueryDefinitionDataSource,
        )

        return {
            "aggregator": (CommitmentsQueryDefinitionAggregator,),
            "data_source": (CommitmentsQueryDefinitionDataSource,),
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
        aggregator: CommitmentsQueryDefinitionAggregator,
        data_source: CommitmentsQueryDefinitionDataSource,
        name: str,
        query: str,
        **kwargs,
    ):
        """
        A metric query of a query definition.

        :param aggregator: The reducer a scalar widget applies to the query.
        :type aggregator: CommitmentsQueryDefinitionAggregator

        :param data_source: The data source of the query.
        :type data_source: CommitmentsQueryDefinitionDataSource

        :param name: The name formulas use to reference the query.
        :type name: str

        :param query: The metric query.
        :type query: str
        """
        super().__init__(kwargs)

        self_.aggregator = aggregator
        self_.data_source = data_source
        self_.name = name
        self_.query = query
