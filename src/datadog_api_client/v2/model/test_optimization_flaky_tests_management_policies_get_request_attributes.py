# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class TestOptimizationFlakyTestsManagementPoliciesGetRequestAttributes(ModelNormal):
    validations = {
        "repository_id": {
            "min_length": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "repository_id": (str,),
        }

    attribute_map = {
        "repository_id": "repository_id",
    }

    def __init__(self_, repository_id: str, **kwargs):
        """
        Attributes for requesting Flaky Tests Management policies.

        :param repository_id: The repository identifier.
        :type repository_id: str
        """
        super().__init__(kwargs)

        self_.repository_id = repository_id
