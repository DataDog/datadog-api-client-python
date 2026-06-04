# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class OrgSAMLPreferencesType(ModelSimple):
    """
    SAML preferences resource type.

    :param value: If omitted defaults to "saml_preferences". Must be one of ["saml_preferences"].
    :type value: str
    """

    allowed_values = {
        "saml_preferences",
    }
    SAML_PREFERENCES: ClassVar["OrgSAMLPreferencesType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


OrgSAMLPreferencesType.SAML_PREFERENCES = OrgSAMLPreferencesType("saml_preferences")
