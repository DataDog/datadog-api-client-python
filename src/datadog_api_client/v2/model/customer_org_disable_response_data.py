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
    from datadog_api_client.v2.model.customer_org_disable_response_attributes import (
        CustomerOrgDisableResponseAttributes,
    )
    from datadog_api_client.v2.model.customer_org_disable_response_type import CustomerOrgDisableResponseType


class CustomerOrgDisableResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.customer_org_disable_response_attributes import (
            CustomerOrgDisableResponseAttributes,
        )
        from datadog_api_client.v2.model.customer_org_disable_response_type import CustomerOrgDisableResponseType

        return {
            "attributes": (CustomerOrgDisableResponseAttributes,),
            "id": (str,),
            "type": (CustomerOrgDisableResponseType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, attributes: CustomerOrgDisableResponseAttributes, id: str, type: CustomerOrgDisableResponseType, **kwargs
    ):
        """
        Data object returned after disabling the customer organization.

        :param attributes: Attributes describing the outcome of the disable action on the customer organization.
        :type attributes: CustomerOrgDisableResponseAttributes

        :param id: Identifier of the disabled organization.
        :type id: str

        :param type: JSON:API resource type for a customer org disable response.
        :type type: CustomerOrgDisableResponseType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
