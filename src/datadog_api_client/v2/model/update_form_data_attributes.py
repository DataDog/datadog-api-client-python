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
    from datadog_api_client.v2.model.form_update_attributes import FormUpdateAttributes


class UpdateFormDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.form_update_attributes import FormUpdateAttributes

        return {
            "form_update": (FormUpdateAttributes,),
        }

    attribute_map = {
        "form_update": "form_update",
    }

    def __init__(self_, form_update: FormUpdateAttributes, **kwargs):
        """
        The attributes for updating a form.

        :param form_update: The fields to update on a form. At least one field must be provided.
        :type form_update: FormUpdateAttributes
        """
        super().__init__(kwargs)

        self_.form_update = form_update
