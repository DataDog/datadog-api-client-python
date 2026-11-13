# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    UUID,
)


class ExperimentsBanditVariantV2(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "feature_flag_variant_id": (UUID,),
            "is_active": (bool,),
            "is_fallback": (bool,),
            "key": (str, none_type),
            "name": (str, none_type),
        }

    attribute_map = {
        "feature_flag_variant_id": "feature_flag_variant_id",
        "is_active": "is_active",
        "is_fallback": "is_fallback",
        "key": "key",
        "name": "name",
    }

    def __init__(
        self_,
        feature_flag_variant_id: UUID,
        is_active: bool,
        is_fallback: bool,
        key: Union[str, none_type],
        name: Union[str, none_type],
        **kwargs,
    ):
        """
        A flag variant the bandit uses.

        :param feature_flag_variant_id: The variant's ID on the flag.
        :type feature_flag_variant_id: UUID

        :param is_active: Whether the variant is one of the arms the bandit chooses between.
        :type is_active: bool

        :param is_fallback: Whether the variant is served when the bandit reaches its scheduled end. At most one variant is the fallback.
        :type is_fallback: bool

        :param key: The variant's key. An arm keeps the key it had when it was added, because exposures are matched on it. Null only for a fallback deleted from the flag.
        :type key: str, none_type

        :param name: The variant's name on the flag. Null when it is no longer on the flag.
        :type name: str, none_type
        """
        super().__init__(kwargs)

        self_.feature_flag_variant_id = feature_flag_variant_id
        self_.is_active = is_active
        self_.is_fallback = is_fallback
        self_.key = key
        self_.name = name
