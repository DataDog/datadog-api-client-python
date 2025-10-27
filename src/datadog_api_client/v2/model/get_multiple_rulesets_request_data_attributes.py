# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class GetMultipleRulesetsRequestDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "include_testing_rules": (bool,),
            "include_tests": (bool,),
            "rulesets": ([str],),
        }

    attribute_map = {
        "include_testing_rules": "include_testing_rules",
        "include_tests": "include_tests",
        "rulesets": "rulesets",
    }

    def __init__(
        self_,
        include_testing_rules: Union[bool, UnsetType] = unset,
        include_tests: Union[bool, UnsetType] = unset,
        rulesets: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """


        :param include_testing_rules:
        :type include_testing_rules: bool, optional

        :param include_tests:
        :type include_tests: bool, optional

        :param rulesets:
        :type rulesets: [str], optional
        """
        if include_testing_rules is not unset:
            kwargs["include_testing_rules"] = include_testing_rules
        if include_tests is not unset:
            kwargs["include_tests"] = include_tests
        if rulesets is not unset:
            kwargs["rulesets"] = rulesets
        super().__init__(kwargs)
