# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class HostMeta(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.agent_check import AgentCheck
        from datadog_api_client.v1.model.host_meta_install_method import HostMetaInstallMethod

        return {
            "agent_checks": ([AgentCheck],),
            "agent_version": (str,),
            "cpu_cores": (int,),
            "fbsd_v": ([str],),
            "gohai": (str,),
            "install_method": (HostMetaInstallMethod,),
            "mac_v": ([str],),
            "machine": (str,),
            "nix_v": ([str],),
            "platform": (str,),
            "processor": (str,),
            "python_v": (str,),
            "socket_fqdn": (str,),
            "socket_hostname": (str,),
            "win_v": ([str],),
        }

    attribute_map = {
        "agent_checks": "agent_checks",
        "agent_version": "agent_version",
        "cpu_cores": "cpuCores",
        "fbsd_v": "fbsdV",
        "gohai": "gohai",
        "install_method": "install_method",
        "mac_v": "macV",
        "machine": "machine",
        "nix_v": "nixV",
        "platform": "platform",
        "processor": "processor",
        "python_v": "pythonV",
        "socket_fqdn": "socket-fqdn",
        "socket_hostname": "socket-hostname",
        "win_v": "winV",
    }

    def __init__(self, *args, **kwargs):
        """
        Metadata associated with your host.

        :param agent_checks: A list of Agent checks running on the host.
        :type agent_checks: [AgentCheck], optional

        :param agent_version: The Datadog Agent version.
        :type agent_version: str, optional

        :param cpu_cores: The number of cores.
        :type cpu_cores: int, optional

        :param fbsd_v: An array of Mac versions.
        :type fbsd_v: [str], optional

        :param gohai: JSON string containing system information.
        :type gohai: str, optional

        :param install_method: Agent install method.
        :type install_method: HostMetaInstallMethod, optional

        :param mac_v: An array of Mac versions.
        :type mac_v: [str], optional

        :param machine: The machine architecture.
        :type machine: str, optional

        :param nix_v: Array of Unix versions.
        :type nix_v: [str], optional

        :param platform: The OS platform.
        :type platform: str, optional

        :param processor: The processor.
        :type processor: str, optional

        :param python_v: The Python version.
        :type python_v: str, optional

        :param socket_fqdn: The socket fqdn.
        :type socket_fqdn: str, optional

        :param socket_hostname: The socket hostname.
        :type socket_hostname: str, optional

        :param win_v: An array of Windows versions.
        :type win_v: [str], optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(HostMeta, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
