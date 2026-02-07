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
    from datadog_api_client.v2.model.generate_campaign_team_reports_request_data import (
        GenerateCampaignTeamReportsRequestData,
    )


class GenerateCampaignTeamReportsRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.generate_campaign_team_reports_request_data import (
            GenerateCampaignTeamReportsRequestData,
        )

        return {
            "data": (GenerateCampaignTeamReportsRequestData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: GenerateCampaignTeamReportsRequestData, **kwargs):
        """
        Request to generate team-specific campaign reports.

        :param data: Data for generating team campaign reports.
        :type data: GenerateCampaignTeamReportsRequestData
        """
        super().__init__(kwargs)

        self_.data = data
