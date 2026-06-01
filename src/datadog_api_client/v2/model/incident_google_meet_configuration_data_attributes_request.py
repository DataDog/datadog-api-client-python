# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class IncidentGoogleMeetConfigurationDataAttributesRequest(ModelNormal):
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

    def __init__(self_, allow_manual_meeting_creation: bool, auto_summarize: bool, **kwargs):
        """
        Attributes for creating a Google Meet configuration.

        :param allow_manual_meeting_creation: Whether to allow manual meeting creation.
        :type allow_manual_meeting_creation: bool

        :param auto_summarize: Whether to auto-summarize meetings.
        :type auto_summarize: bool
        """
        super().__init__(kwargs)

        self_.allow_manual_meeting_creation = allow_manual_meeting_creation
        self_.auto_summarize = auto_summarize
