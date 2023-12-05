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
    from datadog_api_client.v2.model.okta_account_update_request_attributes import OktaAccountUpdateRequestAttributes
    from datadog_api_client.v2.model.okta_account_type import OktaAccountType


class OktaAccountUpdateRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.okta_account_update_request_attributes import (
            OktaAccountUpdateRequestAttributes,
        )
        from datadog_api_client.v2.model.okta_account_type import OktaAccountType

        return {
            "attributes": (OktaAccountUpdateRequestAttributes,),
            "type": (OktaAccountType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[OktaAccountUpdateRequestAttributes, UnsetType] = unset,
        type: Union[OktaAccountType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Data object for updating an Okta account.

        :param attributes: Attributes object for updating an Okta account.
        :type attributes: OktaAccountUpdateRequestAttributes, optional

        :param type: Account type for an Okta account.
        :type type: OktaAccountType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
