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


class OpenAPIFile(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "openapi_spec_file": (file_type,),
        }

    attribute_map = {
        "openapi_spec_file": "openapi_spec_file",
    }

    def __init__(self_, openapi_spec_file: Union[file_type, UnsetType] = unset, **kwargs):
        """
        Object for API data in an ``OpenAPI`` format as a file.

        :param openapi_spec_file: Binary ``OpenAPI`` spec file
        :type openapi_spec_file: file_type, optional
        """
        if openapi_spec_file is not unset:
            kwargs["openapi_spec_file"] = openapi_spec_file
        super().__init__(kwargs)
