# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)


class SyntheticsCheckType(ModelSimple):
    """
    Type of assertion to apply in an API test.

    :param value: Must be one of ["equals", "notEquals", "contains", "notContains", "startsWith", "notStartsWith", "greater", "lower", "greaterEquals", "lowerEquals", "matchRegex", "between", "isEmpty", "notIsEmpty"].
    :type value: str
    """

    allowed_values = {
        "equals",
        "notEquals",
        "contains",
        "notContains",
        "startsWith",
        "notStartsWith",
        "greater",
        "lower",
        "greaterEquals",
        "lowerEquals",
        "matchRegex",
        "between",
        "isEmpty",
        "notIsEmpty",
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SyntheticsCheckType.EQUALS = SyntheticsCheckType("equals")
SyntheticsCheckType.NOT_EQUALS = SyntheticsCheckType("notEquals")
SyntheticsCheckType.CONTAINS = SyntheticsCheckType("contains")
SyntheticsCheckType.NOT_CONTAINS = SyntheticsCheckType("notContains")
SyntheticsCheckType.STARTS_WITH = SyntheticsCheckType("startsWith")
SyntheticsCheckType.NOT_STARTS_WITH = SyntheticsCheckType("notStartsWith")
SyntheticsCheckType.GREATER = SyntheticsCheckType("greater")
SyntheticsCheckType.LOWER = SyntheticsCheckType("lower")
SyntheticsCheckType.GREATER_EQUALS = SyntheticsCheckType("greaterEquals")
SyntheticsCheckType.LOWER_EQUALS = SyntheticsCheckType("lowerEquals")
SyntheticsCheckType.MATCH_REGEX = SyntheticsCheckType("matchRegex")
SyntheticsCheckType.BETWEEN = SyntheticsCheckType("between")
SyntheticsCheckType.IS_EMPTY = SyntheticsCheckType("isEmpty")
SyntheticsCheckType.NOT_IS_EMPTY = SyntheticsCheckType("notIsEmpty")
