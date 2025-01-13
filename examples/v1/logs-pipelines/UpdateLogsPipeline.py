"""
Update a pipeline returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.logs_pipelines_api import LogsPipelinesApi
from datadog_api_client.v1.model.logs_filter import LogsFilter
from datadog_api_client.v1.model.logs_grok_parser import LogsGrokParser
from datadog_api_client.v1.model.logs_grok_parser_rules import LogsGrokParserRules
from datadog_api_client.v1.model.logs_grok_parser_type import LogsGrokParserType
from datadog_api_client.v1.model.logs_pipeline import LogsPipeline

body = LogsPipeline(
    filter=LogsFilter(
        query="source:python",
    ),
    name="",
    processors=[
        LogsGrokParser(
            grok=LogsGrokParserRules(
                match_rules="rule_name_1 foo\nrule_name_2 bar\n",
                support_rules="rule_name_1 foo\nrule_name_2 bar\n",
            ),
            is_enabled=False,
            samples=[],
            source="message",
            type=LogsGrokParserType.GROK_PARSER,
        ),
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = LogsPipelinesApi(api_client)
    response = api_instance.update_logs_pipeline(pipeline_id="pipeline_id", body=body)

    print(response)
