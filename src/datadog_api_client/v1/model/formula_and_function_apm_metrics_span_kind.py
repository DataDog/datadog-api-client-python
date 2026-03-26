# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class FormulaAndFunctionApmMetricsSpanKind(ModelSimple):
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
    CONSUMER: ClassVar["FormulaAndFunctionApmMetricsSpanKind"]
    SERVER: ClassVar["FormulaAndFunctionApmMetricsSpanKind"]
    CLIENT: ClassVar["FormulaAndFunctionApmMetricsSpanKind"]
    PRODUCER: ClassVar["FormulaAndFunctionApmMetricsSpanKind"]
    INTERNAL: ClassVar["FormulaAndFunctionApmMetricsSpanKind"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


FormulaAndFunctionApmMetricsSpanKind.CONSUMER = FormulaAndFunctionApmMetricsSpanKind("consumer")
FormulaAndFunctionApmMetricsSpanKind.SERVER = FormulaAndFunctionApmMetricsSpanKind("server")
FormulaAndFunctionApmMetricsSpanKind.CLIENT = FormulaAndFunctionApmMetricsSpanKind("client")
FormulaAndFunctionApmMetricsSpanKind.PRODUCER = FormulaAndFunctionApmMetricsSpanKind("producer")
FormulaAndFunctionApmMetricsSpanKind.INTERNAL = FormulaAndFunctionApmMetricsSpanKind("internal")
