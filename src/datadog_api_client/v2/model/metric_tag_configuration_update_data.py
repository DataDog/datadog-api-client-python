# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v2.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v2.model.metric_tag_configuration_update_attributes import (
        MetricTagConfigurationUpdateAttributes,
    )
    from datadog_api_client.v2.model.metric_tag_configuration_type import MetricTagConfigurationType

    globals()["MetricTagConfigurationUpdateAttributes"] = MetricTagConfigurationUpdateAttributes
    globals()["MetricTagConfigurationType"] = MetricTagConfigurationType


class MetricTagConfigurationUpdateData(ModelNormal):

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "attributes": (MetricTagConfigurationUpdateAttributes,),
            "id": (str,),
            "type": (MetricTagConfigurationType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    read_only_vars = {}

    def __init__(self, id, type, *args, **kwargs):
        """
        Object for a single tag configuration to be edited.

        :param attributes: Object containing the definition of a metric tag configuration to be updated.
        :type attributes: MetricTagConfigurationUpdateAttributes, optional

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

        self = super(MetricTagConfigurationUpdateData, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.id = id
        self.type = type
        return self
