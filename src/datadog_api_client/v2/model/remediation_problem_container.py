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


class RemediationProblemContainer(ModelNormal):
    validations = {
        "exit_code": {
            "inclusive_maximum": 255,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "cpu_limit": (int,),
            "exit_code": (int,),
            "health_status": (str,),
            "image": (str,),
            "last_status": (str,),
            "memory_limit_mib": (int,),
            "name": (str,),
            "reason": (str,),
        }

    attribute_map = {
        "cpu_limit": "cpu_limit",
        "exit_code": "exit_code",
        "health_status": "health_status",
        "image": "image",
        "last_status": "last_status",
        "memory_limit_mib": "memory_limit_mib",
        "name": "name",
        "reason": "reason",
    }

    def __init__(
        self_,
        cpu_limit: Union[int, UnsetType] = unset,
        exit_code: Union[int, UnsetType] = unset,
        health_status: Union[str, UnsetType] = unset,
        image: Union[str, UnsetType] = unset,
        last_status: Union[str, UnsetType] = unset,
        memory_limit_mib: Union[int, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        reason: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        A container within a problematic task that is exhibiting issues.

        :param cpu_limit: CPU limit.
        :type cpu_limit: int, optional

        :param exit_code: Exit code if the container stopped.
        :type exit_code: int, optional

        :param health_status: Container health status.
        :type health_status: str, optional

        :param image: Docker image URI.
        :type image: str, optional

        :param last_status: Container status.
        :type last_status: str, optional

        :param memory_limit_mib: Memory limit in MiB.
        :type memory_limit_mib: int, optional

        :param name: Container name from the task definition.
        :type name: str, optional

        :param reason: Stop reason.
        :type reason: str, optional
        """
        if cpu_limit is not unset:
            kwargs["cpu_limit"] = cpu_limit
        if exit_code is not unset:
            kwargs["exit_code"] = exit_code
        if health_status is not unset:
            kwargs["health_status"] = health_status
        if image is not unset:
            kwargs["image"] = image
        if last_status is not unset:
            kwargs["last_status"] = last_status
        if memory_limit_mib is not unset:
            kwargs["memory_limit_mib"] = memory_limit_mib
        if name is not unset:
            kwargs["name"] = name
        if reason is not unset:
            kwargs["reason"] = reason
        super().__init__(kwargs)
