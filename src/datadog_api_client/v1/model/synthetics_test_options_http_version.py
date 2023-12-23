# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    StringEnum,
)

from typing import ClassVar


class SyntheticsTestOptionsHTTPVersion(StringEnum):
    """
    HTTP version to use for a Synthetic test.

    :param value: Must be one of ["http1", "http2", "any"].
    :type value: str
    """

    allowed_values = {
        "http1",
        "http2",
        "any",
    }
    HTTP1: ClassVar["SyntheticsTestOptionsHTTPVersion"]
    HTTP2: ClassVar["SyntheticsTestOptionsHTTPVersion"]
    ANY: ClassVar["SyntheticsTestOptionsHTTPVersion"]


SyntheticsTestOptionsHTTPVersion.HTTP1 = SyntheticsTestOptionsHTTPVersion("http1")
SyntheticsTestOptionsHTTPVersion.HTTP2 = SyntheticsTestOptionsHTTPVersion("http2")
SyntheticsTestOptionsHTTPVersion.ANY = SyntheticsTestOptionsHTTPVersion("any")
