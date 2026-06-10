# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class FlagSuggestionAction(ModelSimple):
    """
    The type of change action for a suggestion.

    :param value: Must be one of ["created", "updated", "deleted", "archived", "unarchived", "started", "stopped", "paused", "unpaused"].
    :type value: str
    """

    allowed_values = {
        "created",
        "updated",
        "deleted",
        "archived",
        "unarchived",
        "started",
        "stopped",
        "paused",
        "unpaused",
    }
    CREATED: ClassVar["FlagSuggestionAction"]
    UPDATED: ClassVar["FlagSuggestionAction"]
    DELETED: ClassVar["FlagSuggestionAction"]
    ARCHIVED: ClassVar["FlagSuggestionAction"]
    UNARCHIVED: ClassVar["FlagSuggestionAction"]
    STARTED: ClassVar["FlagSuggestionAction"]
    STOPPED: ClassVar["FlagSuggestionAction"]
    PAUSED: ClassVar["FlagSuggestionAction"]
    UNPAUSED: ClassVar["FlagSuggestionAction"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


FlagSuggestionAction.CREATED = FlagSuggestionAction("created")
FlagSuggestionAction.UPDATED = FlagSuggestionAction("updated")
FlagSuggestionAction.DELETED = FlagSuggestionAction("deleted")
FlagSuggestionAction.ARCHIVED = FlagSuggestionAction("archived")
FlagSuggestionAction.UNARCHIVED = FlagSuggestionAction("unarchived")
FlagSuggestionAction.STARTED = FlagSuggestionAction("started")
FlagSuggestionAction.STOPPED = FlagSuggestionAction("stopped")
FlagSuggestionAction.PAUSED = FlagSuggestionAction("paused")
FlagSuggestionAction.UNPAUSED = FlagSuggestionAction("unpaused")
