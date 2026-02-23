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


class GoogleChatUpdateOrganizationHandleRequestAttributes(ModelNormal):
    validations = {
        "name": {
            "max_length": 255,
        },
        "space_resource_name": {
            "max_length": 255,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "name": (str,),
            "space_resource_name": (str,),
        }

    attribute_map = {
        "name": "name",
        "space_resource_name": "space_resource_name",
    }

    def __init__(
        self_, name: Union[str, UnsetType] = unset, space_resource_name: Union[str, UnsetType] = unset, **kwargs
    ):
        """
        Organization handle attributes for an update request.

        :param name: Organization handle name.
        :type name: str, optional

        :param space_resource_name: Google space resource name.
        :type space_resource_name: str, optional
        """
        if name is not unset:
            kwargs["name"] = name
        if space_resource_name is not unset:
            kwargs["space_resource_name"] = space_resource_name
        super().__init__(kwargs)
