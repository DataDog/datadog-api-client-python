# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class ExperimentsConcludeExperimentV2RequestDataAttributes(ModelNormal):
    validations = {
        "decision_variant_key": {
            "min_length": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "decision_variant_key": (str,),
        }

    attribute_map = {
        "decision_variant_key": "decision_variant_key",
    }

    def __init__(self_, decision_variant_key: str, **kwargs):
        """
        Decision to record when concluding the experiment.

        :param decision_variant_key: Key of the winning variant. Must match a variant on the experiment and must not be blank.
        :type decision_variant_key: str
        """
        super().__init__(kwargs)

        self_.decision_variant_key = decision_variant_key
