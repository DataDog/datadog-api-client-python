# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class V2EventAttributesAttributes(ModelComposed):
    def __init__(self, **kwargs):
        """
        JSON object for category-specific attributes.

        :param aggregation_key: Aggregation key of the event.
        :type aggregation_key: str, optional

        :param author: The entity that made the change.
        :type author: ChangeEventAttributesAuthor, optional

        :param change_metadata: JSON object of change metadata.
        :type change_metadata: dict, optional

        :param changed_resource: A uniquely identified resource.
        :type changed_resource: ChangeEventAttributesChangedResource, optional

        :param evt: JSON object of event system attributes.
        :type evt: EventSystemAttributes, optional

        :param impacted_resources: A list of resources impacted by this change.
        :type impacted_resources: [ChangeEventAttributesImpactedResourcesItem], optional

        :param new_value: The new state of the changed resource.
        :type new_value: dict, optional

        :param prev_value: The previous state of the changed resource.
        :type prev_value: dict, optional

        :param service: Service that triggered the event.
        :type service: str, optional

        :param timestamp: POSIX timestamp of the event.
        :type timestamp: int, optional

        :param title: The title of the event.
        :type title: str, optional

        :param custom: JSON object of custom attributes.
        :type custom: dict, optional

        :param links: The links related to the event.
        :type links: [AlertEventAttributesLinksItem], optional

        :param priority: The priority of the alert.
        :type priority: AlertEventAttributesPriority, optional

        :param status: The status of the alert.
        :type status: AlertEventAttributesStatus, optional
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
        from datadog_api_client.v2.model.change_event_attributes import ChangeEventAttributes
        from datadog_api_client.v2.model.alert_event_attributes import AlertEventAttributes

        return {
            "oneOf": [
                ChangeEventAttributes,
                AlertEventAttributes,
            ],
        }
