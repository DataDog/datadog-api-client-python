# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class RUMOperationJourneyCompositeRuleKind(ModelSimple):
    """
    The rule used to combine the composite rule's predicates. `all_of` requires every predicate
        to match, in any order. `in_order` requires every predicate to match in the given order.

    :param value: Must be one of ["all_of", "in_order"].
    :type value: str
    """

    allowed_values = {
        "all_of",
        "in_order",
    }
    ALL_OF: ClassVar["RUMOperationJourneyCompositeRuleKind"]
    IN_ORDER: ClassVar["RUMOperationJourneyCompositeRuleKind"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


RUMOperationJourneyCompositeRuleKind.ALL_OF = RUMOperationJourneyCompositeRuleKind("all_of")
RUMOperationJourneyCompositeRuleKind.IN_ORDER = RUMOperationJourneyCompositeRuleKind("in_order")
