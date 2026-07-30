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


class IncidentGoogleMeetConfigurationPatchDataAttributesRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "allow_manual_meeting_creation": (bool,),
            "auto_summarize": (bool,),
        }

    attribute_map = {
        "allow_manual_meeting_creation": "allow_manual_meeting_creation",
        "auto_summarize": "auto_summarize",
    }

    def __init__(
        self_,
        allow_manual_meeting_creation: Union[bool, UnsetType] = unset,
        auto_summarize: Union[bool, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for patching a Google Meet configuration. All fields are optional.

        :param allow_manual_meeting_creation: Whether to allow manual meeting creation.
        :type allow_manual_meeting_creation: bool, optional

        :param auto_summarize: Whether to auto-summarize meetings.
        :type auto_summarize: bool, optional
        """
        if allow_manual_meeting_creation is not unset:
            kwargs["allow_manual_meeting_creation"] = allow_manual_meeting_creation
        if auto_summarize is not unset:
            kwargs["auto_summarize"] = auto_summarize
        super().__init__(kwargs)
