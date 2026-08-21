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


class TeamsOwnershipMappingBatchError(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "detail": (str,),
            "status": (str,),
            "title": (str,),
        }

    attribute_map = {
        "detail": "detail",
        "status": "status",
        "title": "title",
    }

    def __init__(self_, status: str, title: str, detail: Union[str, UnsetType] = unset, **kwargs):
        """
        An error encountered while validating or applying an operation.

        :param detail: A human-readable explanation specific to this error.
        :type detail: str, optional

        :param status: The HTTP status code applicable to this error.
        :type status: str

        :param title: A short, human-readable summary of the error.
        :type title: str
        """
        if detail is not unset:
            kwargs["detail"] = detail
        super().__init__(kwargs)

        self_.status = status
        self_.title = title
