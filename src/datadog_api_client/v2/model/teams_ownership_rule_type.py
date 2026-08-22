# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class TeamsOwnershipRuleType(ModelSimple):
    """
    The type of the resource. The value should always be teams_ownership_grouped_mappings.

    :param value: If omitted defaults to "teams_ownership_grouped_mappings". Must be one of ["teams_ownership_grouped_mappings"].
    :type value: str
    """

    allowed_values = {
        "teams_ownership_grouped_mappings",
    }
    TEAMS_OWNERSHIP_GROUPED_MAPPINGS: ClassVar["TeamsOwnershipRuleType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


TeamsOwnershipRuleType.TEAMS_OWNERSHIP_GROUPED_MAPPINGS = TeamsOwnershipRuleType("teams_ownership_grouped_mappings")
