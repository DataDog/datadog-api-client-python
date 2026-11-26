# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SpanKind(ModelSimple):
    """
    Test-only generated schema for the dashboard versioning proof of concept.

    :param value: Must be one of ["consumer", "server", "client", "producer", "internal"].
    :type value: str
    """

    allowed_values = {
        "consumer",
        "server",
        "client",
        "producer",
        "internal",
    }
    CONSUMER: ClassVar["SpanKind"]
    SERVER: ClassVar["SpanKind"]
    CLIENT: ClassVar["SpanKind"]
    PRODUCER: ClassVar["SpanKind"]
    INTERNAL: ClassVar["SpanKind"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SpanKind.CONSUMER = SpanKind("consumer")
SpanKind.SERVER = SpanKind("server")
SpanKind.CLIENT = SpanKind("client")
SpanKind.PRODUCER = SpanKind("producer")
SpanKind.INTERNAL = SpanKind("internal")
