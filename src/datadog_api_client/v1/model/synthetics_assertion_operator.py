# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)


class SyntheticsAssertionOperator(ModelSimple):
    """
    Assertion operator to apply.

    :param value: Must be one of ["contains", "doesNotContain", "is", "isNot", "lessThan", "lessThanOrEqual", "moreThan", "moreThanOrEqual", "matches", "doesNotMatch", "validates", "isInMoreThan", "isInLessThan"].
    :type value: str
    """

    allowed_values = {
        "value": {
            "CONTAINS": "contains",
            "DOES_NOT_CONTAIN": "doesNotContain",
            "IS": "is",
            "IS_NOT": "isNot",
            "LESS_THAN": "lessThan",
            "LESS_THAN_OR_EQUAL": "lessThanOrEqual",
            "MORE_THAN": "moreThan",
            "MORE_THAN_OR_EQUAL": "moreThanOrEqual",
            "MATCHES": "matches",
            "DOES_NOT_MATCH": "doesNotMatch",
            "VALIDATES": "validates",
            "IS_IN_MORE_DAYS_THAN": "isInMoreThan",
            "IS_IN_LESS_DAYS_THAN": "isInLessThan",
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }
