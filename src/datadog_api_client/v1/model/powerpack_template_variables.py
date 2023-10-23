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
    from datadog_api_client.v1.model.powerpack_template_variable_contents import PowerpackTemplateVariableContents


class PowerpackTemplateVariables(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.powerpack_template_variable_contents import PowerpackTemplateVariableContents

        return {
            "controlled_by_powerpack": ([PowerpackTemplateVariableContents],),
            "controlled_externally": ([PowerpackTemplateVariableContents],),
        }

    attribute_map = {
        "controlled_by_powerpack": "controlled_by_powerpack",
        "controlled_externally": "controlled_externally",
    }

    def __init__(
        self_,
        controlled_by_powerpack: Union[List[PowerpackTemplateVariableContents], UnsetType] = unset,
        controlled_externally: Union[List[PowerpackTemplateVariableContents], UnsetType] = unset,
        **kwargs,
    ):
        """
        Powerpack template variables.

        :param controlled_by_powerpack: Template variables controlled at the powerpack level.
        :type controlled_by_powerpack: [PowerpackTemplateVariableContents], optional

        :param controlled_externally: Template variables controlled by the external resource, such as the dashboard this powerpack is on.
        :type controlled_externally: [PowerpackTemplateVariableContents], optional
        """
        if controlled_by_powerpack is not unset:
            kwargs["controlled_by_powerpack"] = controlled_by_powerpack
        if controlled_externally is not unset:
            kwargs["controlled_externally"] = controlled_externally
        super().__init__(kwargs)
