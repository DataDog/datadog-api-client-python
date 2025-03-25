# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.github_webhook_trigger import GithubWebhookTrigger


class GithubWebhookTriggerWrapper(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.github_webhook_trigger import GithubWebhookTrigger

        return {
            "github_webhook_trigger": (GithubWebhookTrigger,),
            "start_step_names": ([str],),
        }

    attribute_map = {
        "github_webhook_trigger": "githubWebhookTrigger",
        "start_step_names": "startStepNames",
    }

    def __init__(
        self_,
        github_webhook_trigger: GithubWebhookTrigger,
        start_step_names: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        Schema for a GitHub webhook-based trigger.

        :param github_webhook_trigger: Trigger a workflow from a GitHub webhook. To trigger a workflow from GitHub, you must set a ``webhookSecret``. In your GitHub Webhook Settings, set the Payload URL to "base_url"/api/v2/workflows/"workflow_id"/webhook?orgId="org_id", select application/json for the content type, and be highly recommend enabling SSL verification for security. The workflow must be published.
        :type github_webhook_trigger: GithubWebhookTrigger

        :param start_step_names: A list of steps that run first after a trigger fires.
        :type start_step_names: [str], optional
        """
        if start_step_names is not unset:
            kwargs["start_step_names"] = start_step_names
        super().__init__(kwargs)

        self_.github_webhook_trigger = github_webhook_trigger
