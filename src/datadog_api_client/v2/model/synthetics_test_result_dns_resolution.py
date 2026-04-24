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
    from datadog_api_client.v2.model.synthetics_test_result_dns_resolution_attempt import (
        SyntheticsTestResultDnsResolutionAttempt,
    )


class SyntheticsTestResultDnsResolution(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.synthetics_test_result_dns_resolution_attempt import (
            SyntheticsTestResultDnsResolutionAttempt,
        )

        return {
            "attempts": ([SyntheticsTestResultDnsResolutionAttempt],),
            "resolved_ip": (str,),
            "resolved_port": (str,),
            "server": (str,),
        }

    attribute_map = {
        "attempts": "attempts",
        "resolved_ip": "resolved_ip",
        "resolved_port": "resolved_port",
        "server": "server",
    }

    def __init__(
        self_,
        attempts: Union[List[SyntheticsTestResultDnsResolutionAttempt], UnsetType] = unset,
        resolved_ip: Union[str, UnsetType] = unset,
        resolved_port: Union[str, UnsetType] = unset,
        server: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        DNS resolution details recorded during the test execution.

        :param attempts: DNS resolution attempts made during the test.
        :type attempts: [SyntheticsTestResultDnsResolutionAttempt], optional

        :param resolved_ip: Resolved IP address for the target host.
        :type resolved_ip: str, optional

        :param resolved_port: Resolved port for the target service.
        :type resolved_port: str, optional

        :param server: DNS server used for the resolution.
        :type server: str, optional
        """
        if attempts is not unset:
            kwargs["attempts"] = attempts
        if resolved_ip is not unset:
            kwargs["resolved_ip"] = resolved_ip
        if resolved_port is not unset:
            kwargs["resolved_port"] = resolved_port
        if server is not unset:
            kwargs["server"] = server
        super().__init__(kwargs)
