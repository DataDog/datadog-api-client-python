# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class GenerateCampaignTeamReportsRequestDataType(ModelSimple):
    """


    :param value: If omitted defaults to "campaign-team-report". Must be one of ["campaign-team-report"].
    :type value: str
    """

    allowed_values = {
        "campaign-team-report",
    }
    CAMPAIGN_TEAM_REPORT: ClassVar["GenerateCampaignTeamReportsRequestDataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


GenerateCampaignTeamReportsRequestDataType.CAMPAIGN_TEAM_REPORT = GenerateCampaignTeamReportsRequestDataType(
    "campaign-team-report"
)
