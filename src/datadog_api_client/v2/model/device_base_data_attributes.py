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


class DeviceBaseDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "agent_key": (str,),
            "agent_version": (str,),
            "battery_max_capacity_pct": (int,),
            "cpu_cores": (int,),
            "cpu_logical_processors": (int,),
            "cpu_model": (str,),
            "cpu_usage": (float,),
            "disk_usage": (float,),
            "ip_address": (str,),
            "issues": ([str],),
            "kernel_name": (str,),
            "last_seen": (str,),
            "manufacturer": (str,),
            "mem_usage": (float,),
            "memory_total_kb": (int,),
            "model_name": (str,),
            "model_number": (str,),
            "os": (str,),
            "os_version": (str,),
            "resource_id": (str,),
            "serial_number": (str,),
            "status": (str,),
            "type": (str,),
            "uptime": (float,),
            "wlan_bssid": (str,),
            "wlan_rssi": (float,),
            "wlan_ssid": (str,),
        }

    attribute_map = {
        "agent_key": "agent_key",
        "agent_version": "agent_version",
        "battery_max_capacity_pct": "battery_max_capacity_pct",
        "cpu_cores": "cpu_cores",
        "cpu_logical_processors": "cpu_logical_processors",
        "cpu_model": "cpu_model",
        "cpu_usage": "cpu_usage",
        "disk_usage": "disk_usage",
        "ip_address": "ip_address",
        "issues": "issues",
        "kernel_name": "kernel_name",
        "last_seen": "last_seen",
        "manufacturer": "manufacturer",
        "mem_usage": "mem_usage",
        "memory_total_kb": "memory_total_kb",
        "model_name": "model_name",
        "model_number": "model_number",
        "os": "os",
        "os_version": "os_version",
        "resource_id": "resource_id",
        "serial_number": "serial_number",
        "status": "status",
        "type": "type",
        "uptime": "uptime",
        "wlan_bssid": "wlan_bssid",
        "wlan_rssi": "wlan_rssi",
        "wlan_ssid": "wlan_ssid",
    }

    def __init__(
        self_,
        agent_key: Union[str, UnsetType] = unset,
        agent_version: Union[str, UnsetType] = unset,
        battery_max_capacity_pct: Union[int, UnsetType] = unset,
        cpu_cores: Union[int, UnsetType] = unset,
        cpu_logical_processors: Union[int, UnsetType] = unset,
        cpu_model: Union[str, UnsetType] = unset,
        cpu_usage: Union[float, UnsetType] = unset,
        disk_usage: Union[float, UnsetType] = unset,
        ip_address: Union[str, UnsetType] = unset,
        issues: Union[List[str], UnsetType] = unset,
        kernel_name: Union[str, UnsetType] = unset,
        last_seen: Union[str, UnsetType] = unset,
        manufacturer: Union[str, UnsetType] = unset,
        mem_usage: Union[float, UnsetType] = unset,
        memory_total_kb: Union[int, UnsetType] = unset,
        model_name: Union[str, UnsetType] = unset,
        model_number: Union[str, UnsetType] = unset,
        os: Union[str, UnsetType] = unset,
        os_version: Union[str, UnsetType] = unset,
        resource_id: Union[str, UnsetType] = unset,
        serial_number: Union[str, UnsetType] = unset,
        status: Union[str, UnsetType] = unset,
        type: Union[str, UnsetType] = unset,
        uptime: Union[float, UnsetType] = unset,
        wlan_bssid: Union[str, UnsetType] = unset,
        wlan_rssi: Union[float, UnsetType] = unset,
        wlan_ssid: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Common health and identity attributes shared by every End User Device Monitoring device record.

        :param agent_key: Public key of the Datadog Agent installed on the device.
        :type agent_key: str, optional

        :param agent_version: Version of the Datadog Agent installed on the device.
        :type agent_version: str, optional

        :param battery_max_capacity_pct: Maximum battery capacity expressed as a percentage of the device's design capacity.
        :type battery_max_capacity_pct: int, optional

        :param cpu_cores: Number of physical CPU cores on the device.
        :type cpu_cores: int, optional

        :param cpu_logical_processors: Number of logical CPU processors (hardware threads) on the device.
        :type cpu_logical_processors: int, optional

        :param cpu_model: Human-readable name of the device's CPU model.
        :type cpu_model: str, optional

        :param cpu_usage: Average CPU usage on the device, as a percentage between 0 and 100.
        :type cpu_usage: float, optional

        :param disk_usage: Average disk usage on the device, as a percentage between 0 and 100.
        :type disk_usage: float, optional

        :param ip_address: Last observed IPv4 or IPv6 address of the device.
        :type ip_address: str, optional

        :param issues: List of issue identifiers currently affecting the device.
            References entries returned by the issues endpoint.
        :type issues: [str], optional

        :param kernel_name: Name of the operating system kernel running on the device.
        :type kernel_name: str, optional

        :param last_seen: Timestamp of the most recent telemetry received from the device, in RFC 3339 format.
        :type last_seen: str, optional

        :param manufacturer: Manufacturer of the device.
        :type manufacturer: str, optional

        :param mem_usage: Average memory usage on the device, as a percentage between 0 and 100.
        :type mem_usage: float, optional

        :param memory_total_kb: Total amount of physical memory available on the device, in kilobytes.
        :type memory_total_kb: int, optional

        :param model_name: Marketing or product name of the device model.
        :type model_name: str, optional

        :param model_number: Manufacturer-assigned model number of the device.
        :type model_number: str, optional

        :param os: Operating system family running on the device (for example, ``mac`` , ``windows`` , or ``linux`` ).
        :type os: str, optional

        :param os_version: Operating system version running on the device.
        :type os_version: str, optional

        :param resource_id: Datadog resource identifier for the device.
        :type resource_id: str, optional

        :param serial_number: Serial number assigned to the device by its manufacturer.
        :type serial_number: str, optional

        :param status: Health status of the device computed from its issues and recent telemetry.
        :type status: str, optional

        :param type: Hardware type of the device (for example, ``laptop`` , ``desktop`` , or ``mobile`` ).
        :type type: str, optional

        :param uptime: Time elapsed since the device last booted, in seconds.
        :type uptime: float, optional

        :param wlan_bssid: BSSID (MAC address of the access point) of the wireless network the device is
            currently connected to.
        :type wlan_bssid: str, optional

        :param wlan_rssi: Received signal strength indicator of the device's current wireless connection, in dBm.
        :type wlan_rssi: float, optional

        :param wlan_ssid: SSID of the wireless network the device is currently connected to.
        :type wlan_ssid: str, optional
        """
        if agent_key is not unset:
            kwargs["agent_key"] = agent_key
        if agent_version is not unset:
            kwargs["agent_version"] = agent_version
        if battery_max_capacity_pct is not unset:
            kwargs["battery_max_capacity_pct"] = battery_max_capacity_pct
        if cpu_cores is not unset:
            kwargs["cpu_cores"] = cpu_cores
        if cpu_logical_processors is not unset:
            kwargs["cpu_logical_processors"] = cpu_logical_processors
        if cpu_model is not unset:
            kwargs["cpu_model"] = cpu_model
        if cpu_usage is not unset:
            kwargs["cpu_usage"] = cpu_usage
        if disk_usage is not unset:
            kwargs["disk_usage"] = disk_usage
        if ip_address is not unset:
            kwargs["ip_address"] = ip_address
        if issues is not unset:
            kwargs["issues"] = issues
        if kernel_name is not unset:
            kwargs["kernel_name"] = kernel_name
        if last_seen is not unset:
            kwargs["last_seen"] = last_seen
        if manufacturer is not unset:
            kwargs["manufacturer"] = manufacturer
        if mem_usage is not unset:
            kwargs["mem_usage"] = mem_usage
        if memory_total_kb is not unset:
            kwargs["memory_total_kb"] = memory_total_kb
        if model_name is not unset:
            kwargs["model_name"] = model_name
        if model_number is not unset:
            kwargs["model_number"] = model_number
        if os is not unset:
            kwargs["os"] = os
        if os_version is not unset:
            kwargs["os_version"] = os_version
        if resource_id is not unset:
            kwargs["resource_id"] = resource_id
        if serial_number is not unset:
            kwargs["serial_number"] = serial_number
        if status is not unset:
            kwargs["status"] = status
        if type is not unset:
            kwargs["type"] = type
        if uptime is not unset:
            kwargs["uptime"] = uptime
        if wlan_bssid is not unset:
            kwargs["wlan_bssid"] = wlan_bssid
        if wlan_rssi is not unset:
            kwargs["wlan_rssi"] = wlan_rssi
        if wlan_ssid is not unset:
            kwargs["wlan_ssid"] = wlan_ssid
        super().__init__(kwargs)
