# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v1.model.logs_lookup_processor_type import LogsLookupProcessorType

    globals()["LogsLookupProcessorType"] = LogsLookupProcessorType


class LogsLookupProcessor(ModelNormal):

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "default_lookup": (str,),
            "is_enabled": (bool,),
            "lookup_table": ([str],),
            "name": (str,),
            "source": (str,),
            "target": (str,),
            "type": (LogsLookupProcessorType,),
        }

    attribute_map = {
        "default_lookup": "default_lookup",
        "is_enabled": "is_enabled",
        "lookup_table": "lookup_table",
        "name": "name",
        "source": "source",
        "target": "target",
        "type": "type",
    }

    read_only_vars = {}

    def __init__(self, lookup_table, source, target, type, *args, **kwargs):
        """
        Use the Lookup Processor to define a mapping between a log attribute
        and a human readable value saved in the processors mapping table.
        For example, you can use the Lookup Processor to map an internal service ID
        into a human readable service name. Alternatively, you could also use it to check
        if the MAC address that just attempted to connect to the production
        environment belongs to your list of stolen machines.

        :param default_lookup: Value to set the target attribute if the source value is not found in the list.
        :type default_lookup: str, optional

        :param is_enabled: Whether or not the processor is enabled.
        :type is_enabled: bool, optional

        :param lookup_table: Mapping table of values for the source attribute and their associated target attribute values,
            formatted as `["source_key1,target_value1", "source_key2,target_value2"]`
        :type lookup_table: [str]

        :param name: Name of the processor.
        :type name: str, optional

        :param source: Source attribute used to perform the lookup.
        :type source: str

        :param target: Name of the attribute that contains the corresponding value in the mapping list
            or the `default_lookup` if not found in the mapping list.
        :type target: str

        :param type: Type of logs lookup processor.
        :type type: LogsLookupProcessorType
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.lookup_table = lookup_table
        self.source = source
        self.target = target
        self.type = type

    @classmethod
    def _from_openapi_data(cls, lookup_table, source, target, type, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(LogsLookupProcessor, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.lookup_table = lookup_table
        self.source = source
        self.target = target
        self.type = type
        return self
