# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class DORAListDeploymentsRequestDataType(ModelSimple):
    """
    The definition of `DORAListDeploymentsRequestDataType` object.

    :param value: If omitted defaults to "dora_deployments_list_request". Must be one of ["dora_deployments_list_request"].
    :type value: str
    """

    allowed_values = {
        "dora_deployments_list_request",
    }
    DORA_DEPLOYMENTS_LIST_REQUEST: ClassVar["DORAListDeploymentsRequestDataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


DORAListDeploymentsRequestDataType.DORA_DEPLOYMENTS_LIST_REQUEST = DORAListDeploymentsRequestDataType(
    "dora_deployments_list_request"
)
