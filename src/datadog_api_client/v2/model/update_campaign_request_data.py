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
    from datadog_api_client.v2.model.update_campaign_request_attributes import UpdateCampaignRequestAttributes
    from datadog_api_client.v2.model.campaign_type import CampaignType


class UpdateCampaignRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.update_campaign_request_attributes import UpdateCampaignRequestAttributes
        from datadog_api_client.v2.model.campaign_type import CampaignType

        return {
            "attributes": (UpdateCampaignRequestAttributes,),
            "type": (CampaignType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: UpdateCampaignRequestAttributes, type: CampaignType, **kwargs):
        """
        Data for updating a campaign.

        :param attributes: Attributes for updating a campaign.
        :type attributes: UpdateCampaignRequestAttributes

        :param type: The JSON:API type for campaigns.
        :type type: CampaignType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
