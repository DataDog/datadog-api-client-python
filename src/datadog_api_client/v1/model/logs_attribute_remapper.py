# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v1.model.target_format_type import TargetFormatType
    from datadog_api_client.v1.model.logs_attribute_remapper_type import LogsAttributeRemapperType

    globals()["TargetFormatType"] = TargetFormatType
    globals()["LogsAttributeRemapperType"] = LogsAttributeRemapperType


class LogsAttributeRemapper(ModelNormal):

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "is_enabled": (bool,),
            "name": (str,),
            "override_on_conflict": (bool,),
            "preserve_source": (bool,),
            "source_type": (str,),
            "sources": ([str],),
            "target": (str,),
            "target_format": (TargetFormatType,),
            "target_type": (str,),
            "type": (LogsAttributeRemapperType,),
        }

    attribute_map = {
        "is_enabled": "is_enabled",
        "name": "name",
        "override_on_conflict": "override_on_conflict",
        "preserve_source": "preserve_source",
        "source_type": "source_type",
        "sources": "sources",
        "target": "target",
        "target_format": "target_format",
        "target_type": "target_type",
        "type": "type",
    }

    read_only_vars = {}

    def __init__(self, sources, target, type, *args, **kwargs):
        """
        The remapper processor remaps any source attribute(s) or tag to another target attribute or tag.
        Constraints on the tag/attribute name are explained in the [Tag Best Practice documentation](https://docs.datadoghq.com/logs/guide/log-parsing-best-practice).
        Some additional constraints are applied as `:` or `,` are not allowed in the target tag/attribute name.

        :param is_enabled: Whether or not the processor is enabled.
        :type is_enabled: bool, optional

        :param name: Name of the processor.
        :type name: str, optional

        :param override_on_conflict: Override or not the target element if already set,
        :type override_on_conflict: bool, optional

        :param preserve_source: Remove or preserve the remapped source element.
        :type preserve_source: bool, optional

        :param source_type: Defines if the sources are from log `attribute` or `tag`.
        :type source_type: str, optional

        :param sources: Array of source attributes.
        :type sources: [str]

        :param target: Final attribute or tag name to remap the sources to.
        :type target: str

        :param target_format: If the `target_type` of the remapper is `attribute`, try to cast the value to a new specific type.
            If the cast is not possible, the original type is kept. `string`, `integer`, or `double` are the possible types.
            If the `target_type` is `tag`, this parameter may not be specified.
        :type target_format: TargetFormatType, optional

        :param target_type: Defines if the final attribute or tag name is from log `attribute` or `tag`.
        :type target_type: str, optional

        :param type: Type of logs attribute remapper.
        :type type: LogsAttributeRemapperType
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.sources = sources
        self.target = target
        self.type = type

    @classmethod
    def _from_openapi_data(cls, sources, target, type, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(LogsAttributeRemapper, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.sources = sources
        self.target = target
        self.type = type
        return self
