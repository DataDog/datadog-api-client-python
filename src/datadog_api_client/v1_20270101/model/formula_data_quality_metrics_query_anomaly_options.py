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
    from datadog_api_client.v1_20270101.model.formula_data_quality_metrics_query_anomaly_options_direction import (
        FormulaDataQualityMetricsQueryAnomalyOptionsDirection,
    )


class FormulaDataQualityMetricsQueryAnomalyOptions(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.formula_data_quality_metrics_query_anomaly_options_direction import (
            FormulaDataQualityMetricsQueryAnomalyOptionsDirection,
        )

        return {
            "direction": (FormulaDataQualityMetricsQueryAnomalyOptionsDirection,),
            "rule_id": (float,),
        }

    attribute_map = {
        "direction": "direction",
        "rule_id": "rule_id",
    }

    def __init__(
        self_,
        direction: Union[FormulaDataQualityMetricsQueryAnomalyOptionsDirection, UnsetType] = unset,
        rule_id: Union[float, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param direction: Test-only generated schema for the dashboard versioning proof of concept.
        :type direction: FormulaDataQualityMetricsQueryAnomalyOptionsDirection, optional

        :param rule_id: Test-only generated schema for the dashboard versioning proof of concept.
        :type rule_id: float, optional
        """
        if direction is not unset:
            kwargs["direction"] = direction
        if rule_id is not unset:
            kwargs["rule_id"] = rule_id
        super().__init__(kwargs)
