# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class FeatureFlagChangeEventAction(ModelSimple):
    """
    The kind of change.

    :param value: Must be one of ["created", "updated", "deleted", "archived", "unarchived", "scheduled", "started", "paused", "unpaused", "stopped"].
    :type value: str
    """

    allowed_values = {
        "created",
        "updated",
        "deleted",
        "archived",
        "unarchived",
        "scheduled",
        "started",
        "paused",
        "unpaused",
        "stopped",
    }
    CREATED: ClassVar["FeatureFlagChangeEventAction"]
    UPDATED: ClassVar["FeatureFlagChangeEventAction"]
    DELETED: ClassVar["FeatureFlagChangeEventAction"]
    ARCHIVED: ClassVar["FeatureFlagChangeEventAction"]
    UNARCHIVED: ClassVar["FeatureFlagChangeEventAction"]
    SCHEDULED: ClassVar["FeatureFlagChangeEventAction"]
    STARTED: ClassVar["FeatureFlagChangeEventAction"]
    PAUSED: ClassVar["FeatureFlagChangeEventAction"]
    UNPAUSED: ClassVar["FeatureFlagChangeEventAction"]
    STOPPED: ClassVar["FeatureFlagChangeEventAction"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


FeatureFlagChangeEventAction.CREATED = FeatureFlagChangeEventAction("created")
FeatureFlagChangeEventAction.UPDATED = FeatureFlagChangeEventAction("updated")
FeatureFlagChangeEventAction.DELETED = FeatureFlagChangeEventAction("deleted")
FeatureFlagChangeEventAction.ARCHIVED = FeatureFlagChangeEventAction("archived")
FeatureFlagChangeEventAction.UNARCHIVED = FeatureFlagChangeEventAction("unarchived")
FeatureFlagChangeEventAction.SCHEDULED = FeatureFlagChangeEventAction("scheduled")
FeatureFlagChangeEventAction.STARTED = FeatureFlagChangeEventAction("started")
FeatureFlagChangeEventAction.PAUSED = FeatureFlagChangeEventAction("paused")
FeatureFlagChangeEventAction.UNPAUSED = FeatureFlagChangeEventAction("unpaused")
FeatureFlagChangeEventAction.STOPPED = FeatureFlagChangeEventAction("stopped")
