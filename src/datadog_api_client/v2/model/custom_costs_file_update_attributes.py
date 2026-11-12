# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class CustomCostsFileUpdateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "ai_provider": (bool,),
        }

    attribute_map = {
        "ai_provider": "ai_provider",
    }

    def __init__(self_, ai_provider: bool, **kwargs):
        """
        Attributes of a Custom Costs file that can be updated.

        :param ai_provider: Whether the Custom Costs file contains the costs of an AI provider.
        :type ai_provider: bool
        """
        super().__init__(kwargs)

        self_.ai_provider = ai_provider
