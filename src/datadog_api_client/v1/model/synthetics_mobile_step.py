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
    from datadog_api_client.v1.model.synthetics_mobile_step_params import SyntheticsMobileStepParams
    from datadog_api_client.v1.model.synthetics_mobile_step_type import SyntheticsMobileStepType


class SyntheticsMobileStep(ModelNormal):
    validations = {
        "name": {
            "max_length": 1500,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.synthetics_mobile_step_params import SyntheticsMobileStepParams
        from datadog_api_client.v1.model.synthetics_mobile_step_type import SyntheticsMobileStepType

        return {
            "allow_failure": (bool,),
            "has_new_step_element": (bool,),
            "is_critical": (bool,),
            "name": (str,),
            "no_screenshot": (bool,),
            "params": (SyntheticsMobileStepParams,),
            "public_id": (str,),
            "timeout": (int,),
            "type": (SyntheticsMobileStepType,),
        }

    attribute_map = {
        "allow_failure": "allowFailure",
        "has_new_step_element": "hasNewStepElement",
        "is_critical": "isCritical",
        "name": "name",
        "no_screenshot": "noScreenshot",
        "params": "params",
        "public_id": "publicId",
        "timeout": "timeout",
        "type": "type",
    }

    def __init__(
        self_,
        name: str,
        params: SyntheticsMobileStepParams,
        type: SyntheticsMobileStepType,
        allow_failure: Union[bool, UnsetType] = unset,
        has_new_step_element: Union[bool, UnsetType] = unset,
        is_critical: Union[bool, UnsetType] = unset,
        no_screenshot: Union[bool, UnsetType] = unset,
        public_id: Union[str, UnsetType] = unset,
        timeout: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        The steps used in a Synthetic mobile test.

        :param allow_failure: A boolean set to allow this step to fail.
        :type allow_failure: bool, optional

        :param has_new_step_element: A boolean set to determine if the step has a new step element.
        :type has_new_step_element: bool, optional

        :param is_critical: A boolean to use in addition to ``allowFailure`` to determine if the test should be marked as failed when the step fails.
        :type is_critical: bool, optional

        :param name: The name of the step.
        :type name: str

        :param no_screenshot: A boolean set to not take a screenshot for the step.
        :type no_screenshot: bool, optional

        :param params: The parameters of a mobile step.
        :type params: SyntheticsMobileStepParams

        :param public_id: The public ID of the step.
        :type public_id: str, optional

        :param timeout: The time before declaring a step failed.
        :type timeout: int, optional

        :param type: Step type used in your mobile Synthetic test.
        :type type: SyntheticsMobileStepType
        """
        if allow_failure is not unset:
            kwargs["allow_failure"] = allow_failure
        if has_new_step_element is not unset:
            kwargs["has_new_step_element"] = has_new_step_element
        if is_critical is not unset:
            kwargs["is_critical"] = is_critical
        if no_screenshot is not unset:
            kwargs["no_screenshot"] = no_screenshot
        if public_id is not unset:
            kwargs["public_id"] = public_id
        if timeout is not unset:
            kwargs["timeout"] = timeout
        super().__init__(kwargs)

        self_.name = name
        self_.params = params
        self_.type = type
