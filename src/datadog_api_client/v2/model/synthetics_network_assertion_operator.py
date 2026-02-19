# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SyntheticsNetworkAssertionOperator(ModelSimple):
    """
    Assertion operator to apply.

    :param value: Must be one of ["is", "isNot", "lessThan", "lessThanOrEqual", "moreThan", "moreThanOrEqual"].
    :type value: str
    """

    allowed_values = {
        "is",
        "isNot",
        "lessThan",
        "lessThanOrEqual",
        "moreThan",
        "moreThanOrEqual",
    }
    IS: ClassVar["SyntheticsNetworkAssertionOperator"]
    IS_NOT: ClassVar["SyntheticsNetworkAssertionOperator"]
    LESS_THAN: ClassVar["SyntheticsNetworkAssertionOperator"]
    LESS_THAN_OR_EQUAL: ClassVar["SyntheticsNetworkAssertionOperator"]
    MORE_THAN: ClassVar["SyntheticsNetworkAssertionOperator"]
    MORE_THAN_OR_EQUAL: ClassVar["SyntheticsNetworkAssertionOperator"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SyntheticsNetworkAssertionOperator.IS = SyntheticsNetworkAssertionOperator("is")
SyntheticsNetworkAssertionOperator.IS_NOT = SyntheticsNetworkAssertionOperator("isNot")
SyntheticsNetworkAssertionOperator.LESS_THAN = SyntheticsNetworkAssertionOperator("lessThan")
SyntheticsNetworkAssertionOperator.LESS_THAN_OR_EQUAL = SyntheticsNetworkAssertionOperator("lessThanOrEqual")
SyntheticsNetworkAssertionOperator.MORE_THAN = SyntheticsNetworkAssertionOperator("moreThan")
SyntheticsNetworkAssertionOperator.MORE_THAN_OR_EQUAL = SyntheticsNetworkAssertionOperator("moreThanOrEqual")
