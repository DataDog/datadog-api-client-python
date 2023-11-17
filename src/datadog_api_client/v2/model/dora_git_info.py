# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class DORAGitInfo(ModelNormal):
    validations = {
        "commit_sha": {},
    }

    @cached_property
    def openapi_types(_):
        return {
            "commit_sha": (str,),
            "repository_url": (str,),
        }

    attribute_map = {
        "commit_sha": "commit_sha",
        "repository_url": "repository_url",
    }

    def __init__(self_, commit_sha: str, repository_url: str, **kwargs):
        """
        Git info for DORA Metrics events.

        :param commit_sha: Git Commit SHA.
        :type commit_sha: str

        :param repository_url: Git Repository URL
        :type repository_url: str
        """
        super().__init__(kwargs)

        self_.commit_sha = commit_sha
        self_.repository_url = repository_url
