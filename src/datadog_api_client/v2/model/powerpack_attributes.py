# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.powerpack_group_widget import PowerpackGroupWidget
    from datadog_api_client.v2.model.powerpack_template_variable import PowerpackTemplateVariable


class PowerpackAttributes(ModelNormal):
    validations = {
        "tags": {
            "max_items": 8,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.powerpack_group_widget import PowerpackGroupWidget
        from datadog_api_client.v2.model.powerpack_template_variable import PowerpackTemplateVariable

        return {
            "description": (str,),
            "group_widget": (PowerpackGroupWidget,),
            "name": (str,),
            "tags": ([str],),
            "template_variables": ([PowerpackTemplateVariable],),
        }

    attribute_map = {
        "description": "description",
        "group_widget": "group_widget",
        "name": "name",
        "tags": "tags",
        "template_variables": "template_variables",
    }

    def __init__(
        self_,
        group_widget: PowerpackGroupWidget,
        name: str,
        description: Union[str, UnsetType] = unset,
        tags: Union[List[str], UnsetType] = unset,
        template_variables: Union[List[PowerpackTemplateVariable], UnsetType] = unset,
        **kwargs,
    ):
        """
        Powerpack attribute object.

        :param description: Description of this powerpack.
        :type description: str, optional

        :param group_widget: Powerpack group widget definition object.
        :type group_widget: PowerpackGroupWidget

        :param name: Name of the powerpack.
        :type name: str

        :param tags: List of tags to identify this powerpack.
        :type tags: [str], optional

        :param template_variables: List of template variables for this powerpack.
        :type template_variables: [PowerpackTemplateVariable], optional
        """
        if description is not unset:
            kwargs["description"] = description
        if tags is not unset:
            kwargs["tags"] = tags
        if template_variables is not unset:
            kwargs["template_variables"] = template_variables
        super().__init__(kwargs)

        self_.group_widget = group_widget
        self_.name = name
