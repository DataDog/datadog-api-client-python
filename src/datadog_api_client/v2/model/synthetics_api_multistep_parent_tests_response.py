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
    from datadog_api_client.v2.model.synthetics_api_multistep_parent_test_data import (
        SyntheticsApiMultistepParentTestData,
    )


class SyntheticsApiMultistepParentTestsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.synthetics_api_multistep_parent_test_data import (
            SyntheticsApiMultistepParentTestData,
        )

        return {
            "data": ([SyntheticsApiMultistepParentTestData],),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: Union[List[SyntheticsApiMultistepParentTestData], UnsetType] = unset, **kwargs):
        """
        Response containing the list of parent tests for an API multistep subtest.

        :param data: List of parent tests that include this subtest.
        :type data: [SyntheticsApiMultistepParentTestData], optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
