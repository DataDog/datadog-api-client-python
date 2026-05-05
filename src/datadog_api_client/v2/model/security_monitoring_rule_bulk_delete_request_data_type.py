# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SecurityMonitoringRuleBulkDeleteRequestDataType(ModelSimple):
    """
    The resource type for a bulk delete request.

    :param value: If omitted defaults to "bulk_delete_rules". Must be one of ["bulk_delete_rules"].
    :type value: str
    """

    allowed_values = {
        "bulk_delete_rules",
    }
    BULK_DELETE_RULES: ClassVar["SecurityMonitoringRuleBulkDeleteRequestDataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SecurityMonitoringRuleBulkDeleteRequestDataType.BULK_DELETE_RULES = SecurityMonitoringRuleBulkDeleteRequestDataType(
    "bulk_delete_rules"
)
