# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SyntheticsAssertionBodyHashOperator(ModelSimple):
    """
    Assertion operator to apply.

    :param value: Must be one of ["md5", "sha1", "sha256"].
    :type value: str
    """

    allowed_values = {
        "md5",
        "sha1",
        "sha256",
    }
    MD5: ClassVar["SyntheticsAssertionBodyHashOperator"]
    SHA1: ClassVar["SyntheticsAssertionBodyHashOperator"]
    SHA256: ClassVar["SyntheticsAssertionBodyHashOperator"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SyntheticsAssertionBodyHashOperator.MD5 = SyntheticsAssertionBodyHashOperator("md5")
SyntheticsAssertionBodyHashOperator.SHA1 = SyntheticsAssertionBodyHashOperator("sha1")
SyntheticsAssertionBodyHashOperator.SHA256 = SyntheticsAssertionBodyHashOperator("sha256")
