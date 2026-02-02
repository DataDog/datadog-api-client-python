# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SamlConfigurationsUpdateRequestDataType(ModelSimple):
    """
    Type of the resource.

    :param value: If omitted defaults to "saml_preferences". Must be one of ["saml_preferences"].
    :type value: str
    """

    allowed_values = {
        "saml_preferences",
    }
    SAML_PREFERENCES: ClassVar["SamlConfigurationsUpdateRequestDataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SamlConfigurationsUpdateRequestDataType.SAML_PREFERENCES = SamlConfigurationsUpdateRequestDataType("saml_preferences")
