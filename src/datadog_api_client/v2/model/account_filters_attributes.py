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
    from datadog_api_client.v2.model.account_filtering_config import AccountFilteringConfig


class AccountFiltersAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.account_filtering_config import AccountFilteringConfig

        return {
            "account_filters": (AccountFilteringConfig,),
            "account_id": (str,),
            "cloud": (str,),
        }

    attribute_map = {
        "account_filters": "account_filters",
        "account_id": "account_id",
        "cloud": "cloud",
    }

    def __init__(
        self_,
        account_filters: Union[AccountFilteringConfig, UnsetType] = unset,
        account_id: Union[str, UnsetType] = unset,
        cloud: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for the account filters of a cloud account.

        :param account_filters: The account filtering configuration.
        :type account_filters: AccountFilteringConfig, optional

        :param account_id: The cloud account ID.
        :type account_id: str, optional

        :param cloud: The cloud provider of the account, for example ``aws`` , ``aws_cur2`` , or ``oci``.
        :type cloud: str, optional
        """
        if account_filters is not unset:
            kwargs["account_filters"] = account_filters
        if account_id is not unset:
            kwargs["account_id"] = account_id
        if cloud is not unset:
            kwargs["cloud"] = cloud
        super().__init__(kwargs)
