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
    from datadog_api_client.v2.model.timeseries_anomaly_investigation_formula_limit_order import (
        TimeseriesAnomalyInvestigationFormulaLimitOrder,
    )


class TimeseriesAnomalyInvestigationFormulaLimit(ModelNormal):
    validations = {
        "count": {
            "inclusive_minimum": 0,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.timeseries_anomaly_investigation_formula_limit_order import (
            TimeseriesAnomalyInvestigationFormulaLimitOrder,
        )

        return {
            "count": (int,),
            "order": (TimeseriesAnomalyInvestigationFormulaLimitOrder,),
        }

    attribute_map = {
        "count": "count",
        "order": "order",
    }

    def __init__(
        self_,
        count: Union[int, UnsetType] = unset,
        order: Union[TimeseriesAnomalyInvestigationFormulaLimitOrder, UnsetType] = unset,
        **kwargs,
    ):
        """
        Optional formula limit accepted for compatibility with Timeseries API requests. Formula limits have no effect on timeseries queries.

        :param count: Requested result limit. This field has no effect on a timeseries anomaly investigation.
        :type count: int, optional

        :param order: Sort order used when applying a formula series limit.
        :type order: TimeseriesAnomalyInvestigationFormulaLimitOrder, optional
        """
        if count is not unset:
            kwargs["count"] = count
        if order is not unset:
            kwargs["order"] = order
        super().__init__(kwargs)
