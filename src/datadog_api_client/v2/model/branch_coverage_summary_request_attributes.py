# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class BranchCoverageSummaryRequestAttributes(ModelNormal):
    validations = {
        "branch": {
            "min_length": 1,
        },
        "repository_id": {
            "min_length": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "branch": (str,),
            "repository_id": (str,),
        }

    attribute_map = {
        "branch": "branch",
        "repository_id": "repository_id",
    }

    def __init__(self_, branch: str, repository_id: str, **kwargs):
        """
        Attributes for requesting code coverage summary for a branch.

        :param branch: The branch name.
        :type branch: str

        :param repository_id: The repository identifier.
        :type repository_id: str
        """
        super().__init__(kwargs)

        self_.branch = branch
        self_.repository_id = repository_id
