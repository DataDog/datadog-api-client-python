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
    from datadog_api_client.v2.model.clone_form_data_attributes import CloneFormDataAttributes
    from datadog_api_client.v2.model.form_type import FormType


class CloneFormData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.clone_form_data_attributes import CloneFormDataAttributes
        from datadog_api_client.v2.model.form_type import FormType

        return {
            "attributes": (CloneFormDataAttributes,),
            "type": (FormType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, type: FormType, attributes: Union[CloneFormDataAttributes, UnsetType] = unset, **kwargs):
        """
        The data for cloning a form.

        :param attributes: The attributes for cloning a form.
        :type attributes: CloneFormDataAttributes, optional

        :param type: The resource type for a form.
        :type type: FormType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        super().__init__(kwargs)

        self_.type = type
