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


class IntegrationIncidentFieldMappingsItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "case_field": (str,),
            "incident_user_defined_field_id": (str,),
        }

    attribute_map = {
        "case_field": "case_field",
        "incident_user_defined_field_id": "incident_user_defined_field_id",
    }

    def __init__(
        self_,
        case_field: Union[str, UnsetType] = unset,
        incident_user_defined_field_id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """


        :param case_field:
        :type case_field: str, optional

        :param incident_user_defined_field_id:
        :type incident_user_defined_field_id: str, optional
        """
        if case_field is not unset:
            kwargs["case_field"] = case_field
        if incident_user_defined_field_id is not unset:
            kwargs["incident_user_defined_field_id"] = incident_user_defined_field_id
        super().__init__(kwargs)
