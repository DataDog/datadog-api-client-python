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
    from datadog_api_client.v2.model.scalar_formula_response_atrributes import ScalarFormulaResponseAtrributes
    from datadog_api_client.v2.model.scalar_formula_response_type import ScalarFormulaResponseType


class ScalarResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.scalar_formula_response_atrributes import ScalarFormulaResponseAtrributes
        from datadog_api_client.v2.model.scalar_formula_response_type import ScalarFormulaResponseType

        return {
            "attributes": (ScalarFormulaResponseAtrributes,),
            "id": (str,),
            "type": (ScalarFormulaResponseType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[ScalarFormulaResponseAtrributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        type: Union[ScalarFormulaResponseType, UnsetType] = unset,
        **kwargs,
    ):
        """
        A message containing the response to a scalar query.

        :param attributes: The object describing a scalar response.
        :type attributes: ScalarFormulaResponseAtrributes, optional

        :param id: The identifier of the scalar response resource.
        :type id: str, optional

        :param type: The type of the resource. The value should always be scalar_response.
        :type type: ScalarFormulaResponseType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
