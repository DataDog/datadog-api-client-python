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


class CIAppPipelineEventParentPipeline(ModelNormal):
    _nullable = True

    @cached_property
    def openapi_types(_):
        return {
            "id": (str,),
            "url": (str,),
        }

    attribute_map = {
        "id": "id",
        "url": "url",
    }

    def __init__(self_, id: str, url: Union[str, UnsetType] = unset, **kwargs):
        """
        If the pipeline is triggered as child of another pipeline, this should contain the details of the parent pipeline.

        :param id: UUID of a pipeline.
        :type id: str

        :param url: The URL to look at the pipeline in the CI provider UI.
        :type url: str, optional
        """
        if url is not unset:
            kwargs["url"] = url
        super().__init__(kwargs)

        self_.id = id
