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
    from datadog_api_client.v2.model.google_chat_target_audience_create_request_data import (
        GoogleChatTargetAudienceCreateRequestData,
    )


class GoogleChatTargetAudienceCreateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.google_chat_target_audience_create_request_data import (
            GoogleChatTargetAudienceCreateRequestData,
        )

        return {
            "data": (GoogleChatTargetAudienceCreateRequestData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: GoogleChatTargetAudienceCreateRequestData, **kwargs):
        """
        Create target audience request.

        :param data: Data for a create target audience request.
        :type data: GoogleChatTargetAudienceCreateRequestData
        """
        super().__init__(kwargs)

        self_.data = data
