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


class IncidentUserDefinedFieldImportRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "file": (file_type,),
        }

    attribute_map = {
        "file": "file",
    }

    def __init__(self_, file: Union[file_type, UnsetType] = unset, **kwargs):
        """
        Multipart form data for importing valid values for an incident user-defined field from a CSV file.

        :param file: A CSV file where each distinct value in the first column is imported as a valid value.
        :type file: file_type, optional
        """
        if file is not unset:
            kwargs["file"] = file
        super().__init__(kwargs)
