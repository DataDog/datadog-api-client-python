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


class AwsScanOptionsUpdateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "_lambda": (bool,),
            "sensitive_data": (bool,),
            "vuln_containers_os": (bool,),
            "vuln_host_os": (bool,),
        }

    attribute_map = {
        "_lambda": "lambda",
        "sensitive_data": "sensitive_data",
        "vuln_containers_os": "vuln_containers_os",
        "vuln_host_os": "vuln_host_os",
    }

    def __init__(
        self_,
        _lambda: Union[bool, UnsetType] = unset,
        sensitive_data: Union[bool, UnsetType] = unset,
        vuln_containers_os: Union[bool, UnsetType] = unset,
        vuln_host_os: Union[bool, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for the AWS scan options to update.

        :param _lambda: Indicates if scanning of Lambda functions is enabled.
        :type _lambda: bool, optional

        :param sensitive_data: Indicates if scanning for sensitive data is enabled.
        :type sensitive_data: bool, optional

        :param vuln_containers_os: Indicates if scanning for vulnerabilities in containers is enabled.
        :type vuln_containers_os: bool, optional

        :param vuln_host_os: Indicates if scanning for vulnerabilities in hosts is enabled.
        :type vuln_host_os: bool, optional
        """
        if _lambda is not unset:
            kwargs["_lambda"] = _lambda
        if sensitive_data is not unset:
            kwargs["sensitive_data"] = sensitive_data
        if vuln_containers_os is not unset:
            kwargs["vuln_containers_os"] = vuln_containers_os
        if vuln_host_os is not unset:
            kwargs["vuln_host_os"] = vuln_host_os
        super().__init__(kwargs)
