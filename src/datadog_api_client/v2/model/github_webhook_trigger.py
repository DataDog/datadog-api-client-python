# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.trigger_rate_limit import TriggerRateLimit


class GithubWebhookTrigger(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.trigger_rate_limit import TriggerRateLimit

        return {
            "rate_limit": (TriggerRateLimit,),
        }

    attribute_map = {
        "rate_limit": "rateLimit",
    }

    def __init__(self_, rate_limit: Union[TriggerRateLimit, UnsetType] = unset, **kwargs):
        """
        Trigger a workflow from a GitHub webhook. To trigger a workflow from GitHub, you must set a ``webhookSecret``. In your GitHub Webhook Settings, set the Payload URL to "base_url"/api/v2/workflows/"workflow_id"/webhook?orgId="org_id", select application/json for the content type, and be highly recommend enabling SSL verification for security. The workflow must be published.

        :param rate_limit: Defines a rate limit for a trigger.
        :type rate_limit: TriggerRateLimit, optional
        """
        if rate_limit is not unset:
            kwargs["rate_limit"] = rate_limit
        super().__init__(kwargs)
