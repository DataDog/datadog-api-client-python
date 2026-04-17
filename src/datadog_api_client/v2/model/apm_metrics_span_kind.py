# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ApmMetricsSpanKind(ModelSimple):
    """
    Describes the relationship between the span, its parents, and its children in a trace.

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
    CONSUMER: ClassVar["ApmMetricsSpanKind"]
    SERVER: ClassVar["ApmMetricsSpanKind"]
    CLIENT: ClassVar["ApmMetricsSpanKind"]
    PRODUCER: ClassVar["ApmMetricsSpanKind"]
    INTERNAL: ClassVar["ApmMetricsSpanKind"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ApmMetricsSpanKind.CONSUMER = ApmMetricsSpanKind("consumer")
ApmMetricsSpanKind.SERVER = ApmMetricsSpanKind("server")
ApmMetricsSpanKind.CLIENT = ApmMetricsSpanKind("client")
ApmMetricsSpanKind.PRODUCER = ApmMetricsSpanKind("producer")
ApmMetricsSpanKind.INTERNAL = ApmMetricsSpanKind("internal")
