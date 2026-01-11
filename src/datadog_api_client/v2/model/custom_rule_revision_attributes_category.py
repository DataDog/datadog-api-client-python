# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class CustomRuleRevisionAttributesCategory(ModelSimple):
    """
    Rule category

    :param value: Must be one of ["SECURITY", "BEST_PRACTICES", "CODE_STYLE", "ERROR_PRONE", "PERFORMANCE"].
    :type value: str
    """

    allowed_values = {
        "SECURITY",
        "BEST_PRACTICES",
        "CODE_STYLE",
        "ERROR_PRONE",
        "PERFORMANCE",
    }
    SECURITY: ClassVar["CustomRuleRevisionAttributesCategory"]
    BEST_PRACTICES: ClassVar["CustomRuleRevisionAttributesCategory"]
    CODE_STYLE: ClassVar["CustomRuleRevisionAttributesCategory"]
    ERROR_PRONE: ClassVar["CustomRuleRevisionAttributesCategory"]
    PERFORMANCE: ClassVar["CustomRuleRevisionAttributesCategory"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


CustomRuleRevisionAttributesCategory.SECURITY = CustomRuleRevisionAttributesCategory("SECURITY")
CustomRuleRevisionAttributesCategory.BEST_PRACTICES = CustomRuleRevisionAttributesCategory("BEST_PRACTICES")
CustomRuleRevisionAttributesCategory.CODE_STYLE = CustomRuleRevisionAttributesCategory("CODE_STYLE")
CustomRuleRevisionAttributesCategory.ERROR_PRONE = CustomRuleRevisionAttributesCategory("ERROR_PRONE")
CustomRuleRevisionAttributesCategory.PERFORMANCE = CustomRuleRevisionAttributesCategory("PERFORMANCE")
