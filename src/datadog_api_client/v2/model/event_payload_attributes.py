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
        JSON object for custom attributes. Schema are different per each event category.

        :param author: Object representing the entity which made the change. Optional field but if provided should include `type` and `name`.
        :type author: ChangeEventCustomAttributesAuthor, optional

        :param change_metadata: Free form object with information related to the `change` event. Can be arbitrarily nested and contain any valid JSON.
        :type change_metadata: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, optional

        :param changed_resource: Object representing a uniquely identified resource.
        :type changed_resource: ChangeEventCustomAttributesChangedResource

        :param impacted_resources: A list of resources impacted by this change. It is recommended to provide an impacted resource to display
            the change event at the right location. Only resources of type `service` are supported.
        :type impacted_resources: [ChangeEventCustomAttributesImpactedResourcesItems], optional

        :param new_value: Free form object to track new value of the changed resource.
        :type new_value: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, optional

        :param prev_value: Free form object to track previous value of the changed resource.
        :type prev_value: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, optional
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

        return {
            "oneOf": [
                ChangeEventCustomAttributes,
            ],
        }
