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
    from datadog_api_client.v2.model.form_type import FormType


class DeleteFormData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.form_type import FormType

        return {
            "id": (UUID,),
            "type": (FormType,),
        }

    attribute_map = {
        "id": "id",
        "type": "type",
    }

    def __init__(self_, id: UUID, type: FormType, **kwargs):
        """
        The data returned when a form is deleted.

        :param id: The ID of the deleted form.
        :type id: UUID

        :param type: The resource type for a form.
        :type type: FormType
        """
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
