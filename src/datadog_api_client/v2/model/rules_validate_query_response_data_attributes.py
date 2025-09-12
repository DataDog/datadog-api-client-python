# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class RulesValidateQueryResponseDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "canonical": (str,),
        }

    attribute_map = {
        "canonical": "Canonical",
    }

    def __init__(self_, canonical: str, **kwargs):
        """
        The definition of ``RulesValidateQueryResponseDataAttributes`` object.

        :param canonical: The ``attributes`` ``Canonical``.
        :type canonical: str
        """
        super().__init__(kwargs)

        self_.canonical = canonical
