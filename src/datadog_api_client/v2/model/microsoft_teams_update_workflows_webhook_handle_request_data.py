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
    from datadog_api_client.v2.model.microsoft_teams_workflows_webhook_handle_attributes import (
        MicrosoftTeamsWorkflowsWebhookHandleAttributes,
    )
    from datadog_api_client.v2.model.microsoft_teams_workflows_webhook_handle_type import (
        MicrosoftTeamsWorkflowsWebhookHandleType,
    )


class MicrosoftTeamsUpdateWorkflowsWebhookHandleRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.microsoft_teams_workflows_webhook_handle_attributes import (
            MicrosoftTeamsWorkflowsWebhookHandleAttributes,
        )
        from datadog_api_client.v2.model.microsoft_teams_workflows_webhook_handle_type import (
            MicrosoftTeamsWorkflowsWebhookHandleType,
        )

        return {
            "attributes": (MicrosoftTeamsWorkflowsWebhookHandleAttributes,),
            "type": (MicrosoftTeamsWorkflowsWebhookHandleType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: MicrosoftTeamsWorkflowsWebhookHandleAttributes,
        type: MicrosoftTeamsWorkflowsWebhookHandleType,
        **kwargs,
    ):
        """
        Workflows Webhook handle data from a response.

        :param attributes: Workflows Webhook handle attributes.
        :type attributes: MicrosoftTeamsWorkflowsWebhookHandleAttributes

        :param type: Specifies the Workflows webhook handle resource type.
        :type type: MicrosoftTeamsWorkflowsWebhookHandleType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
