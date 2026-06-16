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
    from datadog_api_client.v2.model.form_publication_attributes import FormPublicationAttributes
    from datadog_api_client.v2.model.form_publication_type import FormPublicationType


class FormPublicationData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.form_publication_attributes import FormPublicationAttributes
        from datadog_api_client.v2.model.form_publication_type import FormPublicationType

        return {
            "attributes": (FormPublicationAttributes,),
            "id": (str,),
            "type": (FormPublicationType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: FormPublicationAttributes, id: str, type: FormPublicationType, **kwargs):
        """
        A form publication resource object.

        :param attributes: The attributes of a form publication.
        :type attributes: FormPublicationAttributes

        :param id: The ID of the form publication.
        :type id: str

        :param type: The resource type for a form publication.
        :type type: FormPublicationType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
