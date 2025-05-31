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


class SyntheticsAssertionXPathTargetTarget(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.synthetics_assertion_target_value import SyntheticsAssertionTargetValue

        return {
            "operator": (str,),
            "target_value": (SyntheticsAssertionTargetValue,),
            "x_path": (str,),
        }

    attribute_map = {
        "operator": "operator",
        "target_value": "targetValue",
        "x_path": "xPath",
    }

    def __init__(
        self_,
        operator: Union[str, UnsetType] = unset,
        target_value: Union[SyntheticsAssertionTargetValue, float, str, UnsetType] = unset,
        x_path: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Composed target for ``validatesXPath`` operator.

        :param operator: The specific operator to use on the path.
        :type operator: str, optional

        :param target_value: Value used by the operator in assertions. Can be either a number or string.
        :type target_value: SyntheticsAssertionTargetValue, optional

        :param x_path: The X path to assert.
        :type x_path: str, optional
        """
        if operator is not unset:
            kwargs["operator"] = operator
        if target_value is not unset:
            kwargs["target_value"] = target_value
        if x_path is not unset:
            kwargs["x_path"] = x_path
        super().__init__(kwargs)
