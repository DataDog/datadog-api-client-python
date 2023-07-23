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


if TYPE_CHECKING:
    from datadog_api_client.v2.model.scalar_formula_request import ScalarFormulaRequest
    from datadog_api_client.v2.model.query_formula import QueryFormula
    from datadog_api_client.v2.model.scalar_formula_request_queries import ScalarFormulaRequestQueries


@dataclass
class ScalarFormulaQueryRequestJSON:
    formulas: Union[List[QueryFormula], UnsetType] = unset
    _from: Union[int, UnsetType] = unset
    queries: Union[ScalarFormulaRequestQueries, UnsetType] = unset
    to: Union[int, UnsetType] = unset


class ScalarFormulaQueryRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.scalar_formula_request import ScalarFormulaRequest

        return {
            "data": (ScalarFormulaRequest,),
        }

    attribute_map = {
        "data": "data",
    }
    json_api_model = ScalarFormulaQueryRequestJSON

    def __init__(self_, data: ScalarFormulaRequest, **kwargs):
        """
        A wrapper request around one scalar query to be executed.

        :param data: A single scalar query to be executed.
        :type data: ScalarFormulaRequest
        """
        super().__init__(kwargs)

        self_.data = data
