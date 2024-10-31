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
    from datadog_api_client.v1.model.synthetics_check_type import SyntheticsCheckType
    from datadog_api_client.v1.model.synthetics_mobile_step_params_direction import SyntheticsMobileStepParamsDirection
    from datadog_api_client.v1.model.synthetics_mobile_step_params_element import SyntheticsMobileStepParamsElement
    from datadog_api_client.v1.model.synthetics_mobile_step_params_positions_items import (
        SyntheticsMobileStepParamsPositionsItems,
    )
    from datadog_api_client.v1.model.synthetics_mobile_step_params_value import SyntheticsMobileStepParamsValue
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
        from datadog_api_client.v1.model.synthetics_check_type import SyntheticsCheckType
        from datadog_api_client.v1.model.synthetics_mobile_step_params_direction import (
            SyntheticsMobileStepParamsDirection,
        )
        from datadog_api_client.v1.model.synthetics_mobile_step_params_element import SyntheticsMobileStepParamsElement
        from datadog_api_client.v1.model.synthetics_mobile_step_params_positions_items import (
            SyntheticsMobileStepParamsPositionsItems,
        )
        from datadog_api_client.v1.model.synthetics_mobile_step_params_value import SyntheticsMobileStepParamsValue
        from datadog_api_client.v1.model.synthetics_mobile_step_params_variable import (
            SyntheticsMobileStepParamsVariable,
        )

        return {
            "check": (SyntheticsCheckType,),
            "delay": (int,),
            "direction": (SyntheticsMobileStepParamsDirection,),
            "element": (SyntheticsMobileStepParamsElement,),
            "enabled": (bool,),
            "max_scrolls": (int,),
            "positions": ([SyntheticsMobileStepParamsPositionsItems],),
            "subtest_public_id": (str,),
            "value": (SyntheticsMobileStepParamsValue,),
            "variable": (SyntheticsMobileStepParamsVariable,),
            "with_enter": (bool,),
            "x": (float,),
            "y": (float,),
        }

    attribute_map = {
        "check": "check",
        "delay": "delay",
        "direction": "direction",
        "element": "element",
        "enabled": "enabled",
        "max_scrolls": "maxScrolls",
        "positions": "positions",
        "subtest_public_id": "subtestPublicId",
        "value": "value",
        "variable": "variable",
        "with_enter": "withEnter",
        "x": "x",
        "y": "y",
    }

    def __init__(
        self_,
        check: Union[SyntheticsCheckType, UnsetType] = unset,
        delay: Union[int, UnsetType] = unset,
        direction: Union[SyntheticsMobileStepParamsDirection, UnsetType] = unset,
        element: Union[SyntheticsMobileStepParamsElement, UnsetType] = unset,
        enabled: Union[bool, UnsetType] = unset,
        max_scrolls: Union[int, UnsetType] = unset,
        positions: Union[List[SyntheticsMobileStepParamsPositionsItems], UnsetType] = unset,
        subtest_public_id: Union[str, UnsetType] = unset,
        value: Union[SyntheticsMobileStepParamsValue, str, int, UnsetType] = unset,
        variable: Union[SyntheticsMobileStepParamsVariable, UnsetType] = unset,
        with_enter: Union[bool, UnsetType] = unset,
        x: Union[float, UnsetType] = unset,
        y: Union[float, UnsetType] = unset,
        **kwargs,
    ):
        """
        The parameters of a mobile step.

        :param check: Type of assertion to apply in an API test.
        :type check: SyntheticsCheckType, optional

        :param delay: Number of milliseconds to wait between inputs in a ``typeText`` step type.
        :type delay: int, optional

        :param direction: The direction of the scroll for a ``scrollToElement`` step type.
        :type direction: SyntheticsMobileStepParamsDirection, optional

        :param element: Information about the element used for a step.
        :type element: SyntheticsMobileStepParamsElement, optional

        :param enabled: Boolean to change the state of the wifi for a ``toggleWiFi`` step type.
        :type enabled: bool, optional

        :param max_scrolls: Maximum number of scrolls to do for a ``scrollToElement`` step type.
        :type max_scrolls: int, optional

        :param positions: List of positions for the ``flick`` step type. The maximum is 10 flicks per step
        :type positions: [SyntheticsMobileStepParamsPositionsItems], optional

        :param subtest_public_id: Public ID of the test to be played as part of a ``playSubTest`` step type.
        :type subtest_public_id: str, optional

        :param value: Values used in the step for in multiple step types.
        :type value: SyntheticsMobileStepParamsValue, optional

        :param variable: Variable object for ``extractVariable`` step type.
        :type variable: SyntheticsMobileStepParamsVariable, optional

        :param with_enter: Boolean to indicate if ``Enter`` should be pressed at the end of the ``typeText`` step type.
        :type with_enter: bool, optional

        :param x: Amount to scroll by on the ``x`` axis for a ``scroll`` step type.
        :type x: float, optional

        :param y: Amount to scroll by on the ``y`` axis for a ``scroll`` step type.
        :type y: float, optional
        """
        if check is not unset:
            kwargs["check"] = check
        if delay is not unset:
            kwargs["delay"] = delay
        if direction is not unset:
            kwargs["direction"] = direction
        if element is not unset:
            kwargs["element"] = element
        if enabled is not unset:
            kwargs["enabled"] = enabled
        if max_scrolls is not unset:
            kwargs["max_scrolls"] = max_scrolls
        if positions is not unset:
            kwargs["positions"] = positions
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
