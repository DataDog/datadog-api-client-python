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
    from datadog_api_client.v1.model.synthetics_step_type import SyntheticsStepType


class SyntheticsStep(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.synthetics_step_type import SyntheticsStepType

        return {
            "allow_failure": (bool,),
            "always_execute": (bool,),
            "exit_if_succeed": (bool,),
            "is_critical": (bool,),
            "name": (str,),
            "no_screenshot": (bool,),
            "params": (dict,),
            "public_id": (str,),
            "timeout": (int,),
            "type": (SyntheticsStepType,),
        }

    attribute_map = {
        "allow_failure": "allowFailure",
        "always_execute": "alwaysExecute",
        "exit_if_succeed": "exitIfSucceed",
        "is_critical": "isCritical",
        "name": "name",
        "no_screenshot": "noScreenshot",
        "params": "params",
        "public_id": "public_id",
        "timeout": "timeout",
        "type": "type",
    }

    def __init__(
        self_,
        allow_failure: Union[bool, UnsetType] = unset,
        always_execute: Union[bool, UnsetType] = unset,
        exit_if_succeed: Union[bool, UnsetType] = unset,
        is_critical: Union[bool, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        no_screenshot: Union[bool, UnsetType] = unset,
        params: Union[dict, UnsetType] = unset,
        public_id: Union[str, UnsetType] = unset,
        timeout: Union[int, UnsetType] = unset,
        type: Union[SyntheticsStepType, UnsetType] = unset,
        **kwargs,
    ):
        """
        The steps used in a Synthetic browser test.

        :param allow_failure: A boolean set to allow this step to fail.
        :type allow_failure: bool, optional

        :param always_execute: A boolean set to always execute this step even if the previous step failed or was skipped.
        :type always_execute: bool, optional

        :param exit_if_succeed: A boolean set to exit the test if the step succeeds.
        :type exit_if_succeed: bool, optional

        :param is_critical: A boolean to use in addition to ``allowFailure`` to determine if the test should be marked as failed when the step fails.
        :type is_critical: bool, optional

        :param name: The name of the step.
        :type name: str, optional

        :param no_screenshot: A boolean set to skip taking a screenshot for the step.
        :type no_screenshot: bool, optional

        :param params: The parameters of the step.
        :type params: dict, optional

        :param public_id: The public ID of the step.
        :type public_id: str, optional

        :param timeout: The time before declaring a step failed.
        :type timeout: int, optional

        :param type: Step type used in your Synthetic test.
        :type type: SyntheticsStepType, optional
        """
        if allow_failure is not unset:
            kwargs["allow_failure"] = allow_failure
        if always_execute is not unset:
            kwargs["always_execute"] = always_execute
        if exit_if_succeed is not unset:
            kwargs["exit_if_succeed"] = exit_if_succeed
        if is_critical is not unset:
            kwargs["is_critical"] = is_critical
        if name is not unset:
            kwargs["name"] = name
        if no_screenshot is not unset:
            kwargs["no_screenshot"] = no_screenshot
        if params is not unset:
            kwargs["params"] = params
        if public_id is not unset:
            kwargs["public_id"] = public_id
        if timeout is not unset:
            kwargs["timeout"] = timeout
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
