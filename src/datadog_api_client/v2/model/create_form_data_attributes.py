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
    from datadog_api_client.v2.model.form_data_definition import FormDataDefinition
    from datadog_api_client.v2.model.form_ui_definition import FormUiDefinition


class CreateFormDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.form_data_definition import FormDataDefinition
        from datadog_api_client.v2.model.form_ui_definition import FormUiDefinition

        return {
            "anonymous": (bool,),
            "data_definition": (FormDataDefinition,),
            "description": (str,),
            "idp_survey": (bool,),
            "name": (str,),
            "single_response": (bool,),
            "ui_definition": (FormUiDefinition,),
        }

    attribute_map = {
        "anonymous": "anonymous",
        "data_definition": "data_definition",
        "description": "description",
        "idp_survey": "idp_survey",
        "name": "name",
        "single_response": "single_response",
        "ui_definition": "ui_definition",
    }

    def __init__(
        self_,
        data_definition: FormDataDefinition,
        name: str,
        ui_definition: FormUiDefinition,
        anonymous: Union[bool, UnsetType] = unset,
        description: Union[str, UnsetType] = unset,
        idp_survey: Union[bool, UnsetType] = unset,
        single_response: Union[bool, UnsetType] = unset,
        **kwargs,
    ):
        """
        The attributes for creating a form.

        :param anonymous: Whether the form accepts anonymous submissions.
        :type anonymous: bool, optional

        :param data_definition: A JSON Schema definition that describes the form's data fields.
        :type data_definition: FormDataDefinition

        :param description: The description of the form.
        :type description: str, optional

        :param idp_survey: Whether the form is an IDP survey.
        :type idp_survey: bool, optional

        :param name: The name of the form.
        :type name: str

        :param single_response: Whether each user can only submit one response.
        :type single_response: bool, optional

        :param ui_definition: UI configuration for rendering form fields, including widget overrides, field ordering, and themes.
        :type ui_definition: FormUiDefinition
        """
        if anonymous is not unset:
            kwargs["anonymous"] = anonymous
        if description is not unset:
            kwargs["description"] = description
        if idp_survey is not unset:
            kwargs["idp_survey"] = idp_survey
        if single_response is not unset:
            kwargs["single_response"] = single_response
        super().__init__(kwargs)

        self_.data_definition = data_definition
        self_.name = name
        self_.ui_definition = ui_definition
