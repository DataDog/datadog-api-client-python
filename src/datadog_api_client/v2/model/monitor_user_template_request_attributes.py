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


class MonitorUserTemplateRequestAttributes(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.monitor_user_template_template_variables_items import (
            MonitorUserTemplateTemplateVariablesItems,
        )

        return {
            "description": (str,),
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
        }

    attribute_map = {
        "description": "description",
        "monitor_definition": "monitor_definition",
        "tags": "tags",
        "template_variables": "template_variables",
        "title": "title",
    }

    def __init__(
        self_,
        monitor_definition: Dict[str, Any],
        tags: List[str],
        title: str,
        description: Union[str, none_type, UnsetType] = unset,
        template_variables: Union[List[MonitorUserTemplateTemplateVariablesItems], UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for a monitor user template.

        :param description: A brief description of the monitor user template.
        :type description: str, none_type, optional

        :param monitor_definition: A valid monitor definition in the same format as the `V1 Monitor API <https://docs.datadoghq.com/api/latest/monitors/#create-a-monitor>`_.
        :type monitor_definition: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}

        :param tags: The definition of ``MonitorUserTemplateTags`` object.
        :type tags: [str]

        :param template_variables: The definition of ``MonitorUserTemplateTemplateVariables`` object.
        :type template_variables: [MonitorUserTemplateTemplateVariablesItems], optional

        :param title: The title of the monitor user template.
        :type title: str
        """
        if description is not unset:
            kwargs["description"] = description
        if template_variables is not unset:
            kwargs["template_variables"] = template_variables
        super().__init__(kwargs)

        self_.monitor_definition = monitor_definition
        self_.tags = tags
        self_.title = title
