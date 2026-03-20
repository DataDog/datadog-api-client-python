# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.observability_pipeline_sensitive_data_scanner_processor_keyword_options import (
        ObservabilityPipelineSensitiveDataScannerProcessorKeywordOptions,
    )
    from datadog_api_client.v2.model.observability_pipeline_sensitive_data_scanner_processor_action import (
        ObservabilityPipelineSensitiveDataScannerProcessorAction,
    )
    from datadog_api_client.v2.model.observability_pipeline_sensitive_data_scanner_processor_pattern import (
        ObservabilityPipelineSensitiveDataScannerProcessorPattern,
    )
    from datadog_api_client.v2.model.observability_pipeline_sensitive_data_scanner_processor_scope import (
        ObservabilityPipelineSensitiveDataScannerProcessorScope,
    )
    from datadog_api_client.v2.model.observability_pipeline_sensitive_data_scanner_processor_action_redact import (
        ObservabilityPipelineSensitiveDataScannerProcessorActionRedact,
    )
    from datadog_api_client.v2.model.observability_pipeline_sensitive_data_scanner_processor_action_hash import (
        ObservabilityPipelineSensitiveDataScannerProcessorActionHash,
    )
    from datadog_api_client.v2.model.observability_pipeline_sensitive_data_scanner_processor_action_partial_redact import (
        ObservabilityPipelineSensitiveDataScannerProcessorActionPartialRedact,
    )
    from datadog_api_client.v2.model.observability_pipeline_sensitive_data_scanner_processor_custom_pattern import (
        ObservabilityPipelineSensitiveDataScannerProcessorCustomPattern,
    )
    from datadog_api_client.v2.model.observability_pipeline_sensitive_data_scanner_processor_library_pattern import (
        ObservabilityPipelineSensitiveDataScannerProcessorLibraryPattern,
    )
    from datadog_api_client.v2.model.observability_pipeline_sensitive_data_scanner_processor_scope_include import (
        ObservabilityPipelineSensitiveDataScannerProcessorScopeInclude,
    )
    from datadog_api_client.v2.model.observability_pipeline_sensitive_data_scanner_processor_scope_exclude import (
        ObservabilityPipelineSensitiveDataScannerProcessorScopeExclude,
    )
    from datadog_api_client.v2.model.observability_pipeline_sensitive_data_scanner_processor_scope_all import (
        ObservabilityPipelineSensitiveDataScannerProcessorScopeAll,
    )


class ObservabilityPipelineSensitiveDataScannerProcessorRule(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_sensitive_data_scanner_processor_keyword_options import (
            ObservabilityPipelineSensitiveDataScannerProcessorKeywordOptions,
        )
        from datadog_api_client.v2.model.observability_pipeline_sensitive_data_scanner_processor_action import (
            ObservabilityPipelineSensitiveDataScannerProcessorAction,
        )
        from datadog_api_client.v2.model.observability_pipeline_sensitive_data_scanner_processor_pattern import (
            ObservabilityPipelineSensitiveDataScannerProcessorPattern,
        )
        from datadog_api_client.v2.model.observability_pipeline_sensitive_data_scanner_processor_scope import (
            ObservabilityPipelineSensitiveDataScannerProcessorScope,
        )

        return {
            "keyword_options": (ObservabilityPipelineSensitiveDataScannerProcessorKeywordOptions,),
            "name": (str,),
            "on_match": (ObservabilityPipelineSensitiveDataScannerProcessorAction,),
            "pattern": (ObservabilityPipelineSensitiveDataScannerProcessorPattern,),
            "scope": (ObservabilityPipelineSensitiveDataScannerProcessorScope,),
            "tags": ([str],),
        }

    attribute_map = {
        "keyword_options": "keyword_options",
        "name": "name",
        "on_match": "on_match",
        "pattern": "pattern",
        "scope": "scope",
        "tags": "tags",
    }

    def __init__(
        self_,
        name: str,
        on_match: Union[
            ObservabilityPipelineSensitiveDataScannerProcessorAction,
            ObservabilityPipelineSensitiveDataScannerProcessorActionRedact,
            ObservabilityPipelineSensitiveDataScannerProcessorActionHash,
            ObservabilityPipelineSensitiveDataScannerProcessorActionPartialRedact,
        ],
        pattern: Union[
            ObservabilityPipelineSensitiveDataScannerProcessorPattern,
            ObservabilityPipelineSensitiveDataScannerProcessorCustomPattern,
            ObservabilityPipelineSensitiveDataScannerProcessorLibraryPattern,
        ],
        scope: Union[
            ObservabilityPipelineSensitiveDataScannerProcessorScope,
            ObservabilityPipelineSensitiveDataScannerProcessorScopeInclude,
            ObservabilityPipelineSensitiveDataScannerProcessorScopeExclude,
            ObservabilityPipelineSensitiveDataScannerProcessorScopeAll,
        ],
        tags: List[str],
        keyword_options: Union[ObservabilityPipelineSensitiveDataScannerProcessorKeywordOptions, UnsetType] = unset,
        **kwargs,
    ):
        """
        Defines a rule for detecting sensitive data, including matching pattern, scope, and the action to take.

        :param keyword_options: Configuration for keywords used to reinforce sensitive data pattern detection.
        :type keyword_options: ObservabilityPipelineSensitiveDataScannerProcessorKeywordOptions, optional

        :param name: A name identifying the rule.
        :type name: str

        :param on_match: Defines what action to take when sensitive data is matched.
        :type on_match: ObservabilityPipelineSensitiveDataScannerProcessorAction

        :param pattern: Pattern detection configuration for identifying sensitive data using either a custom regex or a library reference.
        :type pattern: ObservabilityPipelineSensitiveDataScannerProcessorPattern

        :param scope: Determines which parts of the log the pattern-matching rule should be applied to.
        :type scope: ObservabilityPipelineSensitiveDataScannerProcessorScope

        :param tags: Tags assigned to this rule for filtering and classification.
        :type tags: [str]
        """
        if keyword_options is not unset:
            kwargs["keyword_options"] = keyword_options
        super().__init__(kwargs)

        self_.name = name
        self_.on_match = on_match
        self_.pattern = pattern
        self_.scope = scope
        self_.tags = tags
