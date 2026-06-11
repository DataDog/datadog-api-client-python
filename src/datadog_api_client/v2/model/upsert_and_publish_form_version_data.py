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
    from datadog_api_client.v2.model.upsert_and_publish_form_version_data_attributes import (
        UpsertAndPublishFormVersionDataAttributes,
    )
    from datadog_api_client.v2.model.form_version_type import FormVersionType


class UpsertAndPublishFormVersionData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.upsert_and_publish_form_version_data_attributes import (
            UpsertAndPublishFormVersionDataAttributes,
        )
        from datadog_api_client.v2.model.form_version_type import FormVersionType

        return {
            "attributes": (UpsertAndPublishFormVersionDataAttributes,),
            "type": (FormVersionType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: UpsertAndPublishFormVersionDataAttributes, type: FormVersionType, **kwargs):
        """
        The data for upserting and publishing a form version.

        :param attributes: The attributes for upserting and publishing a form version.
        :type attributes: UpsertAndPublishFormVersionDataAttributes

        :param type: The resource type for a form version.
        :type type: FormVersionType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
