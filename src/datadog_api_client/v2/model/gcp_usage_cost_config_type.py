# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class GCPUsageCostConfigType(ModelSimple):
    """
    Type of GCP Usage Cost config.

    :param value: If omitted defaults to "gcp_uc_config". Must be one of ["gcp_uc_config"].
    :type value: str
    """

    allowed_values = {
        "gcp_uc_config",
    }
    GCP_UC_CONFIG: ClassVar["GCPUsageCostConfigType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


GCPUsageCostConfigType.GCP_UC_CONFIG = GCPUsageCostConfigType("gcp_uc_config")
