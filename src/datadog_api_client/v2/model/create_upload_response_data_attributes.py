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


class CreateUploadResponseDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "part_urls": ([str],),
        }

    attribute_map = {
        "part_urls": "part_urls",
    }

    def __init__(self_, part_urls: Union[List[str], UnsetType] = unset, **kwargs):
        """
        The definition of the upload response attributes object.

        :param part_urls: The URLs of the parts in the upload.
        :type part_urls: [str], optional
        """
        if part_urls is not unset:
            kwargs["part_urls"] = part_urls
        super().__init__(kwargs)
