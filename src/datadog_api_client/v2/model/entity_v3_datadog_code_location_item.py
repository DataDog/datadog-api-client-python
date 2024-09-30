# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class EntityV3DatadogCodeLocationItem(ModelNormal):
    validations = {
        "repository_url": {},
    }

    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        return {
            "paths": ([str],),
            "repository_url": (str,),
        }

    attribute_map = {
        "paths": "paths",
        "repository_url": "repositoryURL",
    }

    def __init__(
        self_, paths: Union[List[str], UnsetType] = unset, repository_url: Union[str, UnsetType] = unset, **kwargs
    ):
        """
        code location item.

        :param paths: The paths (glob) to the source code of the service
        :type paths: [str], optional

        :param repository_url: The repository path of the source code of the entity
        :type repository_url: str, optional
        """
        if paths is not unset:
            kwargs["paths"] = paths
        if repository_url is not unset:
            kwargs["repository_url"] = repository_url
        super().__init__(kwargs)
