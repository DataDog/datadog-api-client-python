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
    from datadog_api_client.v2.model.microsoft_teams_workflows_webhook_handle_response_data import (
        MicrosoftTeamsWorkflowsWebhookHandleResponseData,
    )


class MicrosoftTeamsWorkflowsWebhookHandlesResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.microsoft_teams_workflows_webhook_handle_response_data import (
            MicrosoftTeamsWorkflowsWebhookHandleResponseData,
        )

        return {
            "data": ([MicrosoftTeamsWorkflowsWebhookHandleResponseData],),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: List[MicrosoftTeamsWorkflowsWebhookHandleResponseData], **kwargs):
        """
        Response with a list of Workflows webhook handles.

        :param data: An array of Workflows webhook handles.
        :type data: [MicrosoftTeamsWorkflowsWebhookHandleResponseData]
        """
        super().__init__(kwargs)

        self_.data = data
