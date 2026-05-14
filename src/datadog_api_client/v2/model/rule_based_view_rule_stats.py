# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class RuleBasedViewRuleStats(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "fail": (int,),
            "muted": (int,),
            "_pass": (int,),
        }

    attribute_map = {
        "fail": "fail",
        "muted": "muted",
        "_pass": "pass",
    }

    def __init__(self_, fail: int, muted: int, _pass: int, **kwargs):
        """
        Counts of findings for the rule, grouped by their evaluation status.

        :param fail: Number of findings that failed evaluation.
        :type fail: int

        :param muted: Number of findings that have been muted.
        :type muted: int

        :param _pass: Number of findings that passed evaluation.
        :type _pass: int
        """
        super().__init__(kwargs)

        self_.fail = fail
        self_.muted = muted
        self_._pass = _pass
