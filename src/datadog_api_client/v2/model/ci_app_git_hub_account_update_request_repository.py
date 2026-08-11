# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class CIAppGitHubAccountUpdateRequestRepository(ModelNormal):
    validations = {
        "name": {
            "min_length": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "enabled": (bool,),
            "name": (str,),
        }

    attribute_map = {
        "enabled": "enabled",
        "name": "name",
    }

    def __init__(self_, enabled: bool, name: str, **kwargs):
        """
        Repository-level opt-in change to apply, identified by name.

        :param enabled: Whether to enable or disable CI Visibility for this repository.
        :type enabled: bool

        :param name: The repository name to update.
        :type name: str
        """
        super().__init__(kwargs)

        self_.enabled = enabled
        self_.name = name
