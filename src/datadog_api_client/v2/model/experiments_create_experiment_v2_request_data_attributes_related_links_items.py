# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


class ExperimentsCreateExperimentV2RequestDataAttributesRelatedLinksItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "id": (str, none_type),
            "title": (str, none_type),
            "url": (str,),
        }

    attribute_map = {
        "id": "id",
        "title": "title",
        "url": "url",
    }

    def __init__(
        self_,
        url: str,
        id: Union[str, none_type, UnsetType] = unset,
        title: Union[str, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        External link associated with an experiment.

        :param id: Link ID. Omit it when adding a link.
        :type id: str, none_type, optional

        :param title: Optional display title.
        :type title: str, none_type, optional

        :param url: Absolute URL.
        :type url: str
        """
        if id is not unset:
            kwargs["id"] = id
        if title is not unset:
            kwargs["title"] = title
        super().__init__(kwargs)

        self_.url = url
