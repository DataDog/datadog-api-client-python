# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SecurityMonitoringRuleBulkDeleteResponseDataType(ModelSimple):
    """
    The resource type for a bulk delete response.

    :param value: If omitted defaults to "bulk_delete_response". Must be one of ["bulk_delete_response"].
    :type value: str
    """

    allowed_values = {
        "bulk_delete_response",
    }
    BULK_DELETE_RESPONSE: ClassVar["SecurityMonitoringRuleBulkDeleteResponseDataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SecurityMonitoringRuleBulkDeleteResponseDataType.BULK_DELETE_RESPONSE = (
    SecurityMonitoringRuleBulkDeleteResponseDataType("bulk_delete_response")
)
