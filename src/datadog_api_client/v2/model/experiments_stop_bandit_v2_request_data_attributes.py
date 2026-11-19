# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class ExperimentsStopBanditV2RequestDataAttributes(ModelNormal):
    validations = {
        "served_variant_key": {
            "min_length": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "served_variant_key": (str,),
        }

    attribute_map = {
        "served_variant_key": "served_variant_key",
    }

    def __init__(self_, served_variant_key: str, **kwargs):
        """
        The variant to serve once the bandit stops.

        :param served_variant_key: Key of the flag variant to serve to everyone once the bandit stops. It can be any of the flag's variants, and overrides the configured fallback.
        :type served_variant_key: str
        """
        super().__init__(kwargs)

        self_.served_variant_key = served_variant_key
