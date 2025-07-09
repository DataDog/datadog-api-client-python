# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class CustomDestinationGoogleSecurityOperationsDestinationAuthType(ModelSimple):
    """
    Type of the Google Security Operations destination authentication.

    :param value: If omitted defaults to "gcp_private_key". Must be one of ["gcp_private_key"].
    :type value: str
    """

    allowed_values = {
        "gcp_private_key",
    }
    GCP_PRIVATE_KEY: ClassVar["CustomDestinationGoogleSecurityOperationsDestinationAuthType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


CustomDestinationGoogleSecurityOperationsDestinationAuthType.GCP_PRIVATE_KEY = (
    CustomDestinationGoogleSecurityOperationsDestinationAuthType("gcp_private_key")
)
