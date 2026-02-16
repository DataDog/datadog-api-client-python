# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.form_data_attributes_response import FormDataAttributesResponse
    from datadog_api_client.v2.model.form_type import FormType


class FormDataResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.form_data_attributes_response import FormDataAttributesResponse
        from datadog_api_client.v2.model.form_type import FormType

        return {
            "attributes": (FormDataAttributesResponse,),
            "id": (UUID,),
            "type": (FormType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: FormDataAttributesResponse, id: UUID, type: FormType, **kwargs):
        """


        :param attributes: Attributes of a form.
        :type attributes: FormDataAttributesResponse

        :param id: The form identifier.
        :type id: UUID

        :param type: Type for forms.
        :type type: FormType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
