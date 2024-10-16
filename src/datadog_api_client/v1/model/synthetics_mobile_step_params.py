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
    from datadog_api_client.v1.model.synthetics_mobile_step_params_check import SyntheticsMobileStepParamsCheck
    from datadog_api_client.v1.model.synthetics_mobile_step_params_direction import SyntheticsMobileStepParamsDirection
    from datadog_api_client.v1.model.synthetics_mobile_step_params_element import SyntheticsMobileStepParamsElement
    from datadog_api_client.v1.model.synthetics_mobile_step_params_position import SyntheticsMobileStepParamsPosition
    from datadog_api_client.v1.model.synthetics_mobile_step_params_variable import SyntheticsMobileStepParamsVariable


class SyntheticsMobileStepParams(ModelNormal):
    validations = {
        "delay": {
            "inclusive_maximum": 5000,
            "inclusive_minimum": 0,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.synthetics_mobile_step_params_check import SyntheticsMobileStepParamsCheck
        from datadog_api_client.v1.model.synthetics_mobile_step_params_direction import (
            SyntheticsMobileStepParamsDirection,
        )
        from datadog_api_client.v1.model.synthetics_mobile_step_params_element import SyntheticsMobileStepParamsElement
        from datadog_api_client.v1.model.synthetics_mobile_step_params_position import (
            SyntheticsMobileStepParamsPosition,
        )
        from datadog_api_client.v1.model.synthetics_mobile_step_params_variable import (
            SyntheticsMobileStepParamsVariable,
        )

        return {
            "check": (SyntheticsMobileStepParamsCheck,),
            "delay": (int,),
            "direction": (SyntheticsMobileStepParamsDirection,),
            "element": (SyntheticsMobileStepParamsElement,),
            "enable": (bool,),
            "max_scrolls": (int,),
            "position": (SyntheticsMobileStepParamsPosition,),
            "subtest_public_id": (str,),
            "value": (str,),
            "variable": (SyntheticsMobileStepParamsVariable,),
            "with_enter": (bool,),
            "x": (int,),
            "y": (int,),
        }

    attribute_map = {
        "check": "check",
        "delay": "delay",
        "direction": "direction",
        "element": "element",
        "enable": "enable",
        "max_scrolls": "maxScrolls",
        "position": "position",
        "subtest_public_id": "subtestPublicId",
        "value": "value",
        "variable": "variable",
        "with_enter": "withEnter",
        "x": "x",
        "y": "y",
    }

    def __init__(
        self_,
        check: Union[SyntheticsMobileStepParamsCheck, UnsetType] = unset,
        delay: Union[int, UnsetType] = unset,
        direction: Union[SyntheticsMobileStepParamsDirection, UnsetType] = unset,
        element: Union[SyntheticsMobileStepParamsElement, UnsetType] = unset,
        enable: Union[bool, UnsetType] = unset,
        max_scrolls: Union[int, UnsetType] = unset,
        position: Union[SyntheticsMobileStepParamsPosition, UnsetType] = unset,
        subtest_public_id: Union[str, UnsetType] = unset,
        value: Union[str, UnsetType] = unset,
        variable: Union[SyntheticsMobileStepParamsVariable, UnsetType] = unset,
        with_enter: Union[bool, UnsetType] = unset,
        x: Union[int, UnsetType] = unset,
        y: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        The parameters of a mobile step.

        :param check: The definition of ``SyntheticsMobileStepParamsCheck`` object.
        :type check: SyntheticsMobileStepParamsCheck, optional

        :param delay: The ``SyntheticsMobileStepParams`` ``delay``.
        :type delay: int, optional

        :param direction: The definition of ``SyntheticsMobileStepParamsDirection`` object.
        :type direction: SyntheticsMobileStepParamsDirection, optional

        :param element: The definition of ``SyntheticsMobileStepParamsElement`` object.
        :type element: SyntheticsMobileStepParamsElement, optional

        :param enable: The ``SyntheticsMobileStepParams`` ``enable``.
        :type enable: bool, optional

        :param max_scrolls: The ``SyntheticsMobileStepParams`` ``maxScrolls``.
        :type max_scrolls: int, optional

        :param position: The definition of ``SyntheticsMobileStepParamsPosition`` object.
        :type position: SyntheticsMobileStepParamsPosition, optional

        :param subtest_public_id: The ``SyntheticsMobileStepParams`` ``subtestPublicId``.
        :type subtest_public_id: str, optional

        :param value: The ``SyntheticsMobileStepParams`` ``value``.
        :type value: str, optional

        :param variable: The definition of ``SyntheticsMobileStepParamsVariable`` object.
        :type variable: SyntheticsMobileStepParamsVariable, optional

        :param with_enter: The ``SyntheticsMobileStepParams`` ``withEnter``.
        :type with_enter: bool, optional

        :param x: The ``SyntheticsMobileStepParams`` ``x``.
        :type x: int, optional

        :param y: The ``SyntheticsMobileStepParams`` ``y``.
        :type y: int, optional
        """
        if check is not unset:
            kwargs["check"] = check
        if delay is not unset:
            kwargs["delay"] = delay
        if direction is not unset:
            kwargs["direction"] = direction
        if element is not unset:
            kwargs["element"] = element
        if enable is not unset:
            kwargs["enable"] = enable
        if max_scrolls is not unset:
            kwargs["max_scrolls"] = max_scrolls
        if position is not unset:
            kwargs["position"] = position
        if subtest_public_id is not unset:
            kwargs["subtest_public_id"] = subtest_public_id
        if value is not unset:
            kwargs["value"] = value
        if variable is not unset:
            kwargs["variable"] = variable
        if with_enter is not unset:
            kwargs["with_enter"] = with_enter
        if x is not unset:
            kwargs["x"] = x
        if y is not unset:
            kwargs["y"] = y
        super().__init__(kwargs)
