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
    from datadog_api_client.v2.model.list_form_versions_data_attributes import ListFormVersionsDataAttributes
    from datadog_api_client.v2.model.form_version_list_type import FormVersionListType


class ListFormVersionsData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.list_form_versions_data_attributes import ListFormVersionsDataAttributes
        from datadog_api_client.v2.model.form_version_list_type import FormVersionListType

        return {
            "attributes": (ListFormVersionsDataAttributes,),
            "id": (str,),
            "type": (FormVersionListType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: ListFormVersionsDataAttributes, id: str, type: FormVersionListType, **kwargs):
        """
        A list-of-form-versions resource object.

        :param attributes: The attributes for a list of form versions.
        :type attributes: ListFormVersionsDataAttributes

        :param id: The ID of the form.
        :type id: str

        :param type: The resource type for a list of form versions.
        :type type: FormVersionListType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
