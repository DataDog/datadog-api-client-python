# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class ExperimentsVariantResultsV2DTODataAttributesMetricsItemsCoverageSummary(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "control_total": (float,),
            "coverage": (float,),
            "coverage_unavailable_reason": (str,),
            "eligible_population_total": (float,),
            "experiment_total": (float,),
            "global_metric_total": (float,),
            "traffic_allocation": (float,),
        }

    attribute_map = {
        "control_total": "control_total",
        "coverage": "coverage",
        "coverage_unavailable_reason": "coverage_unavailable_reason",
        "eligible_population_total": "eligible_population_total",
        "experiment_total": "experiment_total",
        "global_metric_total": "global_metric_total",
        "traffic_allocation": "traffic_allocation",
    }

    def __init__(
        self_,
        control_total: Union[float, UnsetType] = unset,
        coverage: Union[float, UnsetType] = unset,
        coverage_unavailable_reason: Union[str, UnsetType] = unset,
        eligible_population_total: Union[float, UnsetType] = unset,
        experiment_total: Union[float, UnsetType] = unset,
        global_metric_total: Union[float, UnsetType] = unset,
        traffic_allocation: Union[float, UnsetType] = unset,
        **kwargs,
    ):
        """
        Population totals and allocation used to calculate metric coverage.

        :param control_total: Total metric value for the control population in the coverage calculation.
        :type control_total: float, optional

        :param coverage: Estimated share of the global metric total from the eligible population if that population received
            control. The estimate can exceed 1.
        :type coverage: float, optional

        :param coverage_unavailable_reason: Reason that metric coverage could not be calculated.
        :type coverage_unavailable_reason: str, optional

        :param eligible_population_total: Estimated metric total for the eligible population if that population received control.
        :type eligible_population_total: float, optional

        :param experiment_total: Total metric value for the experiment population in the coverage calculation.
        :type experiment_total: float, optional

        :param global_metric_total: Observed metric total across subjects inside and outside the experiment.
        :type global_metric_total: float, optional

        :param traffic_allocation: Fraction of eligible traffic allocated to the experiment, weighted by time.
        :type traffic_allocation: float, optional
        """
        if control_total is not unset:
            kwargs["control_total"] = control_total
        if coverage is not unset:
            kwargs["coverage"] = coverage
        if coverage_unavailable_reason is not unset:
            kwargs["coverage_unavailable_reason"] = coverage_unavailable_reason
        if eligible_population_total is not unset:
            kwargs["eligible_population_total"] = eligible_population_total
        if experiment_total is not unset:
            kwargs["experiment_total"] = experiment_total
        if global_metric_total is not unset:
            kwargs["global_metric_total"] = global_metric_total
        if traffic_allocation is not unset:
            kwargs["traffic_allocation"] = traffic_allocation
        super().__init__(kwargs)
