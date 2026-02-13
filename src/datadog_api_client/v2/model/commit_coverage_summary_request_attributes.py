# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class CommitCoverageSummaryRequestAttributes(ModelNormal):
    validations = {
        "commit_sha": {},
        "repository_id": {
            "min_length": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "commit_sha": (str,),
            "repository_id": (str,),
        }

    attribute_map = {
        "commit_sha": "commit_sha",
        "repository_id": "repository_id",
    }

    def __init__(self_, commit_sha: str, repository_id: str, **kwargs):
        """
        Attributes for requesting code coverage summary for a commit.

        :param commit_sha: The commit SHA (40-character hexadecimal string).
        :type commit_sha: str

        :param repository_id: The repository identifier.
        :type repository_id: str
        """
        super().__init__(kwargs)

        self_.commit_sha = commit_sha
        self_.repository_id = repository_id
