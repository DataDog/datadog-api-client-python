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
    from datadog_api_client.v2.model.synthetics_test_result_request_info import SyntheticsTestResultRequestInfo
    from datadog_api_client.v2.model.synthetics_test_result_response_info import SyntheticsTestResultResponseInfo


class SyntheticsTestResultHandshake(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.synthetics_test_result_request_info import SyntheticsTestResultRequestInfo
        from datadog_api_client.v2.model.synthetics_test_result_response_info import SyntheticsTestResultResponseInfo

        return {
            "request": (SyntheticsTestResultRequestInfo,),
            "response": (SyntheticsTestResultResponseInfo,),
        }

    attribute_map = {
        "request": "request",
        "response": "response",
    }

    def __init__(
        self_,
        request: Union[SyntheticsTestResultRequestInfo, UnsetType] = unset,
        response: Union[SyntheticsTestResultResponseInfo, UnsetType] = unset,
        **kwargs,
    ):
        """
        Handshake request and response for protocol-level tests.

        :param request: Details of the outgoing request made during the test execution.
        :type request: SyntheticsTestResultRequestInfo, optional

        :param response: Details of the response received during the test execution.
        :type response: SyntheticsTestResultResponseInfo, optional
        """
        if request is not unset:
            kwargs["request"] = request
        if response is not unset:
            kwargs["response"] = response
        super().__init__(kwargs)
