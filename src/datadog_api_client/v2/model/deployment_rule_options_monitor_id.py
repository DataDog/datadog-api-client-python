# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class DeploymentRuleOptionsMonitorId(ModelNormal):
    validations = {
        "id": {},
    }

    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        return {
            "groups": ([str],),
            "id": (str,),
        }

    attribute_map = {
        "groups": "groups",
        "id": "id",
    }

    def __init__(self_, groups: List[str], id: str, **kwargs):
        """
        A specific monitor and the groups to evaluate for it.

        :param groups: The exact monitor group names to evaluate. An empty array evaluates all groups.
        :type groups: [str]

        :param id: The monitor's decimal ID.
        :type id: str
        """
        super().__init__(kwargs)

        self_.groups = groups
        self_.id = id
