# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ExperimentsDatadogEntryPointFilterOperation(ModelSimple):
    """
    Comparison applied by the Datadog entry-point filter.

    :param value: Must be one of ["eq", "in", "neq", "not_in", "gte", "lte", "gt", "lt"].
    :type value: str
    """

    allowed_values = {
        "eq",
        "in",
        "neq",
        "not_in",
        "gte",
        "lte",
        "gt",
        "lt",
    }
    EQ: ClassVar["ExperimentsDatadogEntryPointFilterOperation"]
    IN: ClassVar["ExperimentsDatadogEntryPointFilterOperation"]
    NEQ: ClassVar["ExperimentsDatadogEntryPointFilterOperation"]
    NOT_IN: ClassVar["ExperimentsDatadogEntryPointFilterOperation"]
    GTE: ClassVar["ExperimentsDatadogEntryPointFilterOperation"]
    LTE: ClassVar["ExperimentsDatadogEntryPointFilterOperation"]
    GT: ClassVar["ExperimentsDatadogEntryPointFilterOperation"]
    LT: ClassVar["ExperimentsDatadogEntryPointFilterOperation"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ExperimentsDatadogEntryPointFilterOperation.EQ = ExperimentsDatadogEntryPointFilterOperation("eq")
ExperimentsDatadogEntryPointFilterOperation.IN = ExperimentsDatadogEntryPointFilterOperation("in")
ExperimentsDatadogEntryPointFilterOperation.NEQ = ExperimentsDatadogEntryPointFilterOperation("neq")
ExperimentsDatadogEntryPointFilterOperation.NOT_IN = ExperimentsDatadogEntryPointFilterOperation("not_in")
ExperimentsDatadogEntryPointFilterOperation.GTE = ExperimentsDatadogEntryPointFilterOperation("gte")
ExperimentsDatadogEntryPointFilterOperation.LTE = ExperimentsDatadogEntryPointFilterOperation("lte")
ExperimentsDatadogEntryPointFilterOperation.GT = ExperimentsDatadogEntryPointFilterOperation("gt")
ExperimentsDatadogEntryPointFilterOperation.LT = ExperimentsDatadogEntryPointFilterOperation("lt")
