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
)


class GcpScanOptionsDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "compliance_host": (bool,),
            "vuln_containers_os": (bool,),
            "vuln_host_os": (bool,),
        }

    attribute_map = {
        "compliance_host": "compliance_host",
        "vuln_containers_os": "vuln_containers_os",
        "vuln_host_os": "vuln_host_os",
    }

    def __init__(
        self_,
        compliance_host: Union[bool, UnsetType] = unset,
        vuln_containers_os: Union[bool, UnsetType] = unset,
        vuln_host_os: Union[bool, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for GCP scan options configuration.

        :param compliance_host: Indicates whether host compliance scanning is enabled.
        :type compliance_host: bool, optional

        :param vuln_containers_os: Indicates if scanning for vulnerabilities in containers is enabled.
        :type vuln_containers_os: bool, optional

        :param vuln_host_os: Indicates if scanning for vulnerabilities in hosts is enabled.
        :type vuln_host_os: bool, optional
        """
        if compliance_host is not unset:
            kwargs["compliance_host"] = compliance_host
        if vuln_containers_os is not unset:
            kwargs["vuln_containers_os"] = vuln_containers_os
        if vuln_host_os is not unset:
            kwargs["vuln_host_os"] = vuln_host_os
        super().__init__(kwargs)
