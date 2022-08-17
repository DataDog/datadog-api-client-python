# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)


class SyntheticsAssertionType(ModelSimple):
    """
    Type of the assertion.

    :param value: Must be one of ["body", "header", "statusCode", "certificate", "responseTime", "property", "recordEvery", "recordSome", "tlsVersion", "minTlsVersion", "latency", "packetLossPercentage", "packetsReceived", "networkHop", "receivedMessage", "grpcHealthcheckStatus", "connection"].
    :type value: str
    """

    allowed_values = {
        "value": {
            "BODY": "body",
            "HEADER": "header",
            "STATUS_CODE": "statusCode",
            "CERTIFICATE": "certificate",
            "RESPONSE_TIME": "responseTime",
            "PROPERTY": "property",
            "RECORD_EVERY": "recordEvery",
            "RECORD_SOME": "recordSome",
            "TLS_VERSION": "tlsVersion",
            "MIN_TLS_VERSION": "minTlsVersion",
            "LATENCY": "latency",
            "PACKET_LOSS_PERCENTAGE": "packetLossPercentage",
            "PACKETS_RECEIVED": "packetsReceived",
            "NETWORK_HOP": "networkHop",
            "RECEIVED_MESSAGE": "receivedMessage",
            "GRPC_HEALTHCHECK_STATUS": "grpcHealthcheckStatus",
            "CONNECTION": "connection",
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }
