# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class UpdateConnectionRequestDataAttributesFieldsToUpdateItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "field_id": (str,),
            "updated_description": (str,),
            "updated_display_name": (str,),
            "updated_field_id": (str,),
            "updated_groups": ([str],),
        }

    attribute_map = {
        "field_id": "field_id",
        "updated_description": "updated_description",
        "updated_display_name": "updated_display_name",
        "updated_field_id": "updated_field_id",
        "updated_groups": "updated_groups",
    }

    def __init__(
        self_,
        field_id: str,
        updated_description: Union[str, UnsetType] = unset,
        updated_display_name: Union[str, UnsetType] = unset,
        updated_field_id: Union[str, UnsetType] = unset,
        updated_groups: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """


        :param field_id:
        :type field_id: str

        :param updated_description:
        :type updated_description: str, optional

        :param updated_display_name:
        :type updated_display_name: str, optional

        :param updated_field_id:
        :type updated_field_id: str, optional

        :param updated_groups:
        :type updated_groups: [str], optional
        """
        if updated_description is not unset:
            kwargs["updated_description"] = updated_description
        if updated_display_name is not unset:
            kwargs["updated_display_name"] = updated_display_name
        if updated_field_id is not unset:
            kwargs["updated_field_id"] = updated_field_id
        if updated_groups is not unset:
            kwargs["updated_groups"] = updated_groups
        super().__init__(kwargs)

        self_.field_id = field_id
