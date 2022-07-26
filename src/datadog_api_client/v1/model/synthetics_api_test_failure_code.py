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
        "value": {
            "BODY_TOO_LARGE": "BODY_TOO_LARGE",
            "DENIED": "DENIED",
            "TOO_MANY_REDIRECTS": "TOO_MANY_REDIRECTS",
            "AUTHENTICATION_ERROR": "AUTHENTICATION_ERROR",
            "DECRYPTION": "DECRYPTION",
            "INVALID_CHAR_IN_HEADER": "INVALID_CHAR_IN_HEADER",
            "HEADER_TOO_LARGE": "HEADER_TOO_LARGE",
            "HEADERS_INCOMPATIBLE_CONTENT_LENGTH": "HEADERS_INCOMPATIBLE_CONTENT_LENGTH",
            "INVALID_REQUEST": "INVALID_REQUEST",
            "REQUIRES_UPDATE": "REQUIRES_UPDATE",
            "UNESCAPED_CHARACTERS_IN_REQUEST_PATH": "UNESCAPED_CHARACTERS_IN_REQUEST_PATH",
            "MALFORMED_RESPONSE": "MALFORMED_RESPONSE",
            "INCORRECT_ASSERTION": "INCORRECT_ASSERTION",
            "CONNREFUSED": "CONNREFUSED",
            "CONNRESET": "CONNRESET",
            "DNS": "DNS",
            "HOSTUNREACH": "HOSTUNREACH",
            "NETUNREACH": "NETUNREACH",
            "TIMEOUT": "TIMEOUT",
            "SSL": "SSL",
            "OCSP": "OCSP",
            "INVALID_TEST": "INVALID_TEST",
            "TUNNEL": "TUNNEL",
            "WEBSOCKET": "WEBSOCKET",
            "UNKNOWN": "UNKNOWN",
            "INTERNAL_ERROR": "INTERNAL_ERROR",
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }
