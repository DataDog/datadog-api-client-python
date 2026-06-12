# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.google_chat_target_audience_data import GoogleChatTargetAudienceData


class GoogleChatTargetAudiencesResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.google_chat_target_audience_data import GoogleChatTargetAudienceData

        return {
            "data": ([GoogleChatTargetAudienceData],),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: List[GoogleChatTargetAudienceData], **kwargs):
        """
        Response containing a list of Google Chat target audiences.

        :param data: An array of Google Chat target audiences.
        :type data: [GoogleChatTargetAudienceData]
        """
        super().__init__(kwargs)

        self_.data = data
