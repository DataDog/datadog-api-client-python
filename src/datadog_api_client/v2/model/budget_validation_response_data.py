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
    from datadog_api_client.v2.model.budget_validation_response_data_attributes import (
        BudgetValidationResponseDataAttributes,
    )
    from datadog_api_client.v2.model.budget_validation_response_data_type import BudgetValidationResponseDataType


class BudgetValidationResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.budget_validation_response_data_attributes import (
            BudgetValidationResponseDataAttributes,
        )
        from datadog_api_client.v2.model.budget_validation_response_data_type import BudgetValidationResponseDataType

        return {
            "attributes": (BudgetValidationResponseDataAttributes,),
            "id": (str,),
            "type": (BudgetValidationResponseDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        type: BudgetValidationResponseDataType,
        attributes: Union[BudgetValidationResponseDataAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The data object for a budget validation response, containing the resource type, ID, and validation attributes.

        :param attributes: The attributes of a budget validation response, including any validation errors and the validity status.
        :type attributes: BudgetValidationResponseDataAttributes, optional

        :param id: The unique identifier of the budget being validated.
        :type id: str, optional

        :param type: Budget validation resource type.
        :type type: BudgetValidationResponseDataType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.type = type
