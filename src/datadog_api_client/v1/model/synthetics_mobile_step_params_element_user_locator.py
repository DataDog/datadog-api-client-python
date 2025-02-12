# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v1.model.synthetics_mobile_step_params_element_user_locator_values_items import (
        SyntheticsMobileStepParamsElementUserLocatorValuesItems,
    )


class SyntheticsMobileStepParamsElementUserLocator(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.synthetics_mobile_step_params_element_user_locator_values_items import (
            SyntheticsMobileStepParamsElementUserLocatorValuesItems,
        )

        return {
            "fail_test_on_cannot_locate": (bool,),
            "values": ([SyntheticsMobileStepParamsElementUserLocatorValuesItems],),
        }

    attribute_map = {
        "fail_test_on_cannot_locate": "failTestOnCannotLocate",
        "values": "values",
    }

    def __init__(
        self_,
        fail_test_on_cannot_locate: Union[bool, UnsetType] = unset,
        values: Union[List[SyntheticsMobileStepParamsElementUserLocatorValuesItems], UnsetType] = unset,
        **kwargs,
    ):
        """
        User locator to find the element.

        :param fail_test_on_cannot_locate: Whether if the test should fail if the element cannot be found.
        :type fail_test_on_cannot_locate: bool, optional

        :param values: Values of the user locator.
        :type values: [SyntheticsMobileStepParamsElementUserLocatorValuesItems], optional
        """
        if fail_test_on_cannot_locate is not unset:
            kwargs["fail_test_on_cannot_locate"] = fail_test_on_cannot_locate
        if values is not unset:
            kwargs["values"] = values
        super().__init__(kwargs)
