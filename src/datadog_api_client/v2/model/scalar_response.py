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


from datadog_api_client.v2.model.scalar_column import ScalarColumn
from datadog_api_client.v2.model.scalar_formula_response_atrributes import ScalarFormulaResponseAtrributes
from datadog_api_client.v2.model.scalar_column import ScalarColumn
from datadog_api_client.v2.model.group_scalar_column import GroupScalarColumn
from datadog_api_client.v2.model.data_scalar_column import DataScalarColumn

if TYPE_CHECKING:
    from datadog_api_client.v2.model.scalar_formula_response_type import ScalarFormulaResponseType


@dataclass
class ScalarResponseJSON:
    columns: Union[List[Union[ScalarColumn, GroupScalarColumn, DataScalarColumn]], UnsetType] = unset


class ScalarResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.scalar_formula_response_type import ScalarFormulaResponseType

        return {
            "attributes": (ScalarFormulaResponseAtrributes,),
            "type": (ScalarFormulaResponseType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }
    json_api_model = ScalarResponseJSON

    def __init__(
        self_,
        attributes: Union[ScalarFormulaResponseAtrributes, UnsetType] = unset,
        type: Union[ScalarFormulaResponseType, UnsetType] = unset,
        **kwargs,
    ):
        """
        A message containing the response to a scalar query.

        :param attributes: The object describing a scalar response.
        :type attributes: ScalarFormulaResponseAtrributes, optional

        :param type: The type of the resource. The value should always be scalar_response.
        :type type: ScalarFormulaResponseType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
