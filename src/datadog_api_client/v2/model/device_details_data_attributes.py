# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.device_employee import DeviceEmployee
    from datadog_api_client.v2.model.device_geo_ip import DeviceGeoIP
    from datadog_api_client.v2.model.device_status import DeviceStatus


class DeviceDetailsDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.device_employee import DeviceEmployee
        from datadog_api_client.v2.model.device_geo_ip import DeviceGeoIP
        from datadog_api_client.v2.model.device_status import DeviceStatus

        return {
            "agent_key": (str,),
            "agent_version": (str,),
            "battery_charge_pct": (int,),
            "battery_charge_rate": (int,),
            "battery_critical": (bool,),
            "battery_cycle_count": (int,),
            "battery_max_capacity_pct": (int,),
            "cnm_enabled": (bool,),
            "cpu_cores": (int,),
            "cpu_logical_processors": (int,),
            "cpu_model": (str,),
            "cpu_usage": (float,),
            "disk_usage": (float,),
            "employee": (DeviceEmployee,),
            "geo_ip": (DeviceGeoIP,),
            "ip_address": (str,),
            "issues": ([str],),
            "kernel_name": (str,),
            "last_reboot": (str,),
            "last_seen": (str,),
            "manufacturer": (str,),
            "mem_usage": (float,),
            "memory_total_kb": (int,),
            "model_name": (str,),
            "model_number": (str,),
            "os": (str,),
            "os_version": (str,),
            "packet_sent": (float,),
            "resource_id": (str,),
            "retransmit": (float,),
            "retransmit_pct": (float,),
            "serial_number": (str,),
            "status": (DeviceStatus,),
            "tcp_canceled": (float,),
            "tcp_established": (float,),
            "tcp_establishment_failure_pct": (float,),
            "tcp_establishment_failures": (float,),
            "tcp_host_unreachable": (float,),
            "tcp_network_unreachable": (float,),
            "tcp_refusals": (float,),
            "tcp_timeouts": (float,),
            "type": (str,),
            "uptime": (float,),
            "wlan_bssid": (str,),
            "wlan_rssi": (float,),
            "wlan_ssid": (str,),
        }

    attribute_map = {
        "agent_key": "agent_key",
        "agent_version": "agent_version",
        "battery_charge_pct": "battery_charge_pct",
        "battery_charge_rate": "battery_charge_rate",
        "battery_critical": "battery_critical",
        "battery_cycle_count": "battery_cycle_count",
        "battery_max_capacity_pct": "battery_max_capacity_pct",
        "cnm_enabled": "cnm_enabled",
        "cpu_cores": "cpu_cores",
        "cpu_logical_processors": "cpu_logical_processors",
        "cpu_model": "cpu_model",
        "cpu_usage": "cpu_usage",
        "disk_usage": "disk_usage",
        "employee": "employee",
        "geo_ip": "geo_ip",
        "ip_address": "ip_address",
        "issues": "issues",
        "kernel_name": "kernel_name",
        "last_reboot": "last_reboot",
        "last_seen": "last_seen",
        "manufacturer": "manufacturer",
        "mem_usage": "mem_usage",
        "memory_total_kb": "memory_total_kb",
        "model_name": "model_name",
        "model_number": "model_number",
        "os": "os",
        "os_version": "os_version",
        "packet_sent": "packet_sent",
        "resource_id": "resource_id",
        "retransmit": "retransmit",
        "retransmit_pct": "retransmit_pct",
        "serial_number": "serial_number",
        "status": "status",
        "tcp_canceled": "tcp_canceled",
        "tcp_established": "tcp_established",
        "tcp_establishment_failure_pct": "tcp_establishment_failure_pct",
        "tcp_establishment_failures": "tcp_establishment_failures",
        "tcp_host_unreachable": "tcp_host_unreachable",
        "tcp_network_unreachable": "tcp_network_unreachable",
        "tcp_refusals": "tcp_refusals",
        "tcp_timeouts": "tcp_timeouts",
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
        battery_charge_pct: Union[int, UnsetType] = unset,
        battery_charge_rate: Union[int, UnsetType] = unset,
        battery_critical: Union[bool, UnsetType] = unset,
        battery_cycle_count: Union[int, UnsetType] = unset,
        battery_max_capacity_pct: Union[int, UnsetType] = unset,
        cnm_enabled: Union[bool, UnsetType] = unset,
        cpu_cores: Union[int, UnsetType] = unset,
        cpu_logical_processors: Union[int, UnsetType] = unset,
        cpu_model: Union[str, UnsetType] = unset,
        cpu_usage: Union[float, UnsetType] = unset,
        disk_usage: Union[float, UnsetType] = unset,
        employee: Union[DeviceEmployee, UnsetType] = unset,
        geo_ip: Union[DeviceGeoIP, UnsetType] = unset,
        ip_address: Union[str, UnsetType] = unset,
        issues: Union[List[str], UnsetType] = unset,
        kernel_name: Union[str, UnsetType] = unset,
        last_reboot: Union[str, UnsetType] = unset,
        last_seen: Union[str, UnsetType] = unset,
        manufacturer: Union[str, UnsetType] = unset,
        mem_usage: Union[float, UnsetType] = unset,
        memory_total_kb: Union[int, UnsetType] = unset,
        model_name: Union[str, UnsetType] = unset,
        model_number: Union[str, UnsetType] = unset,
        os: Union[str, UnsetType] = unset,
        os_version: Union[str, UnsetType] = unset,
        packet_sent: Union[float, UnsetType] = unset,
        resource_id: Union[str, UnsetType] = unset,
        retransmit: Union[float, UnsetType] = unset,
        retransmit_pct: Union[float, UnsetType] = unset,
        serial_number: Union[str, UnsetType] = unset,
        status: Union[DeviceStatus, UnsetType] = unset,
        tcp_canceled: Union[float, UnsetType] = unset,
        tcp_established: Union[float, UnsetType] = unset,
        tcp_establishment_failure_pct: Union[float, UnsetType] = unset,
        tcp_establishment_failures: Union[float, UnsetType] = unset,
        tcp_host_unreachable: Union[float, UnsetType] = unset,
        tcp_network_unreachable: Union[float, UnsetType] = unset,
        tcp_refusals: Union[float, UnsetType] = unset,
        tcp_timeouts: Union[float, UnsetType] = unset,
        type: Union[str, UnsetType] = unset,
        uptime: Union[float, UnsetType] = unset,
        wlan_bssid: Union[str, UnsetType] = unset,
        wlan_rssi: Union[float, UnsetType] = unset,
        wlan_ssid: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Extended set of attributes for a single End User Device Monitoring device,
        including Cloud Network Monitoring and battery metrics.

        :param agent_key: Public key of the Datadog Agent installed on the device.
        :type agent_key: str, optional

        :param agent_version: Version of the Datadog Agent installed on the device.
        :type agent_version: str, optional

        :param battery_charge_pct: Current battery charge level as a percentage between 0 and 100.
        :type battery_charge_pct: int, optional

        :param battery_charge_rate: Rate at which the battery is charging or discharging, in milliamperes.
            Negative values indicate discharge.
        :type battery_charge_rate: int, optional

        :param battery_critical: Whether the device's battery health has degraded to a critical level.
        :type battery_critical: bool, optional

        :param battery_cycle_count: Number of full charge cycles the battery has gone through.
        :type battery_cycle_count: int, optional

        :param battery_max_capacity_pct: Maximum battery capacity expressed as a percentage of the device's design capacity.
        :type battery_max_capacity_pct: int, optional

        :param cnm_enabled: Whether Cloud Network Monitoring is enabled on the device.
        :type cnm_enabled: bool, optional

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

        :param employee: Directory information about the employee associated with the device,
            sourced from a customer reference table.
            Absent when no reference table is configured or the device has no match.
        :type employee: DeviceEmployee, optional

        :param geo_ip: Location derived from the device's public IP address.
            Absent when no location data is available.
        :type geo_ip: DeviceGeoIP, optional

        :param ip_address: Last observed IPv4 or IPv6 address of the device.
        :type ip_address: str, optional

        :param issues: List of issue identifiers currently affecting the device.
        :type issues: [str], optional

        :param kernel_name: Name of the operating system kernel running on the device.
        :type kernel_name: str, optional

        :param last_reboot: Timestamp of the most recent device reboot, in RFC 3339 format.
        :type last_reboot: str, optional

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

        :param os: Operating system family running on the device, as reported by the Datadog Agent
            (for example, ``macOS`` , ``Windows`` , or ``linux`` ). Empty when unknown.
        :type os: str, optional

        :param os_version: Operating system version running on the device.
        :type os_version: str, optional

        :param packet_sent: Number of TCP packets sent by the device over the query window,
            as reported by Cloud Network Monitoring.
        :type packet_sent: float, optional

        :param resource_id: Datadog resource identifier for the device.
        :type resource_id: str, optional

        :param retransmit: Number of TCP packets retransmitted by the device over the query window.
        :type retransmit: float, optional

        :param retransmit_pct: Percentage of sent TCP packets that were retransmitted, between 0 and 100.
        :type retransmit_pct: float, optional

        :param serial_number: Serial number assigned to the device by its manufacturer.
        :type serial_number: str, optional

        :param status: Health status of the device, computed from its issues and recent telemetry.
            ``inactive`` means the device stopped reporting. ``unknown`` means no telemetry is available yet.
        :type status: DeviceStatus, optional

        :param tcp_canceled: Number of TCP connection attempts canceled by the device over the query window.
        :type tcp_canceled: float, optional

        :param tcp_established: Number of TCP connections established by the device over the query window.
        :type tcp_established: float, optional

        :param tcp_establishment_failure_pct: Percentage of TCP connection attempts that failed, between 0 and 100.
        :type tcp_establishment_failure_pct: float, optional

        :param tcp_establishment_failures: Number of TCP connection attempts that failed over the query window.
        :type tcp_establishment_failures: float, optional

        :param tcp_host_unreachable: Number of TCP connection attempts that failed because the host was unreachable.
        :type tcp_host_unreachable: float, optional

        :param tcp_network_unreachable: Number of TCP connection attempts that failed because the network was unreachable.
        :type tcp_network_unreachable: float, optional

        :param tcp_refusals: Number of TCP connection attempts refused by the remote host over the query window.
        :type tcp_refusals: float, optional

        :param tcp_timeouts: Number of TCP connection attempts that timed out over the query window.
        :type tcp_timeouts: float, optional

        :param type: Hardware type of the device (for example, ``laptop`` or ``desktop`` ). ``unknown`` when the type cannot be determined.
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
        if battery_charge_pct is not unset:
            kwargs["battery_charge_pct"] = battery_charge_pct
        if battery_charge_rate is not unset:
            kwargs["battery_charge_rate"] = battery_charge_rate
        if battery_critical is not unset:
            kwargs["battery_critical"] = battery_critical
        if battery_cycle_count is not unset:
            kwargs["battery_cycle_count"] = battery_cycle_count
        if battery_max_capacity_pct is not unset:
            kwargs["battery_max_capacity_pct"] = battery_max_capacity_pct
        if cnm_enabled is not unset:
            kwargs["cnm_enabled"] = cnm_enabled
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
        if employee is not unset:
            kwargs["employee"] = employee
        if geo_ip is not unset:
            kwargs["geo_ip"] = geo_ip
        if ip_address is not unset:
            kwargs["ip_address"] = ip_address
        if issues is not unset:
            kwargs["issues"] = issues
        if kernel_name is not unset:
            kwargs["kernel_name"] = kernel_name
        if last_reboot is not unset:
            kwargs["last_reboot"] = last_reboot
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
        if packet_sent is not unset:
            kwargs["packet_sent"] = packet_sent
        if resource_id is not unset:
            kwargs["resource_id"] = resource_id
        if retransmit is not unset:
            kwargs["retransmit"] = retransmit
        if retransmit_pct is not unset:
            kwargs["retransmit_pct"] = retransmit_pct
        if serial_number is not unset:
            kwargs["serial_number"] = serial_number
        if status is not unset:
            kwargs["status"] = status
        if tcp_canceled is not unset:
            kwargs["tcp_canceled"] = tcp_canceled
        if tcp_established is not unset:
            kwargs["tcp_established"] = tcp_established
        if tcp_establishment_failure_pct is not unset:
            kwargs["tcp_establishment_failure_pct"] = tcp_establishment_failure_pct
        if tcp_establishment_failures is not unset:
            kwargs["tcp_establishment_failures"] = tcp_establishment_failures
        if tcp_host_unreachable is not unset:
            kwargs["tcp_host_unreachable"] = tcp_host_unreachable
        if tcp_network_unreachable is not unset:
            kwargs["tcp_network_unreachable"] = tcp_network_unreachable
        if tcp_refusals is not unset:
            kwargs["tcp_refusals"] = tcp_refusals
        if tcp_timeouts is not unset:
            kwargs["tcp_timeouts"] = tcp_timeouts
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
