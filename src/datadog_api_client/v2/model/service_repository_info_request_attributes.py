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
    UUID,
)


class ServiceRepositoryInfoRequestAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "debug_id": (UUID,),
            "service": (str,),
            "version": (str,),
        }

    attribute_map = {
        "debug_id": "debug_id",
        "service": "service",
        "version": "version",
    }

    def __init__(
        self_,
        debug_id: Union[UUID, UnsetType] = unset,
        service: Union[str, UnsetType] = unset,
        version: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for the service repository info request.

        :param debug_id: The debug ID of a JavaScript source map, in UUID format. Alternative to ``service`` and ``version``.
        :type debug_id: UUID, optional

        :param service: The name of the service. Required with ``version`` when ``debug_id`` is not set.
        :type service: str, optional

        :param version: The version of the service. Required with ``service`` when ``debug_id`` is not set.
        :type version: str, optional
        """
        if debug_id is not unset:
            kwargs["debug_id"] = debug_id
        if service is not unset:
            kwargs["service"] = service
        if version is not unset:
            kwargs["version"] = version
        super().__init__(kwargs)
