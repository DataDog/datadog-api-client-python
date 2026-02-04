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
    from datadog_api_client.v2.model.form_update_attributes_form_update import FormUpdateAttributesFormUpdate


class FormUpdateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.form_update_attributes_form_update import FormUpdateAttributesFormUpdate

        return {
            "form_update": (FormUpdateAttributesFormUpdate,),
        }

    attribute_map = {
        "form_update": "form_update",
    }

    def __init__(self_, form_update: Union[FormUpdateAttributesFormUpdate, UnsetType] = unset, **kwargs):
        """
        Attributes for updating a form.

        :param form_update: Update parameters for the form.
        :type form_update: FormUpdateAttributesFormUpdate, optional
        """
        if form_update is not unset:
            kwargs["form_update"] = form_update
        super().__init__(kwargs)
