# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SBOMComponentProperty(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "name": (str,),
            "value": (str,),
        }

    attribute_map = {
        "name": "name",
        "value": "value",
    }

    def __init__(self_, name: str, value: str, **kwargs):
        """
        The custom property of the component of the SBOM.

        :param name: The name of the custom property of the component of the SBOM.
        :type name: str

        :param value: The value of the custom property of the component of the SBOM.
        :type value: str
        """
        super().__init__(kwargs)

        self_.name = name
        self_.value = value
