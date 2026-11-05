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


class AiGatewayPolicyTargetRequest(ModelNormal):
    validations = {
        "id": {
            "inclusive_minimum": 1,
        },
        "model": {
            "max_length": 256,
            "min_length": 1,
        },
        "provider": {
            "max_length": 256,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "id": (int,),
            "model": (str,),
            "provider": (str,),
        }

    attribute_map = {
        "id": "id",
        "model": "model",
        "provider": "provider",
    }

    def __init__(
        self_,
        id: Union[int, UnsetType] = unset,
        model: Union[str, UnsetType] = unset,
        provider: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Provider and model target in a routing policy request.

        :param id: Saved target row ID. On replacement, retain this ID only within its original route and at most once. A stale or foreign ID is rejected.
        :type id: int, optional

        :param model: Model name or pattern. Omitted when retaining a saved target by ID or when its provider is hidden.
        :type model: str, optional

        :param provider: Provider slug. Omitted for dynamic resolution or when its provider is hidden.
        :type provider: str, optional
        """
        if id is not unset:
            kwargs["id"] = id
        if model is not unset:
            kwargs["model"] = model
        if provider is not unset:
            kwargs["provider"] = provider
        super().__init__(kwargs)
