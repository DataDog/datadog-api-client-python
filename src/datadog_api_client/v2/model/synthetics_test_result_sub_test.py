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
    from datadog_api_client.v2.model.synthetics_test_result_rum_context import SyntheticsTestResultRumContext


class SyntheticsTestResultSubTest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.synthetics_test_result_rum_context import SyntheticsTestResultRumContext

        return {
            "id": (str,),
            "playing_tab": (int,),
            "rum_context": (SyntheticsTestResultRumContext,),
        }

    attribute_map = {
        "id": "id",
        "playing_tab": "playing_tab",
        "rum_context": "rum_context",
    }

    def __init__(
        self_,
        id: Union[str, UnsetType] = unset,
        playing_tab: Union[int, UnsetType] = unset,
        rum_context: Union[SyntheticsTestResultRumContext, UnsetType] = unset,
        **kwargs,
    ):
        """
        Information about a sub-test played from a parent browser test.

        :param id: Identifier of the sub-test.
        :type id: str, optional

        :param playing_tab: Index of the browser tab playing the sub-test.
        :type playing_tab: int, optional

        :param rum_context: RUM application context associated with a step or sub-test.
        :type rum_context: SyntheticsTestResultRumContext, optional
        """
        if id is not unset:
            kwargs["id"] = id
        if playing_tab is not unset:
            kwargs["playing_tab"] = playing_tab
        if rum_context is not unset:
            kwargs["rum_context"] = rum_context
        super().__init__(kwargs)
