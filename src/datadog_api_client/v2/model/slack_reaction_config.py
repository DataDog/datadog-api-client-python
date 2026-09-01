# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SlackReactionConfig(ModelNormal):
    validations = {
        "reaction_emoji": {
            "min_length": 1,
        },
        "team_id": {
            "min_length": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "reaction_emoji": (str,),
            "team_id": (str,),
        }

    attribute_map = {
        "reaction_emoji": "reactionEmoji",
        "team_id": "teamId",
    }

    def __init__(self_, reaction_emoji: str, team_id: str, **kwargs):
        """
        Configuration for a Slack emoji reaction trigger.

        :param reaction_emoji: The Slack emoji reaction name.
        :type reaction_emoji: str

        :param team_id: The Slack workspace ID.
        :type team_id: str
        """
        super().__init__(kwargs)

        self_.reaction_emoji = reaction_emoji
        self_.team_id = team_id
