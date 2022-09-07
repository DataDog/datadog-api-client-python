# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)


class SyntheticsApiTestFailureCode(ModelSimple):
    """
    Error code that can be returned by a Synthetic test.

    :param value: Must be one of ["BODY_TOO_LARGE", "DENIED", "TOO_MANY_REDIRECTS", "AUTHENTICATION_ERROR", "DECRYPTION", "INVALID_CHAR_IN_HEADER", "HEADER_TOO_LARGE", "HEADERS_INCOMPATIBLE_CONTENT_LENGTH", "INVALID_REQUEST", "REQUIRES_UPDATE", "UNESCAPED_CHARACTERS_IN_REQUEST_PATH", "MALFORMED_RESPONSE", "INCORRECT_ASSERTION", "CONNREFUSED", "CONNRESET", "DNS", "HOSTUNREACH", "NETUNREACH", "TIMEOUT", "SSL", "OCSP", "INVALID_TEST", "TUNNEL", "WEBSOCKET", "UNKNOWN", "INTERNAL_ERROR"].
    :type value: str
    """

    allowed_values = {
        "BODY_TOO_LARGE",
        "DENIED",
        "TOO_MANY_REDIRECTS",
        "AUTHENTICATION_ERROR",
        "DECRYPTION",
        "INVALID_CHAR_IN_HEADER",
        "HEADER_TOO_LARGE",
        "HEADERS_INCOMPATIBLE_CONTENT_LENGTH",
        "INVALID_REQUEST",
        "REQUIRES_UPDATE",
        "UNESCAPED_CHARACTERS_IN_REQUEST_PATH",
        "MALFORMED_RESPONSE",
        "INCORRECT_ASSERTION",
        "CONNREFUSED",
        "CONNRESET",
        "DNS",
        "HOSTUNREACH",
        "NETUNREACH",
        "TIMEOUT",
        "SSL",
        "OCSP",
        "INVALID_TEST",
        "TUNNEL",
        "WEBSOCKET",
        "UNKNOWN",
        "INTERNAL_ERROR",
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SyntheticsApiTestFailureCode.BODY_TOO_LARGE = SyntheticsApiTestFailureCode("BODY_TOO_LARGE")
SyntheticsApiTestFailureCode.DENIED = SyntheticsApiTestFailureCode("DENIED")
SyntheticsApiTestFailureCode.TOO_MANY_REDIRECTS = SyntheticsApiTestFailureCode("TOO_MANY_REDIRECTS")
SyntheticsApiTestFailureCode.AUTHENTICATION_ERROR = SyntheticsApiTestFailureCode("AUTHENTICATION_ERROR")
SyntheticsApiTestFailureCode.DECRYPTION = SyntheticsApiTestFailureCode("DECRYPTION")
SyntheticsApiTestFailureCode.INVALID_CHAR_IN_HEADER = SyntheticsApiTestFailureCode("INVALID_CHAR_IN_HEADER")
SyntheticsApiTestFailureCode.HEADER_TOO_LARGE = SyntheticsApiTestFailureCode("HEADER_TOO_LARGE")
SyntheticsApiTestFailureCode.HEADERS_INCOMPATIBLE_CONTENT_LENGTH = SyntheticsApiTestFailureCode(
    "HEADERS_INCOMPATIBLE_CONTENT_LENGTH"
)
SyntheticsApiTestFailureCode.INVALID_REQUEST = SyntheticsApiTestFailureCode("INVALID_REQUEST")
SyntheticsApiTestFailureCode.REQUIRES_UPDATE = SyntheticsApiTestFailureCode("REQUIRES_UPDATE")
SyntheticsApiTestFailureCode.UNESCAPED_CHARACTERS_IN_REQUEST_PATH = SyntheticsApiTestFailureCode(
    "UNESCAPED_CHARACTERS_IN_REQUEST_PATH"
)
SyntheticsApiTestFailureCode.MALFORMED_RESPONSE = SyntheticsApiTestFailureCode("MALFORMED_RESPONSE")
SyntheticsApiTestFailureCode.INCORRECT_ASSERTION = SyntheticsApiTestFailureCode("INCORRECT_ASSERTION")
SyntheticsApiTestFailureCode.CONNREFUSED = SyntheticsApiTestFailureCode("CONNREFUSED")
SyntheticsApiTestFailureCode.CONNRESET = SyntheticsApiTestFailureCode("CONNRESET")
SyntheticsApiTestFailureCode.DNS = SyntheticsApiTestFailureCode("DNS")
SyntheticsApiTestFailureCode.HOSTUNREACH = SyntheticsApiTestFailureCode("HOSTUNREACH")
SyntheticsApiTestFailureCode.NETUNREACH = SyntheticsApiTestFailureCode("NETUNREACH")
SyntheticsApiTestFailureCode.TIMEOUT = SyntheticsApiTestFailureCode("TIMEOUT")
SyntheticsApiTestFailureCode.SSL = SyntheticsApiTestFailureCode("SSL")
SyntheticsApiTestFailureCode.OCSP = SyntheticsApiTestFailureCode("OCSP")
SyntheticsApiTestFailureCode.INVALID_TEST = SyntheticsApiTestFailureCode("INVALID_TEST")
SyntheticsApiTestFailureCode.TUNNEL = SyntheticsApiTestFailureCode("TUNNEL")
SyntheticsApiTestFailureCode.WEBSOCKET = SyntheticsApiTestFailureCode("WEBSOCKET")
SyntheticsApiTestFailureCode.UNKNOWN = SyntheticsApiTestFailureCode("UNKNOWN")
SyntheticsApiTestFailureCode.INTERNAL_ERROR = SyntheticsApiTestFailureCode("INTERNAL_ERROR")
