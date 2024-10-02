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
    from datadog_api_client.v1.model.synthetics_mobile_test_initial_application_arguments_property_names import (
        SyntheticsMobileTestInitialApplicationArgumentsPropertyNames,
    )


class SyntheticsMobileTestInitialApplicationArguments(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.synthetics_mobile_test_initial_application_arguments_property_names import (
            SyntheticsMobileTestInitialApplicationArgumentsPropertyNames,
        )

        return {
            "property_names": (SyntheticsMobileTestInitialApplicationArgumentsPropertyNames,),
        }

    attribute_map = {
        "property_names": "propertyNames",
    }

    def __init__(
        self_,
        property_names: Union[SyntheticsMobileTestInitialApplicationArgumentsPropertyNames, UnsetType] = unset,
        **kwargs,
    ):
        """
        Initial application arguments for a mobile test.

        :param property_names: Name of the property.
        :type property_names: SyntheticsMobileTestInitialApplicationArgumentsPropertyNames, optional
        """
        if property_names is not unset:
            kwargs["property_names"] = property_names
        super().__init__(kwargs)
