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


class EntityV3APISpecInterfaceFileRef(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        return {
            "file_ref": (str,),
        }

    attribute_map = {
        "file_ref": "fileRef",
    }

    def __init__(self_, file_ref: Union[str, UnsetType] = unset, **kwargs):
        """
        The definition of ``EntityV3APISpecInterfaceFileRef`` object.

        :param file_ref: The reference to the API definition file.
        :type file_ref: str, optional
        """
        if file_ref is not unset:
            kwargs["file_ref"] = file_ref
        super().__init__(kwargs)
