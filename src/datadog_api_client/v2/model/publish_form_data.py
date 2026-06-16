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
    from datadog_api_client.v2.model.publish_form_data_attributes import PublishFormDataAttributes
    from datadog_api_client.v2.model.form_publication_type import FormPublicationType


class PublishFormData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.publish_form_data_attributes import PublishFormDataAttributes
        from datadog_api_client.v2.model.form_publication_type import FormPublicationType

        return {
            "attributes": (PublishFormDataAttributes,),
            "type": (FormPublicationType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: PublishFormDataAttributes, type: FormPublicationType, **kwargs):
        """
        The data for publishing a form version.

        :param attributes: The attributes for publishing a form version.
        :type attributes: PublishFormDataAttributes

        :param type: The resource type for a form publication.
        :type type: FormPublicationType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
