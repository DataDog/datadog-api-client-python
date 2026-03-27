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
    from datadog_api_client.v2.model.synthetics_test_parent_suite_data import SyntheticsTestParentSuiteData


class SyntheticsTestParentSuitesResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.synthetics_test_parent_suite_data import SyntheticsTestParentSuiteData

        return {
            "data": ([SyntheticsTestParentSuiteData],),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: Union[List[SyntheticsTestParentSuiteData], UnsetType] = unset, **kwargs):
        """
        Response containing the list of parent suites for a Synthetic test.

        :param data: List of parent suites for the given test.
        :type data: [SyntheticsTestParentSuiteData], optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
