# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.ai_guard_sds_finding_location import AIGuardSdsFindingLocation


class AIGuardSdsFinding(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_guard_sds_finding_location import AIGuardSdsFindingLocation

        return {
            "category": (str,),
            "location": (AIGuardSdsFindingLocation,),
            "rule_display_name": (str,),
            "rule_tag": (str,),
        }

    attribute_map = {
        "category": "category",
        "location": "location",
        "rule_display_name": "rule_display_name",
        "rule_tag": "rule_tag",
    }

    def __init__(
        self_, category: str, location: AIGuardSdsFindingLocation, rule_display_name: str, rule_tag: str, **kwargs
    ):
        """
        A sensitive data finding detected by the SDS scanner.

        :param category: The category of sensitive data detected.
        :type category: str

        :param location: The location of a sensitive data match within the evaluated request.
        :type location: AIGuardSdsFindingLocation

        :param rule_display_name: The human-readable name of the SDS rule that triggered.
        :type rule_display_name: str

        :param rule_tag: The tag identifier of the SDS rule that triggered.
        :type rule_tag: str
        """
        super().__init__(kwargs)

        self_.category = category
        self_.location = location
        self_.rule_display_name = rule_display_name
        self_.rule_tag = rule_tag
