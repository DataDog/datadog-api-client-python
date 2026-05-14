# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class IncidentMicrosoftTeamsConfigurationDataAttributesRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "manual_meeting_creation": (bool,),
            "post_meeting_summary": (bool,),
        }

    attribute_map = {
        "manual_meeting_creation": "manual_meeting_creation",
        "post_meeting_summary": "post_meeting_summary",
    }

    def __init__(
        self_,
        manual_meeting_creation: Union[bool, UnsetType] = unset,
        post_meeting_summary: Union[bool, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for creating or updating a Microsoft Teams configuration.

        :param manual_meeting_creation: Whether manual meeting creation is enabled.
        :type manual_meeting_creation: bool, optional

        :param post_meeting_summary: Whether post-meeting summary is enabled.
        :type post_meeting_summary: bool, optional
        """
        if manual_meeting_creation is not unset:
            kwargs["manual_meeting_creation"] = manual_meeting_creation
        if post_meeting_summary is not unset:
            kwargs["post_meeting_summary"] = post_meeting_summary
        super().__init__(kwargs)
