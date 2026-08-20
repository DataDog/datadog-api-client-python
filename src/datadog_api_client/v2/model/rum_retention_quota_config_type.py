# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class RumRetentionQuotaConfigType(ModelSimple):
    """
    The type of the resource, always `rum_quota_config`.

    :param value: If omitted defaults to "rum_quota_config". Must be one of ["rum_quota_config"].
    :type value: str
    """

    allowed_values = {
        "rum_quota_config",
    }
    RUM_QUOTA_CONFIG: ClassVar["RumRetentionQuotaConfigType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


RumRetentionQuotaConfigType.RUM_QUOTA_CONFIG = RumRetentionQuotaConfigType("rum_quota_config")
