# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class DORAGitInfoResponse(ModelNormal):
    validations = {
        "commit_sha": {},
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
        Git info returned by DORA Metrics events.

        :param commit_sha: Git Commit SHA.
        :type commit_sha: str

        :param repository_id: Git Repository ID
        :type repository_id: str
        """
        super().__init__(kwargs)

        self_.commit_sha = commit_sha
        self_.repository_id = repository_id
