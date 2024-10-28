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
    from datadog_api_client.v1.model.synthetics_mobile_step_params_element_user_locator_values_items_type import (
        SyntheticsMobileStepParamsElementUserLocatorValuesItemsType,
    )


class SyntheticsMobileStepParamsElementUserLocatorValuesItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.synthetics_mobile_step_params_element_user_locator_values_items_type import (
            SyntheticsMobileStepParamsElementUserLocatorValuesItemsType,
        )

        return {
            "type": (SyntheticsMobileStepParamsElementUserLocatorValuesItemsType,),
            "value": (str,),
        }

    attribute_map = {
        "type": "type",
        "value": "value",
    }

    def __init__(
        self_,
        type: Union[SyntheticsMobileStepParamsElementUserLocatorValuesItemsType, UnsetType] = unset,
        value: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        A single user locator object.

        :param type: Type of a user locator.
        :type type: SyntheticsMobileStepParamsElementUserLocatorValuesItemsType, optional

        :param value: Value of a user locator.
        :type value: str, optional
        """
        if type is not unset:
            kwargs["type"] = type
        if value is not unset:
            kwargs["value"] = value
        super().__init__(kwargs)
