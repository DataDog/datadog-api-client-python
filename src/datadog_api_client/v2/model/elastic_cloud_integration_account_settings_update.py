# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class ElasticCloudIntegrationAccountSettingsUpdate(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "tags": (str,),
            "url": (str,),
        }

    attribute_map = {
        "tags": "tags",
        "url": "url",
    }

    def __init__(self_, tags: Union[str, UnsetType] = unset, url: Union[str, UnsetType] = unset, **kwargs):
        """
        Settings for updating the Elastic Cloud integration account. Only the fields provided are changed.

        :param tags: Comma-separated list of custom tags for this Elastic Cloud deployment.
        :type tags: str, optional

        :param url: Elastic Cloud deployment URL.
        :type url: str, optional
        """
        if tags is not unset:
            kwargs["tags"] = tags
        if url is not unset:
            kwargs["url"] = url
        super().__init__(kwargs)
