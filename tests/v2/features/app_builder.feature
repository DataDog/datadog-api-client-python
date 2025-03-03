@endpoint(app-builder) @endpoint(app-builder-v2)
Feature: App Builder
  Datadog App Builder provides a low-code solution to rapidly develop and
  integrate secure, customized applications into your monitoring stack that
  are built to accelerate remediation at scale. These API endpoints allow
  you to create, read, update, delete, and publish apps.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "AppBuilder" API

  @skip-typescript @team:DataDog/app-builder-backend
  Scenario: Create App returns "Bad Request" response
    Given new "CreateApp" request
    And body with value {"data": {"attributes": {"description": "This is a bad example app", "queries": [], "rootInstanceName": "grid0"}, "type": "appDefinitions"}}
    When the request is sent
    Then the response status is 400 Bad Request
    And the response "errors" has length 1
    And the response "errors[0].title" is equal to "missing required field"

  @skip-typescript @team:DataDog/app-builder-backend
  Scenario: Create App returns "Created" response
    Given new "CreateApp" request
    And body with value {"data":{"type":"appDefinitions","attributes":{"rootInstanceName":"grid0","components":[{"name":"grid0","type":"grid","properties":{"children":[{"type":"gridCell","name":"gridCell0","properties":{"children":[{"name":"text0","type":"text","properties":{"content":"# Cat Facts","contentType":"markdown","textAlign":"left","verticalAlign":"top","isVisible":true},"events":[]}],"isVisible":"true","layout":{"default":{"x":0,"y":0,"width":4,"height":5}}},"events":[]},{"type":"gridCell","name":"gridCell2","properties":{"children":[{"name":"table0","type":"table","properties":{"data":"${fetchFacts?.outputs?.body?.data}","columns":[{"dataPath":"fact","header":"fact","isHidden":false,"id":"0ae2ae9e-0280-4389-83c6-1c5949f7e674"},{"dataPath":"length","header":"length","isHidden":true,"id":"c9048611-0196-4a00-9366-1ef9e3ec0408"},{"id":"8fa9284b-7a58-4f13-9959-57b7d8a7fe8f","dataPath":"Due Date","header":"Unused Old Column","disableSortBy":false,"formatter":{"type":"formatted_time","format":"LARGE_WITHOUT_TIME"},"isDeleted":true}],"summary":true,"pageSize":"${pageSize?.value}","paginationType":"server_side","isLoading":"${fetchFacts?.isLoading}","rowButtons":[],"isWrappable":false,"isScrollable":"vertical","isSubRowsEnabled":false,"globalFilter":false,"isVisible":true,"totalCount":"${fetchFacts?.outputs?.body?.total}"},"events":[]}],"isVisible":"true","layout":{"default":{"x":0,"y":5,"width":12,"height":96}}},"events":[]},{"type":"gridCell","name":"gridCell1","properties":{"children":[{"name":"text1","type":"text","properties":{"content":"## Random Fact\n\n${randomFact?.outputs?.fact}","contentType":"markdown","textAlign":"left","verticalAlign":"top","isVisible":true},"events":[]}],"isVisible":"true","layout":{"default":{"x":0,"y":101,"width":12,"height":16}}},"events":[]},{"type":"gridCell","name":"gridCell3","properties":{"children":[{"name":"button0","type":"button","properties":{"label":"Increase Page Size","level":"default","isPrimary":true,"isBorderless":false,"isLoading":false,"isDisabled":false,"isVisible":true,"iconLeft":"angleUp","iconRight":""},"events":[{"variableName":"pageSize","value":"${pageSize?.value + 1}","name":"click","type":"setStateVariableValue"}]}],"isVisible":"true","layout":{"default":{"x":10,"y":134,"width":2,"height":4}}},"events":[]},{"type":"gridCell","name":"gridCell4","properties":{"children":[{"name":"button1","type":"button","properties":{"label":"Decrease Page Size","level":"default","isPrimary":true,"isBorderless":false,"isLoading":false,"isDisabled":false,"isVisible":true,"iconLeft":"angleDown","iconRight":""},"events":[{"variableName":"pageSize","value":"${pageSize?.value - 1}","name":"click","type":"setStateVariableValue"}]}],"isVisible":"true","layout":{"default":{"x":10,"y":138,"width":2,"height":4}}},"events":[]}],"backgroundColor":"default"},"events":[]}],"queries":[{"id":"92ff0bb8-553b-4f31-87c7-ef5bd16d47d5","type":"action","name":"fetchFacts","events":[],"properties":{"spec":{"fqn":"com.datadoghq.http.request","connectionId":"5e63f4a8-4ce6-47de-ba11-f6617c1d54f3","inputs":{"verb":"GET","url":"https://catfact.ninja/facts","urlParams":[{"key":"limit","value":"${pageSize.value.toString()}"},{"key":"page","value":"${(table0.pageIndex + 1).toString()}"}]}}}},{"type":"stateVariable","name":"pageSize","properties":{"defaultValue":"${20}"},"id":"afd03c81-4075-4432-8618-ba09d52d2f2d"},{"type":"dataTransform","name":"randomFact","properties":{"outputs":"${(() => {const facts = fetchFacts.outputs.body.data\nreturn facts[Math.floor(Math.random()*facts.length)]\n})()}"},"id":"0fb22859-47dc-4137-9e41-7b67d04c525c"}],"name":"Example Cat Facts Viewer","description":"This is a slightly complicated example app that fetches and displays cat facts"}}}
    When the request is sent
    Then the response status is 201 Created
    And the response "data.type" is equal to "appDefinitions"

  @skip @team:DataDog/app-builder-backend
  Scenario: Delete App returns "Bad Request" response
    Given new "DeleteApp" request
    And request contains "app_id" parameter with value "bad-app-id"
    When the request is sent
    Then the response status is 400 Bad Request

  @skip @team:DataDog/app-builder-backend
  Scenario: Delete App returns "Gone" response
    Given new "DeleteApp" request
    And request contains "app_id" parameter with value "7addb29b-f935-472c-ae79-d1963979a23e"
    When the request is sent
    Then the response status is 410 Gone

  @skip-typescript @team:DataDog/app-builder-backend
  Scenario: Delete App returns "Not Found" response
    Given new "DeleteApp" request
    And request contains "app_id" parameter with value "7addb29b-f935-472c-ae79-d1963979a23e"
    When the request is sent
    Then the response status is 404 Not Found

  @skip-typescript @team:DataDog/app-builder-backend
  Scenario: Delete App returns "OK" response
    Given there is a valid "app" in the system
    And new "DeleteApp" request
    And request contains "app_id" parameter from "app.data.id"
    When the request is sent
    Then the response status is 200 OK
    And the response "data.id" has the same value as "app.data.id"
    And the response "data.type" is equal to "appDefinitions"

  @generated @skip @team:DataDog/app-builder-backend
  Scenario: Delete Multiple Apps returns "Bad Request" response
    Given new "DeleteApps" request
    And body with value {"data": [{"id": "aea2ed17-b45f-40d0-ba59-c86b7972c901", "type": "appDefinitions"}, {"id": "f69bb8be-6168-4fe7-a30d-370256b6504a", "type": "appDefinitions"}, {"id": "ab1ed73e-13ad-4426-b0df-a0ff8876a088", "type": "appDefinitions"}]}
    When the request is sent
    Then the response status is 400 Bad Request

  @skip-typescript @team:DataDog/app-builder-backend
  Scenario: Delete Multiple Apps returns "Not Found" response
    Given new "DeleteApps" request
    And body with value {"data": [{"id": "aea2ed17-b45f-40d0-ba59-c86b7972c901", "type": "appDefinitions"}, {"id": "f69bb8be-6168-4fe7-a30d-370256b6504a", "type": "appDefinitions"}, {"id": "ab1ed73e-13ad-4426-b0df-a0ff8876a088", "type": "appDefinitions"}]}
    When the request is sent
    Then the response status is 404 Not Found

  @skip-typescript @team:DataDog/app-builder-backend
  Scenario: Delete Multiple Apps returns "OK" response
    Given new "DeleteApps" request
    And there is a valid "app" in the system
    And body with value {"data": [{"id": "{{ app.data.id }}", "type": "appDefinitions"}]}
    When the request is sent
    Then the response status is 200 OK
    And the response "data" has length 1
    And the response "data[0].id" has the same value as "app.data.id"

  @skip @team:DataDog/app-builder-backend
  Scenario: Get App returns "Bad Request" response
    Given new "GetApp" request
    And request contains "app_id" parameter with value "invalid-uuid"
    When the request is sent
    Then the response status is 400 Bad Request

  @skip-typescript @team:DataDog/app-builder-backend
  Scenario: Get App returns "Gone" response
    Given new "GetApp" request
    And there is a valid "app" in the system
    And request contains "app_id" parameter from "app.data.id"
    And request contains "version" parameter with value "31"
    When the request is sent
    Then the response status is 410 Gone

  @skip-typescript @team:DataDog/app-builder-backend
  Scenario: Get App returns "Not Found" response
    Given new "GetApp" request
    And request contains "app_id" parameter with value "7addb29b-f935-472c-ae79-d1963979a23e"
    When the request is sent
    Then the response status is 404 Not Found

  @skip-typescript @team:DataDog/app-builder-backend
  Scenario: Get App returns "OK" response
    Given new "GetApp" request
    And there is a valid "app" in the system
    And request contains "app_id" parameter from "app.data.id"
    When the request is sent
    Then the response status is 200 OK
    And the response "data.id" has the same value as "app.data.id"
    And the response "data.type" is equal to "appDefinitions"

  @generated @skip @team:DataDog/app-builder-backend
  Scenario: List Apps returns "Bad Request" response
    Given new "ListApps" request
    When the request is sent
    Then the response status is 400 Bad Request

  @skip-typescript @team:DataDog/app-builder-backend
  Scenario: List Apps returns "OK" response
    Given new "ListApps" request
    When the request is sent
    Then the response status is 200 OK

  @skip @team:DataDog/app-builder-backend
  Scenario: Publish App returns "Bad Request" response
    Given new "PublishApp" request
    And request contains "app_id" parameter with value "invalid-uuid"
    When the request is sent
    Then the response status is 400 Bad Request

  @skip-typescript @team:DataDog/app-builder-backend
  Scenario: Publish App returns "Created" response
    Given new "PublishApp" request
    And there is a valid "app" in the system
    And request contains "app_id" parameter from "app.data.id"
    When the request is sent
    Then the response status is 201 Created

  @skip-typescript @team:DataDog/app-builder-backend
  Scenario: Publish App returns "Not Found" response
    Given new "PublishApp" request
    And request contains "app_id" parameter with value "7addb29b-f935-472c-ae79-d1963979a23e"
    When the request is sent
    Then the response status is 404 Not Found

  @skip @team:DataDog/app-builder-backend
  Scenario: Unpublish App returns "Bad Request" response
    Given new "UnpublishApp" request
    And request contains "app_id" parameter with value "invalid-uuid"
    When the request is sent
    Then the response status is 400 Bad Request

  @skip-typescript @team:DataDog/app-builder-backend
  Scenario: Unpublish App returns "Not Found" response
    Given new "UnpublishApp" request
    And request contains "app_id" parameter with value "7addb29b-f935-472c-ae79-d1963979a23e"
    When the request is sent
    Then the response status is 404 Not Found

  @skip-typescript @team:DataDog/app-builder-backend
  Scenario: Unpublish App returns "OK" response
    Given new "UnpublishApp" request
    And there is a valid "app" in the system
    And request contains "app_id" parameter from "app.data.id"
    When the request is sent
    Then the response status is 200 OK

  @skip-typescript @team:DataDog/app-builder-backend
  Scenario: Update App returns "Bad Request" response
    Given new "UpdateApp" request
    And there is a valid "app" in the system
    And request contains "app_id" parameter from "app.data.id"
    And body with value {"data": {"attributes": {"rootInstanceName": ""}, "id": "{{ app.data.id }}", "type": "appDefinitions"}}
    When the request is sent
    Then the response status is 400 Bad Request
    And the response "errors" has length 1
    And the response "errors[0].title" is equal to "missing required field"

  @skip-typescript @team:DataDog/app-builder-backend
  Scenario: Update App returns "OK" response
    Given new "UpdateApp" request
    And there is a valid "app" in the system
    And request contains "app_id" parameter from "app.data.id"
    And body with value {"data": {"attributes": {"name": "Updated Name", "rootInstanceName": "grid0"}, "id": "{{ app.data.id }}", "type": "appDefinitions"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.id" has the same value as "app.data.id"
    And the response "data.type" is equal to "appDefinitions"
    And the response "data.attributes.name" is equal to "Updated Name"
