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
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.update_form_data_attributes import UpdateFormDataAttributes
    from datadog_api_client.v2.model.form_type import FormType


class UpdateFormData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.update_form_data_attributes import UpdateFormDataAttributes
        from datadog_api_client.v2.model.form_type import FormType

        return {
            "attributes": (UpdateFormDataAttributes,),
            "id": (UUID,),
            "type": (FormType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, attributes: UpdateFormDataAttributes, type: FormType, id: Union[UUID, UnsetType] = unset, **kwargs
    ):
        """
        The data for updating a form.

        :param attributes: The attributes for updating a form.
        :type attributes: UpdateFormDataAttributes

        :param id: The ID of the form.
        :type id: UUID, optional

        :param type: The resource type for a form.
        :type type: FormType
        """
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
