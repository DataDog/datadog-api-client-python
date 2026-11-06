# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class OIDCCloudAuthDiscoveryType(ModelSimple):
    """
    How the signing keys are discovered.

    :param value: Must be one of ["oidc_discovery", "direct_jwks"].
    :type value: str
    """

    allowed_values = {
        "oidc_discovery",
        "direct_jwks",
    }
    OIDC_DISCOVERY: ClassVar["OIDCCloudAuthDiscoveryType"]
    DIRECT_JWKS: ClassVar["OIDCCloudAuthDiscoveryType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


OIDCCloudAuthDiscoveryType.OIDC_DISCOVERY = OIDCCloudAuthDiscoveryType("oidc_discovery")
OIDCCloudAuthDiscoveryType.DIRECT_JWKS = OIDCCloudAuthDiscoveryType("direct_jwks")
