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


class IncidentGoogleChatConfigurationPatchDataAttributesRequest(ModelNormal):
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
        self_,
        domain_id: Union[str, UnsetType] = unset,
        space_name_template: Union[str, UnsetType] = unset,
        space_target_audience_id: Union[str, UnsetType] = unset,
        space_time_zone: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for patching a Google Chat configuration. All fields are optional.

        :param domain_id: The Google Chat domain ID.
        :type domain_id: str, optional

        :param space_name_template: The template for the Google Chat space name.
        :type space_name_template: str, optional

        :param space_target_audience_id: The target audience ID for the Google Chat space.
        :type space_target_audience_id: str, optional

        :param space_time_zone: The time zone for the Google Chat space.
        :type space_time_zone: str, optional
        """
        if domain_id is not unset:
            kwargs["domain_id"] = domain_id
        if space_name_template is not unset:
            kwargs["space_name_template"] = space_name_template
        if space_target_audience_id is not unset:
            kwargs["space_target_audience_id"] = space_target_audience_id
        if space_time_zone is not unset:
            kwargs["space_time_zone"] = space_time_zone
        super().__init__(kwargs)
