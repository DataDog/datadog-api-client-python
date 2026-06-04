# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class OAuth2WellKnownSitesEnvType(ModelSimple):
    """
    JSON:API resource type for OAuth2 well-known sites environment.

    :param value: If omitted defaults to "env". Must be one of ["env"].
    :type value: str
    """

    allowed_values = {
        "env",
    }
    ENV: ClassVar["OAuth2WellKnownSitesEnvType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


OAuth2WellKnownSitesEnvType.ENV = OAuth2WellKnownSitesEnvType("env")
