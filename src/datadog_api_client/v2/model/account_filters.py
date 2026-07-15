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
    from datadog_api_client.v2.model.account_filters_attributes import AccountFiltersAttributes
    from datadog_api_client.v2.model.account_filters_type import AccountFiltersType


class AccountFilters(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.account_filters_attributes import AccountFiltersAttributes
        from datadog_api_client.v2.model.account_filters_type import AccountFiltersType

        return {
            "attributes": (AccountFiltersAttributes,),
            "id": (str,),
            "type": (AccountFiltersType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: AccountFiltersAttributes,
        type: AccountFiltersType,
        id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The account filters for a cloud account.

        :param attributes: Attributes for the account filters of a cloud account.
        :type attributes: AccountFiltersAttributes

        :param id: The ID of the cloud account.
        :type id: str, optional

        :param type: Type of account filters.
        :type type: AccountFiltersType
        """
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
