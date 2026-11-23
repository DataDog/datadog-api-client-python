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
    from datadog_api_client.v2.model.commitments_coverage_timeseries_metric import CommitmentsCoverageTimeseriesMetric
    from datadog_api_client.v2.model.commitments_query_definition import CommitmentsQueryDefinition


class CommitmentsCoverageTimeseriesResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.commitments_coverage_timeseries_metric import (
            CommitmentsCoverageTimeseriesMetric,
        )
        from datadog_api_client.v2.model.commitments_query_definition import CommitmentsQueryDefinition

        return {
            "cost": (CommitmentsCoverageTimeseriesMetric,),
            "hours": (CommitmentsCoverageTimeseriesMetric,),
            "query_definition": (CommitmentsQueryDefinition,),
        }

    attribute_map = {
        "cost": "cost",
        "hours": "hours",
        "query_definition": "query_definition",
    }

    def __init__(
        self_,
        cost: CommitmentsCoverageTimeseriesMetric,
        hours: CommitmentsCoverageTimeseriesMetric,
        query_definition: Union[CommitmentsQueryDefinition, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of a timeseries coverage response.

        :param cost: A coverage timeseries metric. For AWS and Azure, ``series`` holds the ``on_demand_only`` , ``spot_only`` , ``ri`` ,
            and ``sp`` buckets, plus ``ppp`` for Azure pre-purchase plans when enabled. For GCP, ``series`` holds the
            ``on_demand_only`` and ``flex_cud`` buckets.
        :type cost: CommitmentsCoverageTimeseriesMetric

        :param hours: A coverage timeseries metric. For AWS and Azure, ``series`` holds the ``on_demand_only`` , ``spot_only`` , ``ri`` ,
            and ``sp`` buckets, plus ``ppp`` for Azure pre-purchase plans when enabled. For GCP, ``series`` holds the
            ``on_demand_only`` and ``flex_cud`` buckets.
        :type hours: CommitmentsCoverageTimeseriesMetric

        :param query_definition: The query that produces the response values, in the same format as dashboard and notebook widget
            requests, so a client can graph the values in a widget. Each formula's ``id`` names the response value
            that it produces.
        :type query_definition: CommitmentsQueryDefinition, optional
        """
        if query_definition is not unset:
            kwargs["query_definition"] = query_definition
        super().__init__(kwargs)

        self_.cost = cost
        self_.hours = hours
