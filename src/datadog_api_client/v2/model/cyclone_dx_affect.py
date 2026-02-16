# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class CycloneDXAffect(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "ref": (str,),
        }

    attribute_map = {
        "ref": "ref",
    }

    def __init__(self_, ref: str, **kwargs):
        """
        Reference to a component affected by a vulnerability.

        :param ref: Reference to a component's bom-ref.
        :type ref: str
        """
        super().__init__(kwargs)

        self_.ref = ref
