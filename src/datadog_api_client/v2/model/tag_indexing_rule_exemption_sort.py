# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class TagIndexingRuleExemptionSort(ModelSimple):
    """
    Sort field for tag indexing rule exemptions.

    :param value: If omitted defaults to "estimated_change_in_volume". Must be one of ["name", "-name", "estimated_change_in_volume", "-estimated_change_in_volume"].
    :type value: str
    """

    allowed_values = {
        "name",
        "-name",
        "estimated_change_in_volume",
        "-estimated_change_in_volume",
    }
    NAME: ClassVar["TagIndexingRuleExemptionSort"]
    NAME_DESCENDING: ClassVar["TagIndexingRuleExemptionSort"]
    ESTIMATED_CHANGE_IN_VOLUME: ClassVar["TagIndexingRuleExemptionSort"]
    ESTIMATED_CHANGE_IN_VOLUME_DESCENDING: ClassVar["TagIndexingRuleExemptionSort"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


TagIndexingRuleExemptionSort.NAME = TagIndexingRuleExemptionSort("name")
TagIndexingRuleExemptionSort.NAME_DESCENDING = TagIndexingRuleExemptionSort("-name")
TagIndexingRuleExemptionSort.ESTIMATED_CHANGE_IN_VOLUME = TagIndexingRuleExemptionSort("estimated_change_in_volume")
TagIndexingRuleExemptionSort.ESTIMATED_CHANGE_IN_VOLUME_DESCENDING = TagIndexingRuleExemptionSort(
    "-estimated_change_in_volume"
)
