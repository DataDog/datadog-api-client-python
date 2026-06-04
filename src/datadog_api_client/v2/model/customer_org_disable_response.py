# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.customer_org_disable_response_data import CustomerOrgDisableResponseData


class CustomerOrgDisableResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.customer_org_disable_response_data import CustomerOrgDisableResponseData

        return {
            "data": (CustomerOrgDisableResponseData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: CustomerOrgDisableResponseData, **kwargs):
        """
        Response describing the outcome of disabling the customer organization.

        :param data: Data object returned after disabling the customer organization.
        :type data: CustomerOrgDisableResponseData
        """
        super().__init__(kwargs)

        self_.data = data
