# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class GoogleChatCreateOrganizationHandleRequestAttributes(ModelNormal):
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

    def __init__(self_, name: str, space_resource_name: str, **kwargs):
        """
        Organization handle attributes for a create request.

        :param name: Organization handle name.
        :type name: str

        :param space_resource_name: Google space resource name.
        :type space_resource_name: str
        """
        super().__init__(kwargs)

        self_.name = name
        self_.space_resource_name = space_resource_name
