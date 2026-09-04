# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class DemUser(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "email": (str,),
            "handle": (str,),
            "name": (str,),
            "uuid": (str,),
        }

    attribute_map = {
        "email": "email",
        "handle": "handle",
        "name": "name",
        "uuid": "uuid",
    }

    def __init__(self_, email: str, handle: str, name: str, uuid: str, **kwargs):
        """
        A Datadog user associated with a DEM operation.

        :param email: The email address of the user.
        :type email: str

        :param handle: The handle of the user.
        :type handle: str

        :param name: The display name of the user.
        :type name: str

        :param uuid: The UUID of the user.
        :type uuid: str
        """
        super().__init__(kwargs)

        self_.email = email
        self_.handle = handle
        self_.name = name
        self_.uuid = uuid
