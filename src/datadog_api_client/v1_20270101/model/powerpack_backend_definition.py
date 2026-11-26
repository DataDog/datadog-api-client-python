# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v1_20270101.model.powerpack_state import PowerpackState
    from datadog_api_client.v1_20270101.model.powerpack_backend_template_variables import (
        PowerpackBackendTemplateVariables,
    )
    from datadog_api_client.v1_20270101.model.powerpack_backend_definition_type import PowerpackBackendDefinitionType


class PowerpackBackendDefinition(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.powerpack_state import PowerpackState
        from datadog_api_client.v1_20270101.model.powerpack_backend_template_variables import (
            PowerpackBackendTemplateVariables,
        )
        from datadog_api_client.v1_20270101.model.powerpack_backend_definition_type import (
            PowerpackBackendDefinitionType,
        )

        return {
            "background_color": (str,),
            "banner_img": (str,),
            "powerpack_id": (str,),
            "show_title": (bool,),
            "state": (PowerpackState,),
            "template_variables": (PowerpackBackendTemplateVariables,),
            "title": (str,),
            "type": (PowerpackBackendDefinitionType,),
        }

    attribute_map = {
        "background_color": "background_color",
        "banner_img": "banner_img",
        "powerpack_id": "powerpack_id",
        "show_title": "show_title",
        "state": "state",
        "template_variables": "template_variables",
        "title": "title",
        "type": "type",
    }

    def __init__(
        self_,
        powerpack_id: str,
        type: PowerpackBackendDefinitionType,
        background_color: Union[str, UnsetType] = unset,
        banner_img: Union[str, UnsetType] = unset,
        show_title: Union[bool, UnsetType] = unset,
        state: Union[PowerpackState, UnsetType] = unset,
        template_variables: Union[PowerpackBackendTemplateVariables, UnsetType] = unset,
        title: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param background_color: Test-only generated schema for the dashboard versioning proof of concept.
        :type background_color: str, optional

        :param banner_img: Test-only generated schema for the dashboard versioning proof of concept.
        :type banner_img: str, optional

        :param powerpack_id: Test-only generated schema for the dashboard versioning proof of concept.
        :type powerpack_id: str

        :param show_title: Test-only generated schema for the dashboard versioning proof of concept.
        :type show_title: bool, optional

        :param state: Test-only generated schema for the dashboard versioning proof of concept.
        :type state: PowerpackState, optional

        :param template_variables: Test-only generated schema for the dashboard versioning proof of concept.
        :type template_variables: PowerpackBackendTemplateVariables, optional

        :param title: Test-only generated schema for the dashboard versioning proof of concept.
        :type title: str, optional

        :param type: Test-only generated schema for the dashboard versioning proof of concept.
        :type type: PowerpackBackendDefinitionType
        """
        if background_color is not unset:
            kwargs["background_color"] = background_color
        if banner_img is not unset:
            kwargs["banner_img"] = banner_img
        if show_title is not unset:
            kwargs["show_title"] = show_title
        if state is not unset:
            kwargs["state"] = state
        if template_variables is not unset:
            kwargs["template_variables"] = template_variables
        if title is not unset:
            kwargs["title"] = title
        super().__init__(kwargs)

        self_.powerpack_id = powerpack_id
        self_.type = type
