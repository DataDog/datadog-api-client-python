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


class AIGuardMeta(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "coding_agent": (str,),
            "confidence_threshold": (float,),
            "env": (str,),
            "is_sds_enabled_override": (bool,),
            "service": (str,),
        }

    attribute_map = {
        "coding_agent": "coding_agent",
        "confidence_threshold": "confidence_threshold",
        "env": "env",
        "is_sds_enabled_override": "is_sds_enabled_override",
        "service": "service",
    }

    def __init__(
        self_,
        coding_agent: Union[str, UnsetType] = unset,
        confidence_threshold: Union[float, UnsetType] = unset,
        env: Union[str, UnsetType] = unset,
        is_sds_enabled_override: Union[bool, UnsetType] = unset,
        service: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Optional metadata providing context about the originating service and request.

        :param coding_agent: Identifier of the coding agent sending the request, if applicable.
        :type coding_agent: str, optional

        :param confidence_threshold: Override for the default threat detection confidence threshold, between 0.0 and 1.0.
        :type confidence_threshold: float, optional

        :param env: The deployment environment of the originating service.
        :type env: str, optional

        :param is_sds_enabled_override: Override whether sensitive data scanning is applied to this request.
        :type is_sds_enabled_override: bool, optional

        :param service: The name of the service sending the evaluation request.
        :type service: str, optional
        """
        if coding_agent is not unset:
            kwargs["coding_agent"] = coding_agent
        if confidence_threshold is not unset:
            kwargs["confidence_threshold"] = confidence_threshold
        if env is not unset:
            kwargs["env"] = env
        if is_sds_enabled_override is not unset:
            kwargs["is_sds_enabled_override"] = is_sds_enabled_override
        if service is not unset:
            kwargs["service"] = service
        super().__init__(kwargs)
