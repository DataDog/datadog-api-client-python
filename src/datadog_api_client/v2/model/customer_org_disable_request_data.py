# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.customer_org_disable_request_attributes import CustomerOrgDisableRequestAttributes
    from datadog_api_client.v2.model.customer_org_disable_type import CustomerOrgDisableType


class CustomerOrgDisableRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.customer_org_disable_request_attributes import (
            CustomerOrgDisableRequestAttributes,
        )
        from datadog_api_client.v2.model.customer_org_disable_type import CustomerOrgDisableType

        return {
            "attributes": (CustomerOrgDisableRequestAttributes,),
            "id": (str,),
            "type": (CustomerOrgDisableType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        type: CustomerOrgDisableType,
        attributes: Union[CustomerOrgDisableRequestAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Data object for a customer org disable request.

        :param attributes: Optional attributes for a customer org disable request. When supplied, ``org_uuid``
            must match the authenticated organization or the request is rejected.
        :type attributes: CustomerOrgDisableRequestAttributes, optional

        :param id: Optional client-supplied identifier for the request. Useful for client-side
            correlation; the server does not use this value.
        :type id: str, optional

        :param type: JSON:API resource type for a customer org disable request.
        :type type: CustomerOrgDisableType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.type = type
