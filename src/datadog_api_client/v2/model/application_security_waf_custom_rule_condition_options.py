# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class ApplicationSecurityWafCustomRuleConditionOptions(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "case_sensitive": (bool,),
            "min_length": (int,),
        }

    attribute_map = {
        "case_sensitive": "case_sensitive",
        "min_length": "min_length",
    }

    def __init__(
        self_, case_sensitive: Union[bool, UnsetType] = unset, min_length: Union[int, UnsetType] = unset, **kwargs
    ):
        """
        Options for the operator of this condition.

        :param case_sensitive: Evaluate the value as case sensitive.
        :type case_sensitive: bool, optional

        :param min_length: Only evaluate this condition if the value has a minimum amount of characters.
        :type min_length: int, optional
        """
        if case_sensitive is not unset:
            kwargs["case_sensitive"] = case_sensitive
        if min_length is not unset:
            kwargs["min_length"] = min_length
        super().__init__(kwargs)
