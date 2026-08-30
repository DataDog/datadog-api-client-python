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
    from datadog_api_client.v2.model.slack_reaction_config import SlackReactionConfig


class SlackTrigger(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.slack_reaction_config import SlackReactionConfig

        return {
            "reaction_triggers": ([SlackReactionConfig],),
        }

    attribute_map = {
        "reaction_triggers": "reactionTriggers",
    }

    def __init__(self_, reaction_triggers: Union[List[SlackReactionConfig], UnsetType] = unset, **kwargs):
        """
        Trigger a workflow from Slack. The workflow must be published.

        :param reaction_triggers: Slack emoji reactions that trigger the workflow.
        :type reaction_triggers: [SlackReactionConfig], optional
        """
        if reaction_triggers is not unset:
            kwargs["reaction_triggers"] = reaction_triggers
        super().__init__(kwargs)
