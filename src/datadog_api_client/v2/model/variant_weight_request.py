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


class VariantWeightRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "value": (float,),
            "variant_id": (UUID,),
            "variant_key": (str,),
        }

    attribute_map = {
        "value": "value",
        "variant_id": "variant_id",
        "variant_key": "variant_key",
    }

    def __init__(
        self_,
        value: float,
        variant_id: Union[UUID, UnsetType] = unset,
        variant_key: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Variant weight request payload.

        :param value: The percentage weight for this variant.
        :type value: float

        :param variant_id: The variant ID to assign weight to.
        :type variant_id: UUID, optional

        :param variant_key: The variant key to assign weight to.
        :type variant_key: str, optional
        """
        if variant_id is not unset:
            kwargs["variant_id"] = variant_id
        if variant_key is not unset:
            kwargs["variant_key"] = variant_key
        super().__init__(kwargs)

        self_.value = value
