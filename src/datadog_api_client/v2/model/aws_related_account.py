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
    from datadog_api_client.v2.model.aws_related_account_attributes import AWSRelatedAccountAttributes
    from datadog_api_client.v2.model.aws_related_account_type import AWSRelatedAccountType


class AWSRelatedAccount(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.aws_related_account_attributes import AWSRelatedAccountAttributes
        from datadog_api_client.v2.model.aws_related_account_type import AWSRelatedAccountType

        return {
            "attributes": (AWSRelatedAccountAttributes,),
            "id": (str,),
            "type": (AWSRelatedAccountType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        id: str,
        type: AWSRelatedAccountType,
        attributes: Union[AWSRelatedAccountAttributes, UnsetType] = unset,
        **kwargs,
    ):
        """
        AWS related account.

        :param attributes: Attributes for an AWS related account.
        :type attributes: AWSRelatedAccountAttributes, optional

        :param id: The AWS account ID.
        :type id: str

        :param type: Type of AWS related account.
        :type type: AWSRelatedAccountType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
