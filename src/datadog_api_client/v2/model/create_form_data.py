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
    from datadog_api_client.v2.model.create_form_data_attributes import CreateFormDataAttributes
    from datadog_api_client.v2.model.form_type import FormType


class CreateFormData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.create_form_data_attributes import CreateFormDataAttributes
        from datadog_api_client.v2.model.form_type import FormType

        return {
            "attributes": (CreateFormDataAttributes,),
            "type": (FormType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: CreateFormDataAttributes, type: FormType, **kwargs):
        """
        The data for creating a form.

        :param attributes: The attributes for creating a form.
        :type attributes: CreateFormDataAttributes

        :param type: The resource type for a form.
        :type type: FormType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
