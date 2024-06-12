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


class SecurityMonitoringRuleTestResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "results": ([bool],),
        }

    attribute_map = {
        "results": "results",
    }

    def __init__(self_, results: Union[List[bool], UnsetType] = unset, **kwargs):
        """
        Result of the test of the rule queries.

        :param results: Assert results are returned in the same order as the rule query payloads.
            For each payload, it returns True if the result matched the expected result,
            False otherwise.
        :type results: [bool], optional
        """
        if results is not unset:
            kwargs["results"] = results
        super().__init__(kwargs)
