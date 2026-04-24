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
    from datadog_api_client.v2.model.synthetics_test_result_relationship_test import (
        SyntheticsTestResultRelationshipTest,
    )


class SyntheticsTestResultRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.synthetics_test_result_relationship_test import (
            SyntheticsTestResultRelationshipTest,
        )

        return {
            "test": (SyntheticsTestResultRelationshipTest,),
        }

    attribute_map = {
        "test": "test",
    }

    def __init__(self_, test: Union[SyntheticsTestResultRelationshipTest, UnsetType] = unset, **kwargs):
        """
        Relationships for a Synthetic test result.

        :param test: Relationship to the Synthetic test.
        :type test: SyntheticsTestResultRelationshipTest, optional
        """
        if test is not unset:
            kwargs["test"] = test
        super().__init__(kwargs)
