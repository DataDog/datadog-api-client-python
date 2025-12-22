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


class AttachmentDataAttributesAttachment(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "document_url": (str,),
            "title": (str,),
        }

    attribute_map = {
        "document_url": "documentUrl",
        "title": "title",
    }

    def __init__(self_, document_url: Union[str, UnsetType] = unset, title: Union[str, UnsetType] = unset, **kwargs):
        """


        :param document_url:
        :type document_url: str, optional

        :param title:
        :type title: str, optional
        """
        if document_url is not unset:
            kwargs["document_url"] = document_url
        if title is not unset:
            kwargs["title"] = title
        super().__init__(kwargs)
