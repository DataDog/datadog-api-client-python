# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


class IncidentGoogleMeetConfigurationDataAttributesResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "allow_manual_meeting_creation": (bool,),
            "auto_summarize": (bool,),
            "created_at": (datetime,),
            "modified_at": (datetime,),
        }

    attribute_map = {
        "allow_manual_meeting_creation": "allow_manual_meeting_creation",
        "auto_summarize": "auto_summarize",
        "created_at": "created_at",
        "modified_at": "modified_at",
    }

    def __init__(
        self_,
        allow_manual_meeting_creation: bool,
        auto_summarize: bool,
        modified_at: datetime,
        created_at: Union[datetime, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of a Google Meet configuration.

        :param allow_manual_meeting_creation: Whether manual meeting creation is allowed.
        :type allow_manual_meeting_creation: bool

        :param auto_summarize: Whether meetings are auto-summarized.
        :type auto_summarize: bool

        :param created_at: Timestamp when the configuration was created.
        :type created_at: datetime, optional

        :param modified_at: Timestamp when the configuration was last modified.
        :type modified_at: datetime
        """
        if created_at is not unset:
            kwargs["created_at"] = created_at
        super().__init__(kwargs)

        self_.allow_manual_meeting_creation = allow_manual_meeting_creation
        self_.auto_summarize = auto_summarize
        self_.modified_at = modified_at
