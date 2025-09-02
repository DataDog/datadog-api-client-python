# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class GCPUsageCostConfigPostRequestType(ModelSimple):
    """
    Type of GCP Usage Cost config post request.

    :param value: If omitted defaults to "gcp_uc_config_post_request". Must be one of ["gcp_uc_config_post_request"].
    :type value: str
    """

    allowed_values = {
        "gcp_uc_config_post_request",
    }
    GCP_USAGE_COST_CONFIG_POST_REQUEST: ClassVar["GCPUsageCostConfigPostRequestType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


GCPUsageCostConfigPostRequestType.GCP_USAGE_COST_CONFIG_POST_REQUEST = GCPUsageCostConfigPostRequestType(
    "gcp_uc_config_post_request"
)
