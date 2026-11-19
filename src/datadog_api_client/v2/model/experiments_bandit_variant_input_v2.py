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


class ExperimentsBanditVariantInputV2(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "feature_flag_variant_id": (UUID,),
            "is_active": (bool,),
            "is_fallback": (bool,),
        }

    attribute_map = {
        "feature_flag_variant_id": "feature_flag_variant_id",
        "is_active": "is_active",
        "is_fallback": "is_fallback",
    }

    def __init__(
        self_,
        feature_flag_variant_id: UUID,
        is_active: Union[bool, UnsetType] = unset,
        is_fallback: Union[bool, UnsetType] = unset,
        **kwargs,
    ):
        """
        A flag variant the bandit uses, named by its ID. The variant's ``key`` and ``name`` come from the flag and can't be set.

        :param feature_flag_variant_id: The variant's ID on the flag.
        :type feature_flag_variant_id: UUID

        :param is_active: Whether the variant is one of the arms the bandit chooses between. Defaults to ``true``.
        :type is_active: bool, optional

        :param is_fallback: Whether the variant is served when the bandit reaches its scheduled end. At most one variant is the fallback, and it doesn't have to be an arm. Defaults to ``false``.
        :type is_fallback: bool, optional
        """
        if is_active is not unset:
            kwargs["is_active"] = is_active
        if is_fallback is not unset:
            kwargs["is_fallback"] = is_fallback
        super().__init__(kwargs)

        self_.feature_flag_variant_id = feature_flag_variant_id
