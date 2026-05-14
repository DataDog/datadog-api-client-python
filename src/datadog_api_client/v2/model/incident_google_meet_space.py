# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class IncidentGoogleMeetSpace(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "join_url": (str,),
            "meeting_code": (str,),
            "name": (str,),
        }

    attribute_map = {
        "join_url": "join_url",
        "meeting_code": "meeting_code",
        "name": "name",
    }

    def __init__(self_, join_url: str, meeting_code: str, name: str, **kwargs):
        """
        A Google Meet space associated with an incident.

        :param join_url: The URL to join the Google Meet space.
        :type join_url: str

        :param meeting_code: The meeting code for the space.
        :type meeting_code: str

        :param name: The name of the Google Meet space.
        :type name: str
        """
        super().__init__(kwargs)

        self_.join_url = join_url
        self_.meeting_code = meeting_code
        self_.name = name
