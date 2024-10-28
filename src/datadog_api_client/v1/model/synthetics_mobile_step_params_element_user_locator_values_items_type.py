# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SyntheticsMobileStepParamsElementUserLocatorValuesItemsType(ModelSimple):
    """
    Type of a user locator.

    :param value: Must be one of ["accessibility-id", "id", "ios-predicate-string", "ios-class-chain", "xpath"].
    :type value: str
    """

    allowed_values = {
        "accessibility-id",
        "id",
        "ios-predicate-string",
        "ios-class-chain",
        "xpath",
    }
    ACCESSIBILITY_ID: ClassVar["SyntheticsMobileStepParamsElementUserLocatorValuesItemsType"]
    ID: ClassVar["SyntheticsMobileStepParamsElementUserLocatorValuesItemsType"]
    IOS_PREDICATE_STRING: ClassVar["SyntheticsMobileStepParamsElementUserLocatorValuesItemsType"]
    IOS_CLASS_CHAIN: ClassVar["SyntheticsMobileStepParamsElementUserLocatorValuesItemsType"]
    XPATH: ClassVar["SyntheticsMobileStepParamsElementUserLocatorValuesItemsType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SyntheticsMobileStepParamsElementUserLocatorValuesItemsType.ACCESSIBILITY_ID = (
    SyntheticsMobileStepParamsElementUserLocatorValuesItemsType("accessibility-id")
)
SyntheticsMobileStepParamsElementUserLocatorValuesItemsType.ID = (
    SyntheticsMobileStepParamsElementUserLocatorValuesItemsType("id")
)
SyntheticsMobileStepParamsElementUserLocatorValuesItemsType.IOS_PREDICATE_STRING = (
    SyntheticsMobileStepParamsElementUserLocatorValuesItemsType("ios-predicate-string")
)
SyntheticsMobileStepParamsElementUserLocatorValuesItemsType.IOS_CLASS_CHAIN = (
    SyntheticsMobileStepParamsElementUserLocatorValuesItemsType("ios-class-chain")
)
SyntheticsMobileStepParamsElementUserLocatorValuesItemsType.XPATH = (
    SyntheticsMobileStepParamsElementUserLocatorValuesItemsType("xpath")
)
