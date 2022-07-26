# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)


class SyntheticsTestDetailsSubType(ModelSimple):
    """
    The subtype of the Synthetic API test, `http`, `ssl`, `tcp`,
        `dns`, `icmp`, `udp`, `websocket`, `grpc` or `multi`.

    :param value: Must be one of ["http", "ssl", "tcp", "dns", "multi", "icmp", "udp", "websocket", "grpc"].
    :type value: str
    """

    allowed_values = {
        "value": {
            "HTTP": "http",
            "SSL": "ssl",
            "TCP": "tcp",
            "DNS": "dns",
            "MULTI": "multi",
            "ICMP": "icmp",
            "UDP": "udp",
            "WEBSOCKET": "websocket",
            "GRPC": "grpc",
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }
