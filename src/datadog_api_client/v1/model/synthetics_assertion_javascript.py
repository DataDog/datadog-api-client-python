# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v1.model.synthetics_assertion_javascript_type import SyntheticsAssertionJavascriptType


class SyntheticsAssertionJavascript(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.synthetics_assertion_javascript_type import SyntheticsAssertionJavascriptType

        return {
            "code": (str,),
            "type": (SyntheticsAssertionJavascriptType,),
        }

    attribute_map = {
        "code": "code",
        "type": "type",
    }

    def __init__(self_, code: str, type: SyntheticsAssertionJavascriptType, **kwargs):
        """
        A JavaScript assertion.

        :param code: The JavaScript code that performs the assertions.
        :type code: str

        :param type: Type of the assertion.
        :type type: SyntheticsAssertionJavascriptType
        """
        super().__init__(kwargs)

        self_.code = code
        self_.type = type
