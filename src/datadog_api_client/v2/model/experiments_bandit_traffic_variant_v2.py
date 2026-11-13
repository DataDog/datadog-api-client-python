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


class ExperimentsBanditTrafficVariantV2(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "feature_flag_variant_id": (UUID,),
            "observations": (int,),
            "subjects": (int,),
            "variant_key": (str, none_type),
        }

    attribute_map = {
        "feature_flag_variant_id": "feature_flag_variant_id",
        "observations": "observations",
        "subjects": "subjects",
        "variant_key": "variant_key",
    }

    def __init__(
        self_,
        feature_flag_variant_id: UUID,
        observations: int,
        subjects: int,
        variant_key: Union[str, none_type],
        **kwargs,
    ):
        """
        An arm's observations and subjects in total.

        :param feature_flag_variant_id: The arm's variant ID on the flag.
        :type feature_flag_variant_id: UUID

        :param observations: The arm's valid observations, mature or not.
        :type observations: int

        :param subjects: Subjects whose first valid observation is on this arm. A subject counts once, on the arm its reward goes to.
        :type subjects: int

        :param variant_key: The arm's variant key.
        :type variant_key: str, none_type
        """
        super().__init__(kwargs)

        self_.feature_flag_variant_id = feature_flag_variant_id
        self_.observations = observations
        self_.subjects = subjects
        self_.variant_key = variant_key
