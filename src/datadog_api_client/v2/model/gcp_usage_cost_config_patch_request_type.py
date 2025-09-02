# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class GCPUsageCostConfigPatchRequestType(ModelSimple):
    """
    Type of GCP Usage Cost config patch request.

    :param value: If omitted defaults to "gcp_uc_config_patch_request". Must be one of ["gcp_uc_config_patch_request"].
    :type value: str
    """

    allowed_values = {
        "gcp_uc_config_patch_request",
    }
    GCP_USAGE_COST_CONFIG_PATCH_REQUEST: ClassVar["GCPUsageCostConfigPatchRequestType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


GCPUsageCostConfigPatchRequestType.GCP_USAGE_COST_CONFIG_PATCH_REQUEST = GCPUsageCostConfigPatchRequestType(
    "gcp_uc_config_patch_request"
)
