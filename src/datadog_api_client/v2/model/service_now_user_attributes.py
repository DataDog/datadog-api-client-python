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
    UUID,
)


class ServiceNowUserAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "email": (str,),
            "full_name": (str,),
            "instance_id": (UUID,),
            "user_name": (str,),
            "user_sys_id": (str,),
        }

    attribute_map = {
        "email": "email",
        "full_name": "full_name",
        "instance_id": "instance_id",
        "user_name": "user_name",
        "user_sys_id": "user_sys_id",
    }

    def __init__(
        self_,
        email: str,
        instance_id: UUID,
        user_name: str,
        user_sys_id: str,
        full_name: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of a ServiceNow user

        :param email: The email address of the user
        :type email: str

        :param full_name: The full name of the user
        :type full_name: str, optional

        :param instance_id: The ID of the ServiceNow instance
        :type instance_id: UUID

        :param user_name: The username of the ServiceNow user
        :type user_name: str

        :param user_sys_id: The system ID of the user in ServiceNow
        :type user_sys_id: str
        """
        if full_name is not unset:
            kwargs["full_name"] = full_name
        super().__init__(kwargs)

        self_.email = email
        self_.instance_id = instance_id
        self_.user_name = user_name
        self_.user_sys_id = user_sys_id
