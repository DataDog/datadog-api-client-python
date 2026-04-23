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
    from datadog_api_client.v2.model.synthetics_test_result_bounds import SyntheticsTestResultBounds


class SyntheticsTestResultWarning(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.synthetics_test_result_bounds import SyntheticsTestResultBounds

        return {
            "element_bounds": ([SyntheticsTestResultBounds],),
            "message": (str,),
            "type": (str,),
        }

    attribute_map = {
        "element_bounds": "element_bounds",
        "message": "message",
        "type": "type",
    }

    def __init__(
        self_,
        element_bounds: Union[List[SyntheticsTestResultBounds], UnsetType] = unset,
        message: Union[str, UnsetType] = unset,
        type: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        A warning captured during a browser test step.

        :param element_bounds: Bounds of elements related to the warning.
        :type element_bounds: [SyntheticsTestResultBounds], optional

        :param message: Warning message.
        :type message: str, optional

        :param type: Type of the warning.
        :type type: str, optional
        """
        if element_bounds is not unset:
            kwargs["element_bounds"] = element_bounds
        if message is not unset:
            kwargs["message"] = message
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
