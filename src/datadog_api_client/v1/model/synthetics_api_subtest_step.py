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
    from datadog_api_client.v1.model.synthetics_test_options_retry import SyntheticsTestOptionsRetry
    from datadog_api_client.v1.model.synthetics_api_subtest_step_subtype import SyntheticsAPISubtestStepSubtype


class SyntheticsAPISubtestStep(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.synthetics_test_options_retry import SyntheticsTestOptionsRetry
        from datadog_api_client.v1.model.synthetics_api_subtest_step_subtype import SyntheticsAPISubtestStepSubtype

        return {
            "allow_failure": (bool,),
            "always_execute": (bool,),
            "exit_if_succeed": (bool,),
            "extracted_values_from_script": (str,),
            "id": (str,),
            "is_critical": (bool,),
            "name": (str,),
            "retry": (SyntheticsTestOptionsRetry,),
            "subtest_public_id": (str,),
            "subtype": (SyntheticsAPISubtestStepSubtype,),
        }

    attribute_map = {
        "allow_failure": "allowFailure",
        "always_execute": "alwaysExecute",
        "exit_if_succeed": "exitIfSucceed",
        "extracted_values_from_script": "extractedValuesFromScript",
        "id": "id",
        "is_critical": "isCritical",
        "name": "name",
        "retry": "retry",
        "subtest_public_id": "subtestPublicId",
        "subtype": "subtype",
    }
    read_only_vars = {
        "id",
    }

    def __init__(
        self_,
        name: str,
        subtest_public_id: str,
        subtype: SyntheticsAPISubtestStepSubtype,
        allow_failure: Union[bool, UnsetType] = unset,
        always_execute: Union[bool, UnsetType] = unset,
        exit_if_succeed: Union[bool, UnsetType] = unset,
        extracted_values_from_script: Union[str, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        is_critical: Union[bool, UnsetType] = unset,
        retry: Union[SyntheticsTestOptionsRetry, UnsetType] = unset,
        **kwargs,
    ):
        """
        The subtest step used in a Synthetics multi-step API test.

        :param allow_failure: Determines whether or not to continue with test if this step fails.
        :type allow_failure: bool, optional

        :param always_execute: A boolean set to always execute this step even if the previous step failed or was skipped.
        :type always_execute: bool, optional

        :param exit_if_succeed: Determines whether or not to exit the test if the step succeeds.
        :type exit_if_succeed: bool, optional

        :param extracted_values_from_script: Generate variables using JavaScript.
        :type extracted_values_from_script: str, optional

        :param id: ID of the step.
        :type id: str, optional

        :param is_critical: Determines whether or not to consider the entire test as failed if this step fails.
            Can be used only if ``allowFailure`` is ``true``.
        :type is_critical: bool, optional

        :param name: The name of the step.
        :type name: str

        :param retry: Object describing the retry strategy to apply to a Synthetic test.
        :type retry: SyntheticsTestOptionsRetry, optional

        :param subtest_public_id: Public ID of the test to be played as part of a ``playSubTest`` step type.
        :type subtest_public_id: str

        :param subtype: The subtype of the Synthetic multi-step API subtest step.
        :type subtype: SyntheticsAPISubtestStepSubtype
        """
        if allow_failure is not unset:
            kwargs["allow_failure"] = allow_failure
        if always_execute is not unset:
            kwargs["always_execute"] = always_execute
        if exit_if_succeed is not unset:
            kwargs["exit_if_succeed"] = exit_if_succeed
        if extracted_values_from_script is not unset:
            kwargs["extracted_values_from_script"] = extracted_values_from_script
        if id is not unset:
            kwargs["id"] = id
        if is_critical is not unset:
            kwargs["is_critical"] = is_critical
        if retry is not unset:
            kwargs["retry"] = retry
        super().__init__(kwargs)

        self_.name = name
        self_.subtest_public_id = subtest_public_id
        self_.subtype = subtype
