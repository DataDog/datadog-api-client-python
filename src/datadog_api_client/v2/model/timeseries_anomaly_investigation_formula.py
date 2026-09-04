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
    from datadog_api_client.v2.model.timeseries_anomaly_investigation_formula_limit import (
        TimeseriesAnomalyInvestigationFormulaLimit,
    )


class TimeseriesAnomalyInvestigationFormula(ModelNormal):
    validations = {
        "formula": {
            "min_length": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.timeseries_anomaly_investigation_formula_limit import (
            TimeseriesAnomalyInvestigationFormulaLimit,
        )

        return {
            "formula": (str,),
            "limit": (TimeseriesAnomalyInvestigationFormulaLimit,),
        }

    attribute_map = {
        "formula": "formula",
        "limit": "limit",
    }

    def __init__(
        self_, formula: str, limit: Union[TimeseriesAnomalyInvestigationFormulaLimit, UnsetType] = unset, **kwargs
    ):
        """
        Formula evaluated by the timeseries request.

        :param formula: Formula expression referencing one or more named queries.
        :type formula: str

        :param limit: Optional formula limit accepted for compatibility with Timeseries API requests. Formula limits have no effect on timeseries queries.
        :type limit: TimeseriesAnomalyInvestigationFormulaLimit, optional
        """
        if limit is not unset:
            kwargs["limit"] = limit
        super().__init__(kwargs)

        self_.formula = formula
