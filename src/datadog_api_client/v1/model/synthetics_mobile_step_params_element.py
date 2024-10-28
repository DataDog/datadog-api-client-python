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
    from datadog_api_client.v1.model.synthetics_mobile_step_params_element_context_type import (
        SyntheticsMobileStepParamsElementContextType,
    )
    from datadog_api_client.v1.model.synthetics_mobile_step_params_element_relative_position import (
        SyntheticsMobileStepParamsElementRelativePosition,
    )
    from datadog_api_client.v1.model.synthetics_mobile_step_params_element_user_locator import (
        SyntheticsMobileStepParamsElementUserLocator,
    )


class SyntheticsMobileStepParamsElement(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.synthetics_mobile_step_params_element_context_type import (
            SyntheticsMobileStepParamsElementContextType,
        )
        from datadog_api_client.v1.model.synthetics_mobile_step_params_element_relative_position import (
            SyntheticsMobileStepParamsElementRelativePosition,
        )
        from datadog_api_client.v1.model.synthetics_mobile_step_params_element_user_locator import (
            SyntheticsMobileStepParamsElementUserLocator,
        )

        return {
            "context": (str,),
            "context_type": (SyntheticsMobileStepParamsElementContextType,),
            "element_description": (str,),
            "multi_locator": (dict,),
            "relative_position": (SyntheticsMobileStepParamsElementRelativePosition,),
            "text_content": (str,),
            "user_locator": (SyntheticsMobileStepParamsElementUserLocator,),
            "view_name": (str,),
        }

    attribute_map = {
        "context": "context",
        "context_type": "contextType",
        "element_description": "elementDescription",
        "multi_locator": "multiLocator",
        "relative_position": "relativePosition",
        "text_content": "textContent",
        "user_locator": "userLocator",
        "view_name": "viewName",
    }

    def __init__(
        self_,
        context: Union[str, UnsetType] = unset,
        context_type: Union[SyntheticsMobileStepParamsElementContextType, UnsetType] = unset,
        element_description: Union[str, UnsetType] = unset,
        multi_locator: Union[dict, UnsetType] = unset,
        relative_position: Union[SyntheticsMobileStepParamsElementRelativePosition, UnsetType] = unset,
        text_content: Union[str, UnsetType] = unset,
        user_locator: Union[SyntheticsMobileStepParamsElementUserLocator, UnsetType] = unset,
        view_name: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Information about the element used for a step.

        :param context: Context of the element.
        :type context: str, optional

        :param context_type: Type of the context that the element is in.
        :type context_type: SyntheticsMobileStepParamsElementContextType, optional

        :param element_description: Description of the element.
        :type element_description: str, optional

        :param multi_locator: Multi-locator to find the element.
        :type multi_locator: dict, optional

        :param relative_position: Position of the action relative to the element.
        :type relative_position: SyntheticsMobileStepParamsElementRelativePosition, optional

        :param text_content: Text content of the element.
        :type text_content: str, optional

        :param user_locator: User locator to find the element.
        :type user_locator: SyntheticsMobileStepParamsElementUserLocator, optional

        :param view_name: Name of the view of the element.
        :type view_name: str, optional
        """
        if context is not unset:
            kwargs["context"] = context
        if context_type is not unset:
            kwargs["context_type"] = context_type
        if element_description is not unset:
            kwargs["element_description"] = element_description
        if multi_locator is not unset:
            kwargs["multi_locator"] = multi_locator
        if relative_position is not unset:
            kwargs["relative_position"] = relative_position
        if text_content is not unset:
            kwargs["text_content"] = text_content
        if user_locator is not unset:
            kwargs["user_locator"] = user_locator
        if view_name is not unset:
            kwargs["view_name"] = view_name
        super().__init__(kwargs)
