# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class FormTrigger(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "form_id": (str,),
        }

    attribute_map = {
        "form_id": "formId",
    }

    def __init__(self_, form_id: Union[str, UnsetType] = unset, **kwargs):
        """
        Trigger a workflow from a Form.

        :param form_id: The form UUID.
        :type form_id: str, optional
        """
        if form_id is not unset:
            kwargs["form_id"] = form_id
        super().__init__(kwargs)
