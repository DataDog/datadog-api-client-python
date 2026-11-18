# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class CostRecommendationCustomRuleSettings(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return (float,)

    def __init__(self_, **kwargs):
        """
        Setting overrides, keyed by setting name. Settings left out keep the recommender default. The accepted
        settings and their ranges depend on the recommender.
        """
        super().__init__(kwargs)
