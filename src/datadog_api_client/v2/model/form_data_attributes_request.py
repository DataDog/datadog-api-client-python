# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class FormDataAttributesRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "data_definition": (dict,),
            "description": (str,),
            "name": (str,),
            "ui_definition": (dict,),
        }

    attribute_map = {
        "data_definition": "data_definition",
        "description": "description",
        "name": "name",
        "ui_definition": "ui_definition",
    }

    def __init__(self_, data_definition: dict, description: str, name: str, ui_definition: dict, **kwargs):
        """
        Attributes for creating a form.

        :param data_definition: The data definition for the form.
        :type data_definition: dict

        :param description: The description of the form.
        :type description: str

        :param name: The name of the form.
        :type name: str

        :param ui_definition: The UI definition for the form.
        :type ui_definition: dict
        """
        super().__init__(kwargs)

        self_.data_definition = data_definition
        self_.description = description
        self_.name = name
        self_.ui_definition = ui_definition
