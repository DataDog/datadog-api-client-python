# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.form_version_data_attributes_response import FormVersionDataAttributesResponse
    from datadog_api_client.v2.model.form_version_type import FormVersionType


class FormVersionDataResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.form_version_data_attributes_response import FormVersionDataAttributesResponse
        from datadog_api_client.v2.model.form_version_type import FormVersionType

        return {
            "attributes": (FormVersionDataAttributesResponse,),
            "id": (str,),
            "type": (FormVersionType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: FormVersionDataAttributesResponse, id: str, type: FormVersionType, **kwargs):
        """


        :param attributes: Attributes of a form version.
        :type attributes: FormVersionDataAttributesResponse

        :param id: The version identifier.
        :type id: str

        :param type: Type for form versions.
        :type type: FormVersionType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
