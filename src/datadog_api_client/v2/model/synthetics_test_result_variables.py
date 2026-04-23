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
    from datadog_api_client.v2.model.synthetics_test_result_variable import SyntheticsTestResultVariable


class SyntheticsTestResultVariables(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.synthetics_test_result_variable import SyntheticsTestResultVariable

        return {
            "config": ([SyntheticsTestResultVariable],),
            "extracted": ([SyntheticsTestResultVariable],),
        }

    attribute_map = {
        "config": "config",
        "extracted": "extracted",
    }

    def __init__(
        self_,
        config: Union[List[SyntheticsTestResultVariable], UnsetType] = unset,
        extracted: Union[List[SyntheticsTestResultVariable], UnsetType] = unset,
        **kwargs,
    ):
        """
        Variables captured during a test step.

        :param config: Variables defined in the test configuration.
        :type config: [SyntheticsTestResultVariable], optional

        :param extracted: Variables extracted during the test execution.
        :type extracted: [SyntheticsTestResultVariable], optional
        """
        if config is not unset:
            kwargs["config"] = config
        if extracted is not unset:
            kwargs["extracted"] = extracted
        super().__init__(kwargs)
