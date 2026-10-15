# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SavedFilterConditionOperator(ModelSimple):
    """
    The comparison operator used by a saved filter condition.

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
    LT: ClassVar["SavedFilterConditionOperator"]
    LTE: ClassVar["SavedFilterConditionOperator"]
    GT: ClassVar["SavedFilterConditionOperator"]
    GTE: ClassVar["SavedFilterConditionOperator"]
    MATCHES: ClassVar["SavedFilterConditionOperator"]
    NOT_MATCHES: ClassVar["SavedFilterConditionOperator"]
    ONE_OF: ClassVar["SavedFilterConditionOperator"]
    NOT_ONE_OF: ClassVar["SavedFilterConditionOperator"]
    IS_NULL: ClassVar["SavedFilterConditionOperator"]
    EQUALS: ClassVar["SavedFilterConditionOperator"]
    SEMVER_EQ: ClassVar["SavedFilterConditionOperator"]
    SEMVER_NEQ: ClassVar["SavedFilterConditionOperator"]
    SEMVER_LT: ClassVar["SavedFilterConditionOperator"]
    SEMVER_LTE: ClassVar["SavedFilterConditionOperator"]
    SEMVER_GT: ClassVar["SavedFilterConditionOperator"]
    SEMVER_GTE: ClassVar["SavedFilterConditionOperator"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SavedFilterConditionOperator.LT = SavedFilterConditionOperator("LT")
SavedFilterConditionOperator.LTE = SavedFilterConditionOperator("LTE")
SavedFilterConditionOperator.GT = SavedFilterConditionOperator("GT")
SavedFilterConditionOperator.GTE = SavedFilterConditionOperator("GTE")
SavedFilterConditionOperator.MATCHES = SavedFilterConditionOperator("MATCHES")
SavedFilterConditionOperator.NOT_MATCHES = SavedFilterConditionOperator("NOT_MATCHES")
SavedFilterConditionOperator.ONE_OF = SavedFilterConditionOperator("ONE_OF")
SavedFilterConditionOperator.NOT_ONE_OF = SavedFilterConditionOperator("NOT_ONE_OF")
SavedFilterConditionOperator.IS_NULL = SavedFilterConditionOperator("IS_NULL")
SavedFilterConditionOperator.EQUALS = SavedFilterConditionOperator("EQUALS")
SavedFilterConditionOperator.SEMVER_EQ = SavedFilterConditionOperator("SEMVER_EQ")
SavedFilterConditionOperator.SEMVER_NEQ = SavedFilterConditionOperator("SEMVER_NEQ")
SavedFilterConditionOperator.SEMVER_LT = SavedFilterConditionOperator("SEMVER_LT")
SavedFilterConditionOperator.SEMVER_LTE = SavedFilterConditionOperator("SEMVER_LTE")
SavedFilterConditionOperator.SEMVER_GT = SavedFilterConditionOperator("SEMVER_GT")
SavedFilterConditionOperator.SEMVER_GTE = SavedFilterConditionOperator("SEMVER_GTE")
