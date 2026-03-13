# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class RumSegmentUser(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "handle": (str,),
            "icon": (str,),
            "id": (str,),
            "name": (str,),
            "uuid": (str,),
        }

    attribute_map = {
        "handle": "handle",
        "icon": "icon",
        "id": "id",
        "name": "name",
        "uuid": "uuid",
    }

    def __init__(self_, handle: str, icon: str, id: str, name: str, uuid: str, **kwargs):
        """
        A user who performed an action on a segment.

        :param handle: The email handle of the user.
        :type handle: str

        :param icon: The URL of the user icon.
        :type icon: str

        :param id: The numeric identifier of the user.
        :type id: str

        :param name: The display name of the user.
        :type name: str

        :param uuid: The unique identifier of the user.
        :type uuid: str
        """
        super().__init__(kwargs)

        self_.handle = handle
        self_.icon = icon
        self_.id = id
        self_.name = name
        self_.uuid = uuid
