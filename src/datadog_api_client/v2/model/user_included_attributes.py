# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    UUID,
)


class UserIncludedAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "email": (str,),
            "handle": (str,),
            "icon": (str,),
            "name": (str,),
            "uuid": (UUID,),
        }

    attribute_map = {
        "email": "email",
        "handle": "handle",
        "icon": "icon",
        "name": "name",
        "uuid": "uuid",
    }

    def __init__(self_, email: str, handle: str, icon: str, name: str, uuid: UUID, **kwargs):
        """
        Attributes of an included user.

        :param email: The email address of the user.
        :type email: str

        :param handle: The handle of the user.
        :type handle: str

        :param icon: The icon URL for the user.
        :type icon: str

        :param name: The name of the user.
        :type name: str

        :param uuid: The UUID of the user.
        :type uuid: UUID
        """
        super().__init__(kwargs)

        self_.email = email
        self_.handle = handle
        self_.icon = icon
        self_.name = name
        self_.uuid = uuid
