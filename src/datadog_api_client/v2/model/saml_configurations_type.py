# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SAMLConfigurationsType(ModelSimple):
    """
    SAML configurations resource type.

    :param value: If omitted defaults to "saml_configurations". Must be one of ["saml_configurations"].
    :type value: str
    """

    allowed_values = {
        "saml_configurations",
    }
    SAML_CONFIGURATIONS: ClassVar["SAMLConfigurationsType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SAMLConfigurationsType.SAML_CONFIGURATIONS = SAMLConfigurationsType("saml_configurations")
