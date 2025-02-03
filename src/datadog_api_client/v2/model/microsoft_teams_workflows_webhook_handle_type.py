# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class MicrosoftTeamsWorkflowsWebhookHandleType(ModelSimple):
    """
    Specifies the Workflows webhook handle resource type.

    :param value: If omitted defaults to "workflows-webhook-handle". Must be one of ["workflows-webhook-handle"].
    :type value: str
    """

    allowed_values = {
        "workflows-webhook-handle",
    }
    WORKFLOWS_WEBHOOK_HANDLE: ClassVar["MicrosoftTeamsWorkflowsWebhookHandleType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


MicrosoftTeamsWorkflowsWebhookHandleType.WORKFLOWS_WEBHOOK_HANDLE = MicrosoftTeamsWorkflowsWebhookHandleType(
    "workflows-webhook-handle"
)
