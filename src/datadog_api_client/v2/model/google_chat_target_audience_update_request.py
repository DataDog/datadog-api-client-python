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
    from datadog_api_client.v2.model.google_chat_target_audience_update_request_data import (
        GoogleChatTargetAudienceUpdateRequestData,
    )


class GoogleChatTargetAudienceUpdateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.google_chat_target_audience_update_request_data import (
            GoogleChatTargetAudienceUpdateRequestData,
        )

        return {
            "data": (GoogleChatTargetAudienceUpdateRequestData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: GoogleChatTargetAudienceUpdateRequestData, **kwargs):
        """
        Update target audience request.

        :param data: Data for an update target audience request.
        :type data: GoogleChatTargetAudienceUpdateRequestData
        """
        super().__init__(kwargs)

        self_.data = data
