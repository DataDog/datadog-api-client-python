# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.service_now_basic_auth_type import ServiceNowBasicAuthType


class ServiceNowBasicAuthUpdate(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.service_now_basic_auth_type import ServiceNowBasicAuthType

        return {
            "instance": (str,),
            "password": (str,),
            "type": (ServiceNowBasicAuthType,),
            "username": (str,),
        }

    attribute_map = {
        "instance": "instance",
        "password": "password",
        "type": "type",
        "username": "username",
    }

    def __init__(
        self_,
        type: ServiceNowBasicAuthType,
        instance: Union[str, UnsetType] = unset,
        password: Union[str, UnsetType] = unset,
        username: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of the ``ServiceNowBasicAuth`` object.

        :param instance: The ``ServiceNowBasicAuthUpdate`` ``instance``.
        :type instance: str, optional

        :param password: The ``ServiceNowBasicAuthUpdate`` ``password``.
        :type password: str, optional

        :param type: The definition of the ``ServiceNowBasicAuth`` object.
        :type type: ServiceNowBasicAuthType

        :param username: The ``ServiceNowBasicAuthUpdate`` ``username``.
        :type username: str, optional
        """
        if instance is not unset:
            kwargs["instance"] = instance
        if password is not unset:
            kwargs["password"] = password
        if username is not unset:
            kwargs["username"] = username
        super().__init__(kwargs)

        self_.type = type
