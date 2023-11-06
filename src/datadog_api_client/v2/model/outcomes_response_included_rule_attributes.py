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


class OutcomesResponseIncludedRuleAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "name": (str,),
            "scorecard_name": (str,),
        }

    attribute_map = {
        "name": "name",
        "scorecard_name": "scorecard_name",
    }

    def __init__(self_, name: Union[str, UnsetType] = unset, scorecard_name: Union[str, UnsetType] = unset, **kwargs):
        """
        Details of a rule.

        :param name: Name of the rule.
        :type name: str, optional

        :param scorecard_name: The scorecard name to which this rule must belong.
        :type scorecard_name: str, optional
        """
        if name is not unset:
            kwargs["name"] = name
        if scorecard_name is not unset:
            kwargs["scorecard_name"] = scorecard_name
        super().__init__(kwargs)
