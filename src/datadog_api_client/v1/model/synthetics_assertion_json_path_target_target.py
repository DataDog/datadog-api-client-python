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
    from datadog_api_client.v1.model.synthetics_assertion_target_value import SyntheticsAssertionTargetValue


class SyntheticsAssertionJSONPathTargetTarget(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.synthetics_assertion_target_value import SyntheticsAssertionTargetValue

        return {
            "elements_operator": (str,),
            "json_path": (str,),
            "operator": (str,),
            "target_value": (SyntheticsAssertionTargetValue,),
        }

    attribute_map = {
        "elements_operator": "elementsOperator",
        "json_path": "jsonPath",
        "operator": "operator",
        "target_value": "targetValue",
    }

    def __init__(
        self_,
        elements_operator: Union[str, UnsetType] = unset,
        json_path: Union[str, UnsetType] = unset,
        operator: Union[str, UnsetType] = unset,
        target_value: Union[SyntheticsAssertionTargetValue, float, str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Composed target for ``validatesJSONPath`` operator.

        :param elements_operator: The element from the list of results to assert on.  To choose from the first element in the list ``firstElementMatches`` , every element in the list ``everyElementMatches`` , at least one element in the list ``atLeastOneElementMatches`` or the serialized value of the list ``serializationMatches``.
        :type elements_operator: str, optional

        :param json_path: The JSON path to assert.
        :type json_path: str, optional

        :param operator: The specific operator to use on the path.
        :type operator: str, optional

        :param target_value: Value used by the operator in assertions. Can be either a number or string.
        :type target_value: SyntheticsAssertionTargetValue, optional
        """
        if elements_operator is not unset:
            kwargs["elements_operator"] = elements_operator
        if json_path is not unset:
            kwargs["json_path"] = json_path
        if operator is not unset:
            kwargs["operator"] = operator
        if target_value is not unset:
            kwargs["target_value"] = target_value
        super().__init__(kwargs)
