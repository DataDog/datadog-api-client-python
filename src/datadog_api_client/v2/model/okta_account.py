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
    from datadog_api_client.v2.model.okta_account_attributes import OktaAccountAttributes
    from datadog_api_client.v2.model.okta_account_type import OktaAccountType


class OktaAccount(ModelNormal):
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

    def __init__(
        self_, attributes: OktaAccountAttributes, type: OktaAccountType, id: Union[str, UnsetType] = unset, **kwargs
    ):
        """
        Schema for an Okta account.

        :param attributes: Attributes object for an Okta account.
        :type attributes: OktaAccountAttributes

        :param id: The ID of the Okta account, a UUID hash of the account name.
        :type id: str, optional

        :param type: Account type for an Okta account.
        :type type: OktaAccountType
        """
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
