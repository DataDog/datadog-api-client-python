# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.variant import Variant


class VariantWeight(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.variant import Variant

        return {
            "created_at": (datetime,),
            "id": (UUID,),
            "updated_at": (datetime,),
            "value": (float,),
            "variant": (Variant,),
            "variant_id": (UUID,),
        }

    attribute_map = {
        "created_at": "created_at",
        "id": "id",
        "updated_at": "updated_at",
        "value": "value",
        "variant": "variant",
        "variant_id": "variant_id",
    }

    def __init__(
        self_,
        value: float,
        variant_id: UUID,
        created_at: Union[datetime, UnsetType] = unset,
        id: Union[UUID, UnsetType] = unset,
        updated_at: Union[datetime, UnsetType] = unset,
        variant: Union[Variant, UnsetType] = unset,
        **kwargs,
    ):
        """
        Variant weight details.

        :param created_at: The timestamp when the variant weight was created.
        :type created_at: datetime, optional

        :param id: Unique identifier of the variant weight assignment.
        :type id: UUID, optional

        :param updated_at: The timestamp when the variant weight was last updated.
        :type updated_at: datetime, optional

        :param value: The percentage weight for the variant.
        :type value: float

        :param variant: A variant of a feature flag.
        :type variant: Variant, optional

        :param variant_id: The variant ID.
        :type variant_id: UUID
        """
        if created_at is not unset:
            kwargs["created_at"] = created_at
        if id is not unset:
            kwargs["id"] = id
        if updated_at is not unset:
            kwargs["updated_at"] = updated_at
        if variant is not unset:
            kwargs["variant"] = variant
        super().__init__(kwargs)

        self_.value = value
        self_.variant_id = variant_id
