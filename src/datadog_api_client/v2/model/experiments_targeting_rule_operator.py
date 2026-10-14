# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ExperimentsTargetingRuleOperator(ModelSimple):
    """
    Required with attribute and value for an inline condition; omit when saved_filter_id is set.

    :param value: Must be one of ["LT", "LTE", "GT", "GTE", "MATCHES", "NOT_MATCHES", "ONE_OF", "NOT_ONE_OF", "IS_NULL", "EQUALS", "SEMVER_EQ", "SEMVER_NEQ", "SEMVER_LT", "SEMVER_LTE", "SEMVER_GT", "SEMVER_GTE"].
    :type value: str
    """

    allowed_values = {
        "LT",
        "LTE",
        "GT",
        "GTE",
        "MATCHES",
        "NOT_MATCHES",
        "ONE_OF",
        "NOT_ONE_OF",
        "IS_NULL",
        "EQUALS",
        "SEMVER_EQ",
        "SEMVER_NEQ",
        "SEMVER_LT",
        "SEMVER_LTE",
        "SEMVER_GT",
        "SEMVER_GTE",
    }
    LT: ClassVar["ExperimentsTargetingRuleOperator"]
    LTE: ClassVar["ExperimentsTargetingRuleOperator"]
    GT: ClassVar["ExperimentsTargetingRuleOperator"]
    GTE: ClassVar["ExperimentsTargetingRuleOperator"]
    MATCHES: ClassVar["ExperimentsTargetingRuleOperator"]
    NOT_MATCHES: ClassVar["ExperimentsTargetingRuleOperator"]
    ONE_OF: ClassVar["ExperimentsTargetingRuleOperator"]
    NOT_ONE_OF: ClassVar["ExperimentsTargetingRuleOperator"]
    IS_NULL: ClassVar["ExperimentsTargetingRuleOperator"]
    EQUALS: ClassVar["ExperimentsTargetingRuleOperator"]
    SEMVER_EQ: ClassVar["ExperimentsTargetingRuleOperator"]
    SEMVER_NEQ: ClassVar["ExperimentsTargetingRuleOperator"]
    SEMVER_LT: ClassVar["ExperimentsTargetingRuleOperator"]
    SEMVER_LTE: ClassVar["ExperimentsTargetingRuleOperator"]
    SEMVER_GT: ClassVar["ExperimentsTargetingRuleOperator"]
    SEMVER_GTE: ClassVar["ExperimentsTargetingRuleOperator"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ExperimentsTargetingRuleOperator.LT = ExperimentsTargetingRuleOperator("LT")
ExperimentsTargetingRuleOperator.LTE = ExperimentsTargetingRuleOperator("LTE")
ExperimentsTargetingRuleOperator.GT = ExperimentsTargetingRuleOperator("GT")
ExperimentsTargetingRuleOperator.GTE = ExperimentsTargetingRuleOperator("GTE")
ExperimentsTargetingRuleOperator.MATCHES = ExperimentsTargetingRuleOperator("MATCHES")
ExperimentsTargetingRuleOperator.NOT_MATCHES = ExperimentsTargetingRuleOperator("NOT_MATCHES")
ExperimentsTargetingRuleOperator.ONE_OF = ExperimentsTargetingRuleOperator("ONE_OF")
ExperimentsTargetingRuleOperator.NOT_ONE_OF = ExperimentsTargetingRuleOperator("NOT_ONE_OF")
ExperimentsTargetingRuleOperator.IS_NULL = ExperimentsTargetingRuleOperator("IS_NULL")
ExperimentsTargetingRuleOperator.EQUALS = ExperimentsTargetingRuleOperator("EQUALS")
ExperimentsTargetingRuleOperator.SEMVER_EQ = ExperimentsTargetingRuleOperator("SEMVER_EQ")
ExperimentsTargetingRuleOperator.SEMVER_NEQ = ExperimentsTargetingRuleOperator("SEMVER_NEQ")
ExperimentsTargetingRuleOperator.SEMVER_LT = ExperimentsTargetingRuleOperator("SEMVER_LT")
ExperimentsTargetingRuleOperator.SEMVER_LTE = ExperimentsTargetingRuleOperator("SEMVER_LTE")
ExperimentsTargetingRuleOperator.SEMVER_GT = ExperimentsTargetingRuleOperator("SEMVER_GT")
ExperimentsTargetingRuleOperator.SEMVER_GTE = ExperimentsTargetingRuleOperator("SEMVER_GTE")
