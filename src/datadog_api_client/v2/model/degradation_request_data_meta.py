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


class DegradationRequestDataMeta(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "idempotency_key": (UUID,),
        }

    attribute_map = {
        "idempotency_key": "idempotency_key",
    }

    def __init__(self_, idempotency_key: Union[UUID, UnsetType] = unset, **kwargs):
        """
        The supported metadata for a degradation request.

        :param idempotency_key: A unique key used to ensure idempotent requests.
        :type idempotency_key: UUID, optional
        """
        if idempotency_key is not unset:
            kwargs["idempotency_key"] = idempotency_key
        super().__init__(kwargs)
