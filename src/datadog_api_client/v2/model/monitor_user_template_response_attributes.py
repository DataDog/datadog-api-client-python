# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict, List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    date,
    datetime,
    none_type,
    unset,
    UnsetType,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.monitor_user_template_template_variables_items import (
        MonitorUserTemplateTemplateVariablesItems,
    )


class MonitorUserTemplateResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.monitor_user_template_template_variables_items import (
            MonitorUserTemplateTemplateVariablesItems,
        )

        return {
            "created": (datetime,),
            "description": (str,),
            "modified": (datetime,),
            "monitor_definition": (
                {
                    str: (
                        bool,
                        date,
                        datetime,
                        dict,
                        float,
                        int,
                        list,
                        str,
                        UUID,
                        none_type,
                    )
                },
            ),
            "tags": ([str],),
            "template_variables": ([MonitorUserTemplateTemplateVariablesItems],),
            "title": (str,),
            "version": (int,),
        }

    attribute_map = {
        "created": "created",
        "description": "description",
        "modified": "modified",
        "monitor_definition": "monitor_definition",
        "tags": "tags",
        "template_variables": "template_variables",
        "title": "title",
        "version": "version",
    }
    read_only_vars = {
        "created",
        "modified",
        "version",
    }

    def __init__(
        self_,
        created: Union[datetime, UnsetType] = unset,
        description: Union[str, none_type, UnsetType] = unset,
        modified: Union[datetime, UnsetType] = unset,
        monitor_definition: Union[Dict[str, Any], UnsetType] = unset,
        tags: Union[List[str], UnsetType] = unset,
        template_variables: Union[List[MonitorUserTemplateTemplateVariablesItems], UnsetType] = unset,
        title: Union[str, UnsetType] = unset,
        version: Union[int, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for a monitor user template.

        :param created: The created timestamp of the template.
        :type created: datetime, optional

        :param description: A brief description of the monitor user template.
        :type description: str, none_type, optional

        :param modified: The last modified timestamp. When the template version was created.
        :type modified: datetime, optional

        :param monitor_definition: A valid monitor definition in the same format as the `V1 Monitor API <https://docs.datadoghq.com/api/latest/monitors/#create-a-monitor>`_.
        :type monitor_definition: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, optional

        :param tags: The definition of ``MonitorUserTemplateTags`` object.
        :type tags: [str], optional

        :param template_variables: The definition of ``MonitorUserTemplateTemplateVariables`` object.
        :type template_variables: [MonitorUserTemplateTemplateVariablesItems], optional

        :param title: The title of the monitor user template.
        :type title: str, optional

        :param version: The version of the monitor user template.
        :type version: int, none_type, optional
        """
        if created is not unset:
            kwargs["created"] = created
        if description is not unset:
            kwargs["description"] = description
        if modified is not unset:
            kwargs["modified"] = modified
        if monitor_definition is not unset:
            kwargs["monitor_definition"] = monitor_definition
        if tags is not unset:
            kwargs["tags"] = tags
        if template_variables is not unset:
            kwargs["template_variables"] = template_variables
        if title is not unset:
            kwargs["title"] = title
        if version is not unset:
            kwargs["version"] = version
        super().__init__(kwargs)
