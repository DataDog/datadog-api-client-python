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
    from datadog_api_client.v1.model.synthetics_mobile_test_initial_application_arguments import (
        SyntheticsMobileTestInitialApplicationArguments,
    )
    from datadog_api_client.v1.model.synthetics_config_variable import SyntheticsConfigVariable


class SyntheticsMobileTestConfig(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.synthetics_mobile_test_initial_application_arguments import (
            SyntheticsMobileTestInitialApplicationArguments,
        )
        from datadog_api_client.v1.model.synthetics_config_variable import SyntheticsConfigVariable

        return {
            "initial_application_arguments": (SyntheticsMobileTestInitialApplicationArguments,),
            "variables": ([SyntheticsConfigVariable],),
        }

    attribute_map = {
        "initial_application_arguments": "initialApplicationArguments",
        "variables": "variables",
    }

    def __init__(
        self_,
        initial_application_arguments: Union[SyntheticsMobileTestInitialApplicationArguments, UnsetType] = unset,
        variables: Union[List[SyntheticsConfigVariable], UnsetType] = unset,
        **kwargs,
    ):
        """
        Configuration object for a Synthetic mobile test.

        :param initial_application_arguments: Initial application arguments for a mobile test.
        :type initial_application_arguments: SyntheticsMobileTestInitialApplicationArguments, optional

        :param variables: Array of variables used for the test steps.
        :type variables: [SyntheticsConfigVariable], optional
        """
        if initial_application_arguments is not unset:
            kwargs["initial_application_arguments"] = initial_application_arguments
        if variables is not unset:
            kwargs["variables"] = variables
        super().__init__(kwargs)
