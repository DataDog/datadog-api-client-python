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
    from datadog_api_client.v2.model.okta_account_attributes import OktaAccountAttributes
    from datadog_api_client.v2.model.okta_account_type import OktaAccountType


class OktaAccountResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.okta_account_attributes import OktaAccountAttributes
        from datadog_api_client.v2.model.okta_account_type import OktaAccountType

        return {
            "attributes": (OktaAccountAttributes,),
            "id": (str,),
            "type": (OktaAccountType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: OktaAccountAttributes, id: str, type: OktaAccountType, **kwargs):
        """
        Data object of an Okta account

        :param attributes: Attributes object for an Okta account.
        :type attributes: OktaAccountAttributes

        :param id: The ID of the Okta account, a UUID hash of the account name.
        :type id: str

        :param type: Account type for an Okta account.
        :type type: OktaAccountType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
