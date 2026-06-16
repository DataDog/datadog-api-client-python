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
    from datadog_api_client.v2.model.form_version_attributes import FormVersionAttributes
    from datadog_api_client.v2.model.form_version_type import FormVersionType


class FormVersionData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.form_version_attributes import FormVersionAttributes
        from datadog_api_client.v2.model.form_version_type import FormVersionType

        return {
            "attributes": (FormVersionAttributes,),
            "id": (str,),
            "type": (FormVersionType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: FormVersionAttributes, id: str, type: FormVersionType, **kwargs):
        """
        A form version resource object.

        :param attributes: The attributes of a form version.
        :type attributes: FormVersionAttributes

        :param id: The ID of the form version.
        :type id: str

        :param type: The resource type for a form version.
        :type type: FormVersionType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
