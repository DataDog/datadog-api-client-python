# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class CampaignStatus(ModelSimple):
    """
    The status of the campaign.

    :param value: Must be one of ["in_progress", "not_started", "completed"].
    :type value: str
    """

    allowed_values = {
        "in_progress",
        "not_started",
        "completed",
    }
    IN_PROGRESS: ClassVar["CampaignStatus"]
    NOT_STARTED: ClassVar["CampaignStatus"]
    COMPLETED: ClassVar["CampaignStatus"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


CampaignStatus.IN_PROGRESS = CampaignStatus("in_progress")
CampaignStatus.NOT_STARTED = CampaignStatus("not_started")
CampaignStatus.COMPLETED = CampaignStatus("completed")
