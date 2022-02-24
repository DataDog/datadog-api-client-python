# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v1.model.logs_category_processor_category import LogsCategoryProcessorCategory
    from datadog_api_client.v1.model.logs_category_processor_type import LogsCategoryProcessorType

    globals()["LogsCategoryProcessorCategory"] = LogsCategoryProcessorCategory
    globals()["LogsCategoryProcessorType"] = LogsCategoryProcessorType


class LogsCategoryProcessor(ModelNormal):

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "categories": ([LogsCategoryProcessorCategory],),
            "is_enabled": (bool,),
            "name": (str,),
            "target": (str,),
            "type": (LogsCategoryProcessorType,),
        }

    attribute_map = {
        "categories": "categories",
        "is_enabled": "is_enabled",
        "name": "name",
        "target": "target",
        "type": "type",
    }

    read_only_vars = {}

    def __init__(self, categories, target, type, *args, **kwargs):
        """
        Use the Category Processor to add a new attribute (without spaces or special characters in the new attribute name)
        to a log matching a provided search query. Use categories to create groups for an analytical view.
        For example, URL groups, machine groups, environments, and response time buckets.

        **Notes**:

        - The syntax of the query is the one of Logs Explorer search bar.
          The query can be done on any log attribute or tag, whether it is a facet or not.
          Wildcards can also be used inside your query.
        - Once the log has matched one of the Processor queries, it stops.
          Make sure they are properly ordered in case a log could match several queries.
        - The names of the categories must be unique.
        - Once defined in the Category Processor, you can map categories to log status using the Log Status Remapper.

        :param categories: Array of filters to match or not a log and their
            corresponding `name`to assign a custom value to the log.
        :type categories: [LogsCategoryProcessorCategory]

        :param is_enabled: Whether or not the processor is enabled.
        :type is_enabled: bool, optional

        :param name: Name of the processor.
        :type name: str, optional

        :param target: Name of the target attribute which value is defined by the matching category.
        :type target: str

        :param type: Type of logs category processor.
        :type type: LogsCategoryProcessorType
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.categories = categories
        self.target = target
        self.type = type

    @classmethod
    def _from_openapi_data(cls, categories, target, type, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(LogsCategoryProcessor, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.categories = categories
        self.target = target
        self.type = type
        return self
