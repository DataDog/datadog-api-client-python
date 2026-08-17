# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.files_coverage_attributes import FilesCoverageAttributes
    from datadog_api_client.v2.model.files_coverage_response_type import FilesCoverageResponseType


class FilesCoverageData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.files_coverage_attributes import FilesCoverageAttributes
        from datadog_api_client.v2.model.files_coverage_response_type import FilesCoverageResponseType

        return {
            "attributes": (FilesCoverageAttributes,),
            "id": (str,),
            "type": (FilesCoverageResponseType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[FilesCoverageAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        type: Union[FilesCoverageResponseType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Data object for files coverage response.

        :param attributes: Attributes of the per-file code coverage response.
        :type attributes: FilesCoverageAttributes, optional

        :param id: Unique identifier for the files coverage response.
        :type id: str, optional

        :param type: JSON:API type for files coverage response. The value must always be ``ci_app_coverage_files``.
        :type type: FilesCoverageResponseType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
