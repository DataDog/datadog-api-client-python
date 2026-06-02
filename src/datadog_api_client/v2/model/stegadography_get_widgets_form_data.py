# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    file_type,
    unset,
    UnsetType,
)


class StegadographyGetWidgetsFormData(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "image": (file_type,),
        }

    attribute_map = {
        "image": "image",
    }

    def __init__(self_, image: Union[file_type, UnsetType] = unset, **kwargs):
        """
        The form data submitted to look up widgets from a watermarked image.

        :param image: A PNG image (for example, a dashboard screenshot) containing embedded widget watermarks.
        :type image: file_type, optional
        """
        if image is not unset:
            kwargs["image"] = image
        super().__init__(kwargs)
