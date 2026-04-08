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
    from datadog_api_client.v2.model.campaign_response_attributes import CampaignResponseAttributes
    from datadog_api_client.v2.model.campaign_type import CampaignType


class CampaignResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.campaign_response_attributes import CampaignResponseAttributes
        from datadog_api_client.v2.model.campaign_type import CampaignType

        return {
            "attributes": (CampaignResponseAttributes,),
            "id": (str,),
            "type": (CampaignType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: CampaignResponseAttributes, id: str, type: CampaignType, **kwargs):
        """
        Campaign data.

        :param attributes: Campaign attributes.
        :type attributes: CampaignResponseAttributes

        :param id: The unique ID of the campaign.
        :type id: str

        :param type: The JSON:API type for campaigns.
        :type type: CampaignType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
