# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class OIDCCloudAuthPersonaMappingType(ModelSimple):
    """
    Resource type returned by the existing Custom OIDC persona mapping API.

    :param value: If omitted defaults to "custom_oidc_identity_mapping". Must be one of ["custom_oidc_identity_mapping"].
    :type value: str
    """

    allowed_values = {
        "custom_oidc_identity_mapping",
    }
    CUSTOM_OIDC_IDENTITY_MAPPING: ClassVar["OIDCCloudAuthPersonaMappingType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


OIDCCloudAuthPersonaMappingType.CUSTOM_OIDC_IDENTITY_MAPPING = OIDCCloudAuthPersonaMappingType(
    "custom_oidc_identity_mapping"
)
