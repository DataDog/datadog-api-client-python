# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class IncidentGoogleChatConfigurationDataAttributesRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "domain_id": (str,),
            "space_name_template": (str,),
            "space_target_audience_id": (str,),
            "space_time_zone": (str,),
        }

    attribute_map = {
        "domain_id": "domain_id",
        "space_name_template": "space_name_template",
        "space_target_audience_id": "space_target_audience_id",
        "space_time_zone": "space_time_zone",
    }

    def __init__(
        self_, domain_id: str, space_name_template: str, space_target_audience_id: str, space_time_zone: str, **kwargs
    ):
        """
        Attributes for creating a Google Chat configuration.

        :param domain_id: The Google Chat domain ID.
        :type domain_id: str

        :param space_name_template: The template for the Google Chat space name.
        :type space_name_template: str

        :param space_target_audience_id: The target audience ID for the Google Chat space.
        :type space_target_audience_id: str

        :param space_time_zone: The time zone for the Google Chat space.
        :type space_time_zone: str
        """
        super().__init__(kwargs)

        self_.domain_id = domain_id
        self_.space_name_template = space_name_template
        self_.space_target_audience_id = space_target_audience_id
        self_.space_time_zone = space_time_zone
