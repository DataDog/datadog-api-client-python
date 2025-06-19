# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class EventPayloadAttributes(ModelComposed):
    def __init__(self, **kwargs):
        """
        JSON object for category-specific attributes. Schema is different per event category.

        :param author: The entity that made the change. Optional, if provided it must include `type` and `name`.
        :type author: ChangeEventCustomAttributesAuthor, optional

        :param change_metadata: Free form JSON object with information related to the `change` event. Supports up to 100 properties per object and a maximum nesting depth of 10 levels.
        :type change_metadata: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, optional

        :param changed_resource: A uniquely identified resource.
        :type changed_resource: ChangeEventCustomAttributesChangedResource

        :param impacted_resources: A list of resources impacted by this change. It is recommended to provide an impacted resource to display
            the change event at the correct location. Only resources of type `service` are supported. Maximum of 100 impacted resources allowed.
        :type impacted_resources: [ChangeEventCustomAttributesImpactedResourcesItems], optional

        :param new_value: Free form JSON object representing the new state of the changed resource.
        :type new_value: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, optional

        :param prev_value: Free form JSON object representing the previous state of the changed resource.
        :type prev_value: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, optional

        :param custom: Free form JSON object for arbitrary data. Supports up to 100 properties per object and a maximum nesting depth of 10 levels.
        :type custom: AlertEventCustomAttributesCustom, optional

        :param links: The links related to the event. Maximum of 20 links allowed.
        :type links: [AlertEventCustomAttributesLinksItems], optional

        :param priority: The priority of the alert.
        :type priority: AlertEventCustomAttributesPriority, optional

        :param status: The status of the alert.
        :type status: AlertEventCustomAttributesStatus
        """
        super().__init__(kwargs)

    @cached_property
    def _composed_schemas(_):
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        from datadog_api_client.v2.model.change_event_custom_attributes import ChangeEventCustomAttributes
        from datadog_api_client.v2.model.alert_event_custom_attributes import AlertEventCustomAttributes

        return {
            "oneOf": [
                ChangeEventCustomAttributes,
                AlertEventCustomAttributes,
            ],
        }
