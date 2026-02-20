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


class GoogleChatAppNamedSpaceResponseAttributes(ModelNormal):
    validations = {
        "display_name": {
            "max_length": 255,
        },
        "organization_binding_id": {
            "max_length": 255,
        },
        "resource_name": {
            "max_length": 255,
        },
        "space_uri": {
            "max_length": 255,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "display_name": (str,),
            "organization_binding_id": (str,),
            "resource_name": (str,),
            "space_uri": (str,),
        }

    attribute_map = {
        "display_name": "display_name",
        "organization_binding_id": "organization_binding_id",
        "resource_name": "resource_name",
        "space_uri": "space_uri",
    }

    def __init__(
        self_,
        display_name: Union[str, UnsetType] = unset,
        organization_binding_id: Union[str, UnsetType] = unset,
        resource_name: Union[str, UnsetType] = unset,
        space_uri: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Google Chat space attributes.

        :param display_name: Google space display name.
        :type display_name: str, optional

        :param organization_binding_id: Organization binding ID.
        :type organization_binding_id: str, optional

        :param resource_name: Google space resource name.
        :type resource_name: str, optional

        :param space_uri: Google space URI.
        :type space_uri: str, optional
        """
        if display_name is not unset:
            kwargs["display_name"] = display_name
        if organization_binding_id is not unset:
            kwargs["organization_binding_id"] = organization_binding_id
        if resource_name is not unset:
            kwargs["resource_name"] = resource_name
        if space_uri is not unset:
            kwargs["space_uri"] = space_uri
        super().__init__(kwargs)
