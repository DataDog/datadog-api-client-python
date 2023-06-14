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
from datadog_api_client.v2.model.scalar_formula_request_queries import ScalarFormulaRequestQueries
from datadog_api_client.v2.model.scalar_formula_request_attributes import ScalarFormulaRequestAttributes
from datadog_api_client.v2.model.query_formula import QueryFormula
from datadog_api_client.v2.model.scalar_formula_request_queries import ScalarFormulaRequestQueries

if TYPE_CHECKING:
    from datadog_api_client.v2.model.scalar_formula_request_type import ScalarFormulaRequestType


@dataclass
class ScalarFormulaRequestJSON:
    formulas: Union[List[QueryFormula], UnsetType] = unset
    _from: Union[int, UnsetType] = unset
    queries: Union[ScalarFormulaRequestQueries, UnsetType] = unset
    to: Union[int, UnsetType] = unset


class ScalarFormulaRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.scalar_formula_request_type import ScalarFormulaRequestType

        return {
            "attributes": (ScalarFormulaRequestAttributes,),
            "type": (ScalarFormulaRequestType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }
    json_api_model = ScalarFormulaRequestJSON

    def __init__(self_, attributes: ScalarFormulaRequestAttributes, type: ScalarFormulaRequestType, **kwargs):
        """
        A single scalar query to be executed.

        :param attributes: The object describing a scalar formula request.
        :type attributes: ScalarFormulaRequestAttributes

        :param type: The type of the resource. The value should always be scalar_request.
        :type type: ScalarFormulaRequestType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
