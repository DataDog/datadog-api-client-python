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


class GoogleChatTargetAudienceUpdateRequestAttributes(ModelNormal):
    validations = {
        "audience_id": {
            "max_length": 255,
        },
        "audience_name": {
            "max_length": 255,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "audience_id": (str,),
            "audience_name": (str,),
        }

    attribute_map = {
        "audience_id": "audience_id",
        "audience_name": "audience_name",
    }

    def __init__(
        self_, audience_id: Union[str, UnsetType] = unset, audience_name: Union[str, UnsetType] = unset, **kwargs
    ):
        """
        Attributes for updating a Google Chat target audience.

        :param audience_id: The audience ID.
        :type audience_id: str, optional

        :param audience_name: The audience name.
        :type audience_name: str, optional
        """
        if audience_id is not unset:
            kwargs["audience_id"] = audience_id
        if audience_name is not unset:
            kwargs["audience_name"] = audience_name
        super().__init__(kwargs)
