# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class GetDeviceAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "description": (str,),
            "device_type": (str,),
            "integration": (str,),
            "ip_address": (str,),
            "location": (str,),
            "model": (str,),
            "name": (str,),
            "os_hostname": (str,),
            "os_name": (str,),
            "os_version": (str,),
            "ping_status": (str,),
            "product_name": (str,),
            "serial_number": (str,),
            "status": (str,),
            "subnet": (str,),
            "sys_object_id": (str,),
            "tags": ([str],),
            "vendor": (str,),
            "version": (str,),
        }

    attribute_map = {
        "description": "description",
        "device_type": "device_type",
        "integration": "integration",
        "ip_address": "ip_address",
        "location": "location",
        "model": "model",
        "name": "name",
        "os_hostname": "os_hostname",
        "os_name": "os_name",
        "os_version": "os_version",
        "ping_status": "ping_status",
        "product_name": "product_name",
        "serial_number": "serial_number",
        "status": "status",
        "subnet": "subnet",
        "sys_object_id": "sys_object_id",
        "tags": "tags",
        "vendor": "vendor",
        "version": "version",
    }

    def __init__(
        self_,
        description: Union[str, UnsetType] = unset,
        device_type: Union[str, UnsetType] = unset,
        integration: Union[str, UnsetType] = unset,
        ip_address: Union[str, UnsetType] = unset,
        location: Union[str, UnsetType] = unset,
        model: Union[str, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        os_hostname: Union[str, UnsetType] = unset,
        os_name: Union[str, UnsetType] = unset,
        os_version: Union[str, UnsetType] = unset,
        ping_status: Union[str, UnsetType] = unset,
        product_name: Union[str, UnsetType] = unset,
        serial_number: Union[str, UnsetType] = unset,
        status: Union[str, UnsetType] = unset,
        subnet: Union[str, UnsetType] = unset,
        sys_object_id: Union[str, UnsetType] = unset,
        tags: Union[List[str], UnsetType] = unset,
        vendor: Union[str, UnsetType] = unset,
        version: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The device attributes

        :param description: A description of the device.
        :type description: str, optional

        :param device_type: The type of the device.
        :type device_type: str, optional

        :param integration: The integration of the device.
        :type integration: str, optional

        :param ip_address: The IP address of the device.
        :type ip_address: str, optional

        :param location: The location of the device.
        :type location: str, optional

        :param model: The model of the device.
        :type model: str, optional

        :param name: The name of the device.
        :type name: str, optional

        :param os_hostname: The operating system hostname of the device.
        :type os_hostname: str, optional

        :param os_name: The operating system name of the device.
        :type os_name: str, optional

        :param os_version: The operating system version of the device.
        :type os_version: str, optional

        :param ping_status: The ping status of the device.
        :type ping_status: str, optional

        :param product_name: The product name of the device.
        :type product_name: str, optional

        :param serial_number: The serial number of the device.
        :type serial_number: str, optional

        :param status: The status of the device.
        :type status: str, optional

        :param subnet: The subnet of the device.
        :type subnet: str, optional

        :param sys_object_id: The device ``sys_object_id``.
        :type sys_object_id: str, optional

        :param tags: A list of tags associated with the device.
        :type tags: [str], optional

        :param vendor: The vendor of the device.
        :type vendor: str, optional

        :param version: The version of the device.
        :type version: str, optional
        """
        if description is not unset:
            kwargs["description"] = description
        if device_type is not unset:
            kwargs["device_type"] = device_type
        if integration is not unset:
            kwargs["integration"] = integration
        if ip_address is not unset:
            kwargs["ip_address"] = ip_address
        if location is not unset:
            kwargs["location"] = location
        if model is not unset:
            kwargs["model"] = model
        if name is not unset:
            kwargs["name"] = name
        if os_hostname is not unset:
            kwargs["os_hostname"] = os_hostname
        if os_name is not unset:
            kwargs["os_name"] = os_name
        if os_version is not unset:
            kwargs["os_version"] = os_version
        if ping_status is not unset:
            kwargs["ping_status"] = ping_status
        if product_name is not unset:
            kwargs["product_name"] = product_name
        if serial_number is not unset:
            kwargs["serial_number"] = serial_number
        if status is not unset:
            kwargs["status"] = status
        if subnet is not unset:
            kwargs["subnet"] = subnet
        if sys_object_id is not unset:
            kwargs["sys_object_id"] = sys_object_id
        if tags is not unset:
            kwargs["tags"] = tags
        if vendor is not unset:
            kwargs["vendor"] = vendor
        if version is not unset:
            kwargs["version"] = version
        super().__init__(kwargs)
