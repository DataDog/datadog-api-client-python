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


class AwsCURConfigPatchRequestAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.account_filtering_config import AccountFilteringConfig

        return {
            "account_filters": (AccountFilteringConfig,),
            "is_enabled": (bool,),
        }

    attribute_map = {
        "account_filters": "account_filters",
        "is_enabled": "is_enabled",
    }

    def __init__(
        self_,
        account_filters: Union[AccountFilteringConfig, UnsetType] = unset,
        is_enabled: Union[bool, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for AWS CUR config Patch Request.

        :param account_filters: The account filtering configuration.
        :type account_filters: AccountFilteringConfig, optional

        :param is_enabled: Whether or not the Cloud Cost Management account is enabled.
        :type is_enabled: bool, optional
        """
        if account_filters is not unset:
            kwargs["account_filters"] = account_filters
        if is_enabled is not unset:
            kwargs["is_enabled"] = is_enabled
        super().__init__(kwargs)
