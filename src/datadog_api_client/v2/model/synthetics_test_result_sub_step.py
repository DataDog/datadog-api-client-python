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
    from datadog_api_client.v2.model.synthetics_test_result_parent_step import SyntheticsTestResultParentStep
    from datadog_api_client.v2.model.synthetics_test_result_parent_test import SyntheticsTestResultParentTest


class SyntheticsTestResultSubStep(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.synthetics_test_result_parent_step import SyntheticsTestResultParentStep
        from datadog_api_client.v2.model.synthetics_test_result_parent_test import SyntheticsTestResultParentTest

        return {
            "level": (int,),
            "parent_step": (SyntheticsTestResultParentStep,),
            "parent_test": (SyntheticsTestResultParentTest,),
        }

    attribute_map = {
        "level": "level",
        "parent_step": "parent_step",
        "parent_test": "parent_test",
    }

    def __init__(
        self_,
        level: Union[int, UnsetType] = unset,
        parent_step: Union[SyntheticsTestResultParentStep, UnsetType] = unset,
        parent_test: Union[SyntheticsTestResultParentTest, UnsetType] = unset,
        **kwargs,
    ):
        """
        Information about a sub-step in a nested test execution.

        :param level: Depth of the sub-step in the execution tree.
        :type level: int, optional

        :param parent_step: Reference to the parent step of a sub-step.
        :type parent_step: SyntheticsTestResultParentStep, optional

        :param parent_test: Reference to the parent test of a sub-step.
        :type parent_test: SyntheticsTestResultParentTest, optional
        """
        if level is not unset:
            kwargs["level"] = level
        if parent_step is not unset:
            kwargs["parent_step"] = parent_step
        if parent_test is not unset:
            kwargs["parent_test"] = parent_test
        super().__init__(kwargs)
