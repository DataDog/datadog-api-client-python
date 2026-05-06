# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class AwsScanOptionsCreateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "compliance_host": (bool,),
            "_lambda": (bool,),
            "sensitive_data": (bool,),
            "vuln_containers_os": (bool,),
            "vuln_host_os": (bool,),
        }

    attribute_map = {
        "compliance_host": "compliance_host",
        "_lambda": "lambda",
        "sensitive_data": "sensitive_data",
        "vuln_containers_os": "vuln_containers_os",
        "vuln_host_os": "vuln_host_os",
    }

    def __init__(
        self_,
        compliance_host: bool,
        _lambda: bool,
        sensitive_data: bool,
        vuln_containers_os: bool,
        vuln_host_os: bool,
        **kwargs,
    ):
        """
        Attributes for the AWS scan options to create.

        :param compliance_host: Indicates whether host compliance scanning is enabled.
        :type compliance_host: bool

        :param _lambda: Indicates if scanning of Lambda functions is enabled.
        :type _lambda: bool

        :param sensitive_data: Indicates if scanning for sensitive data is enabled.
        :type sensitive_data: bool

        :param vuln_containers_os: Indicates if scanning for vulnerabilities in containers is enabled.
        :type vuln_containers_os: bool

        :param vuln_host_os: Indicates if scanning for vulnerabilities in hosts is enabled.
        :type vuln_host_os: bool
        """
        super().__init__(kwargs)

        self_.compliance_host = compliance_host
        self_._lambda = _lambda
        self_.sensitive_data = sensitive_data
        self_.vuln_containers_os = vuln_containers_os
        self_.vuln_host_os = vuln_host_os
