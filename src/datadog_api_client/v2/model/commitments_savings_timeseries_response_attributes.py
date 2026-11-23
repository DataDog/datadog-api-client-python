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
    from datadog_api_client.v2.model.commitments_timeseries_metric import CommitmentsTimeseriesMetric
    from datadog_api_client.v2.model.commitments_unused_cost_meta import CommitmentsUnusedCostMeta
    from datadog_api_client.v2.model.commitments_query_definition import CommitmentsQueryDefinition


class CommitmentsSavingsTimeseriesResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.commitments_timeseries_metric import CommitmentsTimeseriesMetric
        from datadog_api_client.v2.model.commitments_unused_cost_meta import CommitmentsUnusedCostMeta
        from datadog_api_client.v2.model.commitments_query_definition import CommitmentsQueryDefinition

        return {
            "actual_cost": (CommitmentsTimeseriesMetric,),
            "effective_savings_rate": (CommitmentsTimeseriesMetric,),
            "meta": (CommitmentsUnusedCostMeta,),
            "on_demand_equivalent_cost": (CommitmentsTimeseriesMetric,),
            "query_definition": (CommitmentsQueryDefinition,),
            "realized_savings": (CommitmentsTimeseriesMetric,),
        }

    attribute_map = {
        "actual_cost": "actual_cost",
        "effective_savings_rate": "effective_savings_rate",
        "meta": "meta",
        "on_demand_equivalent_cost": "on_demand_equivalent_cost",
        "query_definition": "query_definition",
        "realized_savings": "realized_savings",
    }

    def __init__(
        self_,
        actual_cost: CommitmentsTimeseriesMetric,
        effective_savings_rate: CommitmentsTimeseriesMetric,
        on_demand_equivalent_cost: CommitmentsTimeseriesMetric,
        realized_savings: CommitmentsTimeseriesMetric,
        meta: Union[CommitmentsUnusedCostMeta, UnsetType] = unset,
        query_definition: Union[CommitmentsQueryDefinition, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of a timeseries savings response.

        :param actual_cost: A timeseries metric containing timestamps, series values, and optional unit metadata.
        :type actual_cost: CommitmentsTimeseriesMetric

        :param effective_savings_rate: A timeseries metric containing timestamps, series values, and optional unit metadata.
        :type effective_savings_rate: CommitmentsTimeseriesMetric

        :param meta: Metadata reporting that the cost data lacks the unused costs of some commitments, as with Azure exports
            scoped below the billing profile. Utilization is then overstated, and realized savings and effective
            savings rate are upper bounds. Omitted when the unused costs are available.
        :type meta: CommitmentsUnusedCostMeta, optional

        :param on_demand_equivalent_cost: A timeseries metric containing timestamps, series values, and optional unit metadata.
        :type on_demand_equivalent_cost: CommitmentsTimeseriesMetric

        :param query_definition: The query that produces the response values, in the same format as dashboard and notebook widget
            requests, so a client can graph the values in a widget. Each formula's ``id`` names the response value
            that it produces.
        :type query_definition: CommitmentsQueryDefinition, optional

        :param realized_savings: A timeseries metric containing timestamps, series values, and optional unit metadata.
        :type realized_savings: CommitmentsTimeseriesMetric
        """
        if meta is not unset:
            kwargs["meta"] = meta
        if query_definition is not unset:
            kwargs["query_definition"] = query_definition
        super().__init__(kwargs)

        self_.actual_cost = actual_cost
        self_.effective_savings_rate = effective_savings_rate
        self_.on_demand_equivalent_cost = on_demand_equivalent_cost
        self_.realized_savings = realized_savings
