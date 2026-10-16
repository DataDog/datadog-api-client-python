# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class TagIndexingRuleExemptionVolumeStatus(ModelSimple):
    """
    Indicates whether `estimated_change_in_volume` is available and, if not, why. `ok` indicates a fresh estimate.
        `unindexed_tags` indicates that the matching rule uses tags that are not indexed for the metric.
        `unavailable` indicates that the estimate is stale, was not computed, or could not be retrieved.

    :param value: Must be one of ["ok", "unindexed_tags", "unavailable"].
    :type value: str
    """

    allowed_values = {
        "ok",
        "unindexed_tags",
        "unavailable",
    }
    OK: ClassVar["TagIndexingRuleExemptionVolumeStatus"]
    UNINDEXED_TAGS: ClassVar["TagIndexingRuleExemptionVolumeStatus"]
    UNAVAILABLE: ClassVar["TagIndexingRuleExemptionVolumeStatus"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


TagIndexingRuleExemptionVolumeStatus.OK = TagIndexingRuleExemptionVolumeStatus("ok")
TagIndexingRuleExemptionVolumeStatus.UNINDEXED_TAGS = TagIndexingRuleExemptionVolumeStatus("unindexed_tags")
TagIndexingRuleExemptionVolumeStatus.UNAVAILABLE = TagIndexingRuleExemptionVolumeStatus("unavailable")
