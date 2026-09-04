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
    from datadog_api_client.v2.model.timeseries_anomaly_investigation_formula import (
        TimeseriesAnomalyInvestigationFormula,
    )
    from datadog_api_client.v2.model.timeseries_anomaly_investigation_metric_query import (
        TimeseriesAnomalyInvestigationMetricQuery,
    )


class TimeseriesAnomalyInvestigationTimeseriesRequest(ModelNormal):
    validations = {
        "formulas": {
            "min_items": 1,
        },
        "interval": {
            "inclusive_minimum": 1,
        },
        "queries": {
            "min_items": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.timeseries_anomaly_investigation_formula import (
            TimeseriesAnomalyInvestigationFormula,
        )
        from datadog_api_client.v2.model.timeseries_anomaly_investigation_metric_query import (
            TimeseriesAnomalyInvestigationMetricQuery,
        )

        return {
            "formulas": ([TimeseriesAnomalyInvestigationFormula],),
            "_from": (int,),
            "interval": (int,),
            "queries": ([TimeseriesAnomalyInvestigationMetricQuery],),
            "to": (int,),
        }

    attribute_map = {
        "formulas": "formulas",
        "_from": "from",
        "interval": "interval",
        "queries": "queries",
        "to": "to",
    }

    def __init__(
        self_,
        formulas: List[TimeseriesAnomalyInvestigationFormula],
        _from: int,
        queries: List[TimeseriesAnomalyInvestigationMetricQuery],
        to: int,
        interval: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Metrics timeseries request to investigate.

        :param formulas: Formulas to evaluate. Each formula may contain an explicit ``anomalies()`` call or a supported metrics expression.
        :type formulas: [TimeseriesAnomalyInvestigationFormula]

        :param _from: Start of the investigation time window in milliseconds since the Unix epoch.
        :type _from: int

        :param interval: Optional requested aggregation interval in milliseconds.
        :type interval: int, optional

        :param queries: Metrics queries referenced by the formulas.
        :type queries: [TimeseriesAnomalyInvestigationMetricQuery]

        :param to: End of the investigation time window in milliseconds since the Unix epoch. Must be later than ``from``.
        :type to: int
        """
        if interval is not unset:
            kwargs["interval"] = interval
        super().__init__(kwargs)

        self_.formulas = formulas
        self_._from = _from
        self_.queries = queries
        self_.to = to
