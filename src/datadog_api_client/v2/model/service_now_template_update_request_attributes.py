# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Dict, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
    UUID,
)


class ServiceNowTemplateUpdateRequestAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "assignment_group_id": (UUID,),
            "business_service_id": (UUID,),
            "fields_mapping": ({str: (str,)},),
            "handle_name": (str,),
            "instance_id": (UUID,),
            "servicenow_tablename": (str,),
            "user_id": (UUID,),
        }

    attribute_map = {
        "assignment_group_id": "assignment_group_id",
        "business_service_id": "business_service_id",
        "fields_mapping": "fields_mapping",
        "handle_name": "handle_name",
        "instance_id": "instance_id",
        "servicenow_tablename": "servicenow_tablename",
        "user_id": "user_id",
    }

    def __init__(
        self_,
        handle_name: str,
        instance_id: UUID,
        servicenow_tablename: str,
        assignment_group_id: Union[UUID, UnsetType] = unset,
        business_service_id: Union[UUID, UnsetType] = unset,
        fields_mapping: Union[Dict[str, str], UnsetType] = unset,
        user_id: Union[UUID, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for updating a ServiceNow template

        :param assignment_group_id: The ID of the assignment group
        :type assignment_group_id: UUID, optional

        :param business_service_id: The ID of the business service
        :type business_service_id: UUID, optional

        :param fields_mapping: Custom field mappings for the template
        :type fields_mapping: {str: (str,)}, optional

        :param handle_name: The handle name of the template
        :type handle_name: str

        :param instance_id: The ID of the ServiceNow instance
        :type instance_id: UUID

        :param servicenow_tablename: The name of the destination ServiceNow table
        :type servicenow_tablename: str

        :param user_id: The ID of the user
        :type user_id: UUID, optional
        """
        if assignment_group_id is not unset:
            kwargs["assignment_group_id"] = assignment_group_id
        if business_service_id is not unset:
            kwargs["business_service_id"] = business_service_id
        if fields_mapping is not unset:
            kwargs["fields_mapping"] = fields_mapping
        if user_id is not unset:
            kwargs["user_id"] = user_id
        super().__init__(kwargs)

        self_.handle_name = handle_name
        self_.instance_id = instance_id
        self_.servicenow_tablename = servicenow_tablename
