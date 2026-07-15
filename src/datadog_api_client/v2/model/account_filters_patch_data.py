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
    from datadog_api_client.v2.model.account_filters_patch_request_attributes import (
        AccountFiltersPatchRequestAttributes,
    )
    from datadog_api_client.v2.model.account_filters_patch_request_type import AccountFiltersPatchRequestType


class AccountFiltersPatchData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.account_filters_patch_request_attributes import (
            AccountFiltersPatchRequestAttributes,
        )
        from datadog_api_client.v2.model.account_filters_patch_request_type import AccountFiltersPatchRequestType

        return {
            "attributes": (AccountFiltersPatchRequestAttributes,),
            "type": (AccountFiltersPatchRequestType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_, attributes: AccountFiltersPatchRequestAttributes, type: AccountFiltersPatchRequestType, **kwargs
    ):
        """
        Account filters patch data.

        :param attributes: Attributes for an account filters patch request.
        :type attributes: AccountFiltersPatchRequestAttributes

        :param type: Type of account filters patch request.
        :type type: AccountFiltersPatchRequestType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
