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


class ExperimentsBanditPolicyVariantV2(ModelNormal):
    validations = {
        "probability": {
            "inclusive_maximum": 1,
            "inclusive_minimum": 0,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "feature_flag_variant_id": (UUID,),
            "probability": (float,),
            "variant_key": (str, none_type),
        }

    attribute_map = {
        "feature_flag_variant_id": "feature_flag_variant_id",
        "probability": "probability",
        "variant_key": "variant_key",
    }

    def __init__(
        self_, feature_flag_variant_id: UUID, probability: float, variant_key: Union[str, none_type], **kwargs
    ):
        """
        A variant's share of traffic under a policy.

        :param feature_flag_variant_id: The variant's ID on the flag.
        :type feature_flag_variant_id: UUID

        :param probability: The share of traffic the variant gets, from 0 to 1.
        :type probability: float

        :param variant_key: The variant's key. Null when it can't be resolved.
        :type variant_key: str, none_type
        """
        super().__init__(kwargs)

        self_.feature_flag_variant_id = feature_flag_variant_id
        self_.probability = probability
        self_.variant_key = variant_key
