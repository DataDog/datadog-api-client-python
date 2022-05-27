# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class MetricTagConfigurationCreateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.metric_tag_configuration_create_attributes import (
            MetricTagConfigurationCreateAttributes,
        )
        from datadog_api_client.v2.model.metric_tag_configuration_type import MetricTagConfigurationType

        return {
            "attributes": (MetricTagConfigurationCreateAttributes,),
            "id": (str,),
            "type": (MetricTagConfigurationType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self, id, type, *args, **kwargs):
        """
        Object for a single metric to be configure tags on.

        :param attributes: Object containing the definition of a metric tag configuration to be created.
        :type attributes: MetricTagConfigurationCreateAttributes, optional

        :param id: The metric name for this resource.
        :type id: str

        :param type: The metric tag configuration resource type.
        :type type: MetricTagConfigurationType
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.id = id
        self.type = type

    @classmethod
    def _from_openapi_data(cls, id, type, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(MetricTagConfigurationCreateData, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.id = id
        self.type = type
        return self
