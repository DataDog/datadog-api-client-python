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


class FleetTracerAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "env": (str,),
            "hostname": (str,),
            "language": (str,),
            "language_version": (str,),
            "remote_config_status": (str,),
            "runtime_ids": ([str],),
            "service": (str,),
            "service_hostname": (str,),
            "service_version": (str,),
            "tracer_version": (str,),
        }

    attribute_map = {
        "env": "env",
        "hostname": "hostname",
        "language": "language",
        "language_version": "language_version",
        "remote_config_status": "remote_config_status",
        "runtime_ids": "runtime_ids",
        "service": "service",
        "service_hostname": "service_hostname",
        "service_version": "service_version",
        "tracer_version": "tracer_version",
    }

    def __init__(
        self_,
        env: Union[str, UnsetType] = unset,
        hostname: Union[str, UnsetType] = unset,
        language: Union[str, UnsetType] = unset,
        language_version: Union[str, UnsetType] = unset,
        remote_config_status: Union[str, UnsetType] = unset,
        runtime_ids: Union[List[str], UnsetType] = unset,
        service: Union[str, UnsetType] = unset,
        service_hostname: Union[str, UnsetType] = unset,
        service_version: Union[str, UnsetType] = unset,
        tracer_version: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of a fleet tracer representing a service instance reporting telemetry.

        :param env: The environment the tracer is reporting from.
        :type env: str, optional

        :param hostname: The hostname where the tracer is running.
        :type hostname: str, optional

        :param language: The programming language of the traced application.
        :type language: str, optional

        :param language_version: The version of the programming language runtime.
        :type language_version: str, optional

        :param remote_config_status: The remote configuration status of the tracer.
        :type remote_config_status: str, optional

        :param runtime_ids: Runtime identifiers for the tracer instances.
        :type runtime_ids: [str], optional

        :param service: The telemetry-derived service name reported by the tracer.
        :type service: str, optional

        :param service_hostname: The service hostname reported by the tracer.
        :type service_hostname: str, optional

        :param service_version: The version of the traced service.
        :type service_version: str, optional

        :param tracer_version: The version of the Datadog tracer library.
        :type tracer_version: str, optional
        """
        if env is not unset:
            kwargs["env"] = env
        if hostname is not unset:
            kwargs["hostname"] = hostname
        if language is not unset:
            kwargs["language"] = language
        if language_version is not unset:
            kwargs["language_version"] = language_version
        if remote_config_status is not unset:
            kwargs["remote_config_status"] = remote_config_status
        if runtime_ids is not unset:
            kwargs["runtime_ids"] = runtime_ids
        if service is not unset:
            kwargs["service"] = service
        if service_hostname is not unset:
            kwargs["service_hostname"] = service_hostname
        if service_version is not unset:
            kwargs["service_version"] = service_version
        if tracer_version is not unset:
            kwargs["tracer_version"] = tracer_version
        super().__init__(kwargs)
