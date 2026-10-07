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
    from datadog_api_client.v2.model.cloud_cost_account_attributes import CloudCostAccountAttributes
    from datadog_api_client.v2.model.cloud_cost_account_type import CloudCostAccountType


class CloudCostAccount(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.cloud_cost_account_attributes import CloudCostAccountAttributes
        from datadog_api_client.v2.model.cloud_cost_account_type import CloudCostAccountType

        return {
            "attributes": (CloudCostAccountAttributes,),
            "id": (str,),
            "type": (CloudCostAccountType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: CloudCostAccountAttributes, id: str, type: CloudCostAccountType, **kwargs):
        """
        A Cloud Cost Management account.

        :param attributes: Read-only status and identifiers for a cloud cost account.
        :type attributes: CloudCostAccountAttributes

        :param id: The Datadog cloud account ID used by the account filters API.
        :type id: str

        :param type: Type of a cloud cost account.
        :type type: CloudCostAccountType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
