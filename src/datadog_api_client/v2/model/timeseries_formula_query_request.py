# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from dataclasses import dataclass
from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


from datadog_api_client.v2.model.query_formula import QueryFormula
from datadog_api_client.v2.model.timeseries_formula_request_queries import TimeseriesFormulaRequestQueries
from datadog_api_client.v2.model.query_formula import QueryFormula
from datadog_api_client.v2.model.timeseries_formula_request_queries import TimeseriesFormulaRequestQueries

if TYPE_CHECKING:
    from datadog_api_client.v2.model.timeseries_formula_request import TimeseriesFormulaRequest


@dataclass
class TimeseriesFormulaQueryRequestJSON:
    formulas: Union[List[QueryFormula], UnsetType] = unset
    _from: Union[int, UnsetType] = unset
    interval: Union[int, UnsetType] = unset
    queries: Union[TimeseriesFormulaRequestQueries, UnsetType] = unset
    to: Union[int, UnsetType] = unset


class TimeseriesFormulaQueryRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.timeseries_formula_request import TimeseriesFormulaRequest

        return {
            "data": (TimeseriesFormulaRequest,),
        }

    attribute_map = {
        "data": "data",
    }
    json_api_model = TimeseriesFormulaQueryRequestJSON

    def __init__(self_, data: TimeseriesFormulaRequest, **kwargs):
        """
        A request wrapper around a single timeseries query to be executed.

        :param data: A single timeseries query to be executed.
        :type data: TimeseriesFormulaRequest
        """
        super().__init__(kwargs)

        self_.data = data
