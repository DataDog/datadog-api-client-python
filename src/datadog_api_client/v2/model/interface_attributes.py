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
    from datadog_api_client.v2.model.interface_attributes_status import InterfaceAttributesStatus


class InterfaceAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.interface_attributes_status import InterfaceAttributesStatus

        return {
            "alias": (str,),
            "description": (str,),
            "index": (int,),
            "mac_address": (str,),
            "name": (str,),
            "status": (InterfaceAttributesStatus,),
        }

    attribute_map = {
        "alias": "alias",
        "description": "description",
        "index": "index",
        "mac_address": "mac_address",
        "name": "name",
        "status": "status",
    }

    def __init__(
        self_,
        alias: Union[str, UnsetType] = unset,
        description: Union[str, UnsetType] = unset,
        index: Union[int, UnsetType] = unset,
        mac_address: Union[str, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        status: Union[InterfaceAttributesStatus, UnsetType] = unset,
        **kwargs,
    ):
        """
        The interface attributes

        :param alias: The interface alias
        :type alias: str, optional

        :param description: The interface description
        :type description: str, optional

        :param index: The interface index
        :type index: int, optional

        :param mac_address: The interface MAC address
        :type mac_address: str, optional

        :param name: The interface name
        :type name: str, optional

        :param status: The interface status
        :type status: InterfaceAttributesStatus, optional
        """
        if alias is not unset:
            kwargs["alias"] = alias
        if description is not unset:
            kwargs["description"] = description
        if index is not unset:
            kwargs["index"] = index
        if mac_address is not unset:
            kwargs["mac_address"] = mac_address
        if name is not unset:
            kwargs["name"] = name
        if status is not unset:
            kwargs["status"] = status
        super().__init__(kwargs)
