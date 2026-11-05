# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


class AiGatewayPolicyTarget(ModelNormal):
    validations = {
        "id": {
            "inclusive_minimum": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "id": (int,),
            "model": (str,),
            "priority": (int,),
            "provider": (str, none_type),
        }

    attribute_map = {
        "id": "id",
        "model": "model",
        "priority": "priority",
        "provider": "provider",
    }

    def __init__(
        self_,
        id: int,
        priority: int,
        model: Union[str, UnsetType] = unset,
        provider: Union[str, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        Resolved routing target in a policy response.

        :param id: Saved target row ID. On replacement, retain this ID only within its original route and at most once. A stale or foreign ID is rejected.
        :type id: int

        :param model: Model name or pattern. Omitted when retaining a saved target by ID or when its provider is hidden.
        :type model: str, optional

        :param priority: Routing priority.
        :type priority: int

        :param provider: Provider slug. Omitted for dynamic resolution or when its provider is hidden.
        :type provider: str, none_type, optional
        """
        if model is not unset:
            kwargs["model"] = model
        if provider is not unset:
            kwargs["provider"] = provider
        super().__init__(kwargs)

        self_.id = id
        self_.priority = priority
